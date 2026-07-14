# Count-Me-In: AI-Based Real-Time Passenger Detection and Capacity Monitoring System

## Overview

**Count-Me-In** is an intelligent, real-time passenger detection and capacity monitoring system designed for public transportation networks (buses, trains, metro systems). It uses computer vision and AI models to accurately count passengers, monitor vehicle occupancy, and provide real-time capacity alerts to prevent overcrowding.

## Key Features

- **Real-Time Passenger Detection**: Uses YOLO v8/v10 for fast, accurate person detection
- **Occupancy Tracking**: Monitors vehicle capacity in real-time with visual alerts
- **Edge Processing**: Runs inference on edge devices for minimal latency
- **Multi-Mode Support**: Works with video feeds, RTSP streams, and live camera feeds
- **Dashboard Analytics**: Web-based dashboard for fleet monitoring and analytics
- **Mobile Integration**: Commuter app for real-time capacity information
- **Data Persistence**: PostgreSQL backend for historical analytics and reporting

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     SYSTEM ARCHITECTURE                      │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────┐         ┌──────────────┐                  │
│  │   EDGE       │         │   BACKEND    │                  │
│  │  ┌────────┐  │         │  ┌────────┐  │                  │
│  │  │ YOLO   │  │◄────────┼─►│ API    │  │                  │
│  │  │ Model  │  │         │  │Server  │  │                  │
│  │  └────────┘  │         │  └────────┘  │                  │
│  └──────────────┘         │  ┌────────┐  │                  │
│         ▲                 │  │Database│  │                  │
│         │                 │  └────────┘  │                  │
│    Camera Streams         └──────────────┘                  │
│         │                        ▲                           │
│         │                        │                           │
│         ▼                        ▼                           │
│  ┌──────────────┐         ┌──────────────┐                  │
│  │  DASHBOARD   │         │   MOBILE     │                  │
│  │  Web UI      │         │   APP        │                  │
│  └──────────────┘         └──────────────┘                  │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

## Project Structure

```
Count-Me-In/
├── edge/                    # Edge inference service
│   ├── main.py              # Entry point for edge processing
│   ├── detector.py          # YOLO detection logic
│   ├── tracker.py           # Multi-object tracking
│   ├── camera_handler.py    # Camera/stream input management
│   ├── config.py            # Configuration management
│   └── requirements.txt      # Edge dependencies
│
├── models/                  # AI/ML models
│   ├── yolo_v8/             # YOLOv8 person detection model
│   ├── yolo_v10/            # YOLOv10 person detection model (optional)
│   ├── training/            # Model training scripts
│   └── README.md            # Model documentation
│
├── backend/                 # REST API server
│   ├── app.py               # Flask/FastAPI app initialization
│   ├── routes/
│   │   ├── vehicles.py      # Vehicle management endpoints
│   │   ├── analytics.py     # Analytics endpoints
│   │   ├── alerts.py        # Alert endpoints
│   │   └── health.py        # Health check endpoints
│   ├── models/              # Data models (SQLAlchemy)
│   │   ├── vehicle.py
│   │   ├── occupancy.py
│   │   └── alert.py
│   ├── services/            # Business logic
│   │   ├── occupancy_service.py
│   │   ├── alert_service.py
│   │   └── analytics_service.py
│   ├── database/            # Database setup
│   │   ├── db.py
│   │   └── migrations/      # Alembic migrations
│   ├── config.py            # Configuration
│   ├── requirements.txt      # Backend dependencies
│   └── wsgi.py              # Production WSGI entry
│
├── dashboard/               # Web dashboard (React/Vue)
│   ├── public/              # Static assets
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── pages/           # Page components
│   │   ├── services/        # API client services
│   │   ├── store/           # State management
│   │   ├── styles/          # Styling
│   │   ├── App.jsx          # Main app component
│   │   └── index.jsx        # Entry point
│   ├── package.json
│   └── README.md
│
├── commuter_app/            # Mobile app (React Native/Flutter)
│   ├── src/
│   │   ├── screens/         # App screens
│   │   ├── components/      # Reusable components
│   │   ├── services/        # API client
│   │   ├── redux/           # State management
│   │   └── App.tsx          # App initialization
│   ├── android/
│   ├── ios/
│   ├── package.json
│   └── README.md
│
├── database/                # Database configuration
│   ├── schema.sql           # Database schema
│   ├── seeds/               # Seed data
│   └── README.md
│
├── tests/                   # Test suite
│   ├── unit/                # Unit tests
│   ├── integration/         # Integration tests
│   ├── e2e/                 # End-to-end tests
│   └── fixtures/            # Test fixtures
│
├── docs/                    # Documentation
│   ├── ARCHITECTURE.md      # System architecture
│   ├── API.md               # API documentation
│   ├── DEPLOYMENT.md        # Deployment guide
│   ├── SETUP.md             # Setup instructions
│   └── MODEL_TRAINING.md    # Model training guide
│
├── scripts/                 # Utility scripts
│   ├── setup.sh             # Initial setup
│   ├── migrate.sh           # Database migrations
│   ├── train_model.py       # Model training
│   └── docker_build.sh      # Docker build
│
├── .github/
│   ├── workflows/           # CI/CD pipelines
│   │   ├── test.yml         # Testing workflow
│   │   ├── deploy.yml       # Deployment workflow
│   │   └── lint.yml         # Code quality checks
│   └── ISSUE_TEMPLATE/      # Issue templates
│
├── docker/
│   ├── Dockerfile.edge      # Edge service dockerfile
│   ├── Dockerfile.backend   # Backend dockerfile
│   ├── Dockerfile.dashboard # Dashboard dockerfile
│   └── docker-compose.yml   # Docker compose
│
├── .env.example             # Environment variables template
├── .gitignore
├── LICENSE
├── CONTRIBUTING.md
└── README.md
```

## Quick Start

### Prerequisites
- Python 3.9+
- Node.js 16+
- PostgreSQL 12+
- Docker & Docker Compose (optional)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ijohnanthone/Count-Me-In-An-AI-Based-Real-Time-Passenger-Detection-And-Capacity-Monitoring-System-.git
   cd Count-Me-In-An-AI-Based-Real-Time-Passenger-Detection-And-Capacity-Monitoring-System-
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Initialize database**
   ```bash
   python backend/manage.py db upgrade
   ```

4. **Start with Docker Compose**
   ```bash
   docker-compose up -d
   ```

   Or **start components individually**:
   - Backend: `cd backend && python app.py`
   - Dashboard: `cd dashboard && npm install && npm start`
   - Edge: `cd edge && python main.py`

### Running Tests
```bash
pytest tests/ -v
```

## Key Technologies

- **Computer Vision**: YOLOv8/v10 for real-time person detection
- **Backend**: Python (FastAPI/Flask), PostgreSQL
- **Frontend**: React/Vue.js for dashboard, React Native/Flutter for mobile
- **Edge Computing**: TensorRT, ONNX for optimized inference
- **DevOps**: Docker, Kubernetes, GitHub Actions
- **APIs**: RESTful API, WebSocket for real-time updates

## API Endpoints

### Core Endpoints
- `GET /api/vehicles` - List all vehicles
- `GET /api/vehicles/:id/occupancy` - Get vehicle occupancy
- `POST /api/vehicles/:id/alert` - Trigger capacity alert
- `GET /api/analytics/reports` - Generate occupancy reports
- `WebSocket /ws/live/:vehicle_id` - Real-time occupancy stream

## Performance Metrics

- **Detection Accuracy**: >95% in controlled environments
- **Latency**: <200ms per frame (edge processing)
- **FPS**: 20-30 FPS on edge hardware
- **Scalability**: Support for 1000+ vehicles per backend instance

## Configuration

See `.env.example` for all configurable options:
- Model selection (YOLOv8 vs v10)
- Confidence thresholds
- Database connection strings
- API ports and timeouts
- Alert thresholds

## Development

### Contributing
Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Branching Strategy
- `main` - Production-ready code
- `develop` - Development branch
- `feature/*` - Feature branches
- `bugfix/*` - Bug fix branches

## Deployment

See [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) for:
- Cloud deployment (AWS, GCP, Azure)
- On-premises deployment
- Edge device configuration
- Scaling considerations

## Roadmap

- [ ] Multi-camera tracking across zones
- [ ] Anomaly detection (crowding patterns)
- [ ] Advanced analytics dashboard
- [ ] Mobile app push notifications
- [ ] Integration with transit authorities APIs
- [ ] Cost optimization and model quantization

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## Support & Contact

For issues, questions, or contributions:
- Open an issue on GitHub
- Contact: [project maintainer contact]

## Acknowledgments

- YOLOv8/v10 team for detection models
- Transit authority partners for requirements
- Open-source community contributions
