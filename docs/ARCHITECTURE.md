# Count-Me-In: System Architecture

## Overview

Count-Me-In is a distributed system consisting of three main components:

1. **Edge Service**: Real-time video processing and person detection
2. **Backend Service**: REST API, data persistence, and business logic
3. **Frontend**: Web dashboard and mobile applications

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        USER INTERFACES                           │
├──────────────────────┬──────────────────────┬──────────────────┤
│   Web Dashboard      │   Mobile App         │   Admin Portal   │
│   (React/Vue)        │   (React Native)     │   (React)        │
└──────────────┬───────┴──────────────┬───────┴──────────┬────────┘
               │                      │                  │
               │        HTTP/REST     │                  │
               └──────────────┬───────┘                  │
                              │                          │
                ┌─────────────▼──────────────┐          │
                │    BACKEND API SERVER      │          │
                │  (FastAPI/Flask)           │          │
                │                            │          │
                │  ┌──────────────────────┐ │          │
                │  │  Authentication      │ │          │
                │  ├──────────────────────┤ │          │
                │  │  Route Handlers      │ │          │
                │  ├──────────────────────┤ │          │
                │  │  Business Logic      │ │          │
                │  ├──────────────────────┤ │          │
                │  │  Message Queue       │ │          │
                │  └──────────────────────┘ │          │
                └──────────────┬──────────────┘          │
                               │                         │
                   ┌───────────┼───────────┐             │
                   │           │           │             │
           PostgreSQL      Redis        WebSocket       │
           (Persistence) (Cache/RT)     (Live Data)     │
                   │           │           │             │
                   └───────────┼───────────┘             │
                               │                         │
                               │                         │
        ┌──────────────────────┴─────────────────────┐  │
        │                                            │  │
    ┌───▼────┐                                   ┌──▼──▼───┐
    │  EDGE  │                                   │ EXTERNAL│
    │SERVICE │                                   │ SYSTEMS │
    │        │                                   │(Webhooks│
    │┌──────┐│                                   │Email)   │
    ││YOLO  ││                                   └─────────┘
    ││Model ││
    │└──────┘│
    │┌──────┐│
    ││Object││   Camera/Stream Input
    ││Track ││ ◄─────────────────────
    │└──────┘│
    │┌──────┐│
    ││Alert ││
    ││Logic ││
    │└──────┘│
    └───┬────┘
        │
   Vehicle Data, Occupancy Counts, Alerts
```

## Component Details

### 1. Edge Service

**Purpose**: Real-time video processing and AI inference at the source

**Technologies**:
- Python 3.9+
- YOLOv8/v10 for person detection
- OpenCV for video processing
- PyTorch/TensorRT for optimized inference

**Key Modules**:

```python
edge/
├── main.py              # Entry point, orchestrates processing loop
├── detector.py          # YOLO inference wrapper
├── tracker.py           # Multi-object tracker (ByteTrack/DeepSORT)
├── camera_handler.py    # Handles camera/stream input
├── payload_builder.py   # Constructs data for backend
└── config.py            # Configuration loader
```

**Data Flow**:

```
Camera/Stream Input
        │
        ▼
  Frame Buffer
        │
        ▼
  YOLO Detection
        │
   ┌────┴────┐
   ▼         ▼
 Bounding  Confidence
   Boxes    Scores
        │
        ▼
   Tracker
        │
        ▼
  Occupancy Count
        │
        ▼
  Alert Checks
        │
        ▼
  Payload Creation
        │
        ▼
  Backend API Call
```

**Performance Characteristics**:
- Latency: <200ms per frame
- FPS: 20-30 on edge hardware (Jetson Nano/Xavier)
- Memory: ~2-4GB RAM required
- Power: Optimized for low-power edge devices

### 2. Backend Service

**Purpose**: Central API, data persistence, and business logic

**Technologies**:
- Python (FastAPI recommended for performance)
- PostgreSQL for persistence
- Redis for caching and pub/sub
- SQLAlchemy ORM
- Pydantic for data validation

**Key Modules**:

```python
backend/
├── app.py                    # FastAPI/Flask initialization
├── routes/
│   ├── vehicles.py          # Vehicle CRUD operations
│   ├── occupancy.py         # Occupancy data endpoints
│   ├── analytics.py         # Analytics and reporting
│   ├── alerts.py            # Alert management
│   └── health.py            # Health checks
├── models/
│   ├── vehicle.py           # Vehicle model
│   ├── occupancy_reading.py # Occupancy records
│   ├── alert.py             # Alert model
│   └── user.py              # User authentication
├── services/
│   ├── occupancy_service.py # Occupancy logic
│   ├── alert_service.py     # Alert generation
│   ├── analytics_service.py # Report generation
│   └── cache_service.py     # Redis caching
└── middleware/
    ├── auth.py              # JWT authentication
    └── error_handler.py     # Error handling
```

**API Layers**:

1. **Request Layer**: FastAPI route handlers
2. **Validation Layer**: Pydantic models
3. **Service Layer**: Business logic implementation
4. **Data Layer**: SQLAlchemy models and queries
5. **Cache Layer**: Redis for hot data

**Data Models**:

```sql
Vehicles
├── id (PK)
├── registration_number
├── capacity
├── location
└── route_id

Occupancy_Readings
├── id (PK)
├── vehicle_id (FK)
├── timestamp
├── person_count
├── confidence
└── frame_data

Alerts
├── id (PK)
├── vehicle_id (FK)
├── alert_type (CAPACITY_HIGH, CRITICAL, etc.)
├── timestamp
├── occupancy_percent
└── acknowledged

Users
├── id (PK)
├── email (UNIQUE)
├── password_hash
├── role (ADMIN, OPERATOR, VIEWER)
└── created_at
```

**API Endpoints**:

```
GET    /api/vehicles                    # List all vehicles
GET    /api/vehicles/:id                # Get vehicle details
POST   /api/vehicles                    # Create vehicle
PUT    /api/vehicles/:id                # Update vehicle

GET    /api/vehicles/:id/occupancy      # Current occupancy
GET    /api/occupancy/history           # Historical data
POST   /api/occupancy/readings          # Record occupancy (from edge)

GET    /api/alerts                      # List alerts
POST   /api/alerts                      # Create alert
PUT    /api/alerts/:id/acknowledge      # Acknowledge alert

GET    /api/analytics/occupancy-report  # Generate reports
GET    /api/analytics/peak-hours        # Peak occupancy times
GET    /api/analytics/vehicle-stats     # Vehicle statistics

WS     /ws/live/:vehicle_id             # Real-time occupancy stream

POST   /api/auth/login                  # User authentication
POST   /api/auth/logout                 # User logout
GET    /api/health                      # Health check
```

### 3. Frontend - Dashboard

**Purpose**: Real-time visualization and monitoring

**Technologies**:
- React/Vue.js
- WebSocket for real-time updates
- Chart.js/D3.js for analytics
- Material-UI or Tailwind CSS

**Key Pages**:

1. **Overview Dashboard**: Fleet-wide occupancy overview
2. **Vehicle Detail**: Individual vehicle metrics
3. **Alerts Management**: Active and historical alerts
4. **Analytics**: Reports and trends
5. **Administration**: User and system management

### 4. Frontend - Mobile App

**Purpose**: Passenger information and booking

**Technologies**:
- React Native or Flutter
- Local state management (Redux/Provider)
- Push notifications

**Key Screens**:

1. **Route Finder**: Search routes and capacity
2. **Real-time Capacity**: Current vehicle occupancy
3. **Alerts**: Overcrowding warnings
4. **Favorites**: Saved routes

## Data Flow Scenarios

### Scenario 1: Normal Occupancy Reading

```
1. Edge device processes video frame
2. YOLO detects persons → person_count = 45
3. Edge creates payload:
   {
     "vehicle_id": "V001",
     "timestamp": "2024-01-15T10:30:00Z",
     "person_count": 45,
     "confidence": 0.92,
     "frame_data": "base64_encoded_frame"
   }
4. Edge sends POST to /api/occupancy/readings
5. Backend:
   - Validates data
   - Stores in PostgreSQL
   - Updates Redis cache
   - Broadcasts via WebSocket
6. Dashboard receives update via WebSocket
7. Dashboard updates occupancy visualization in real-time
```

### Scenario 2: Alert Generation

```
1. Edge reads occupancy = 85 persons in 100-capacity vehicle
2. Occupancy percentage = 85%
3. Edge checks threshold (default: 85%)
4. Alert triggered! Edge sends to backend
5. Backend:
   - Creates Alert record
   - Updates vehicle status to "OVERCROWDED"
   - Sends webhook to external system
   - Sends email/SMS notifications
   - Triggers notification in WebSocket
6. Dashboard displays alert banner
7. Mobile app receives push notification
8. Admin acknowledges alert via dashboard
```

### Scenario 3: Analytics Report Request

```
1. User requests "Last 24 hours occupancy report"
2. Dashboard sends: GET /api/analytics/occupancy-report?hours=24
3. Backend:
   - Queries PostgreSQL for readings in timeframe
   - Aggregates occupancy statistics
   - Calculates peak hours, averages
   - Generates charts data
4. Backend returns JSON with analytics
5. Dashboard renders charts and tables
```

## Deployment Architecture

### Single-Vehicle Deployment
```
┌─────────────────┐
│  Edge Device    │
│  (Jetson Nano)  │
└────────┬────────┘
         │ HTTPS
         │
    ┌────▼─────────┐
    │  Backend     │
    │  (Cloud)     │
    └────┬─────────┘
         │
    ┌────▼──────────┐
    │  PostgreSQL   │
    │  + Redis      │
    └───────────────┘
```

### Multi-Fleet Deployment
```
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ Edge Device  │  │ Edge Device  │  │ Edge Device  │
│   (Bus 1)    │  │   (Bus 2)    │  │   (Bus N)    │
└──────┬───────┘  └──────┬───────┘  └──────┬───────┘
       │                 │                  │
       └─────────────────┼──────────────────┘
                         │ Load Balancer
                         │
         ┌───────────────┼───────────────┐
         │               │               │
    ┌────▼────┐      ┌────▼────┐   ┌────▼────┐
    │Backend 1 │      │Backend 2 │   │Backend N │
    └────┬────┘      └────┬────┘   └────┬────┘
         │                │             │
         └────────┬───────┴─────────────┘
                  │
         ┌────────▼──────────┐
         │  PostgreSQL       │
         │  (Replicated)     │
         │  + Redis Cluster  │
         └───────────────────┘
```

## Scalability Considerations

### Horizontal Scaling
- Multiple edge devices feeding to single backend
- Multiple backend instances behind load balancer
- Database replication and sharding
- Cache clustering (Redis Cluster)

### Vertical Scaling
- Increased edge device hardware (Jetson Xavier)
- Larger VM instances for backend
- Read replicas for database
- CDN for static assets

## Security Architecture

### Authentication & Authorization
- JWT tokens for API authentication
- Role-based access control (RBAC)
- API key for edge devices
- OAuth2 for third-party integrations

### Data Protection
- HTTPS/TLS for all communications
- Database encryption at rest
- Sensitive data masking in logs
- Regular security audits

### Network Security
- VPC isolation
- Firewall rules
- Rate limiting
- DDoS protection

## Monitoring & Observability

### Metrics Collected
- API response times
- Database query performance
- Edge device inference latency
- System resource utilization
- Alert frequencies and types

### Logging
- Structured JSON logging
- Centralized log aggregation (ELK stack)
- Log retention policies

### Alerting
- Service health alerts
- High latency alerts
- Database performance alerts
- Device disconnection alerts

## Future Enhancements

1. **Multi-Zone Tracking**: Track persons across multiple cameras
2. **Anomaly Detection**: Identify unusual crowding patterns
3. **Predictive Analytics**: Forecast occupancy trends
4. **Computer Vision**: Age/gender demographics (privacy-respecting)
5. **ML Model Optimization**: Continuous model retraining
6. **Edge Orchestration**: Kubernetes for edge deployment
