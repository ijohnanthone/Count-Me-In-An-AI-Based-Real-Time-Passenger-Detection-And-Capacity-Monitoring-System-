# Count-Me-In API Documentation

## Base URL

```
https://api.yourdomain.com/api
```

## Authentication

All endpoints require JWT token in Authorization header:

```
Authorization: Bearer <your_jwt_token>
```

## Endpoints

### Authentication

#### Login

```http
POST /auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "password123"
}

Response:
{
  "token": "eyJhbGciOiJIUzI1NiIs...",
  "user": {
    "id": "usr_123",
    "email": "user@example.com",
    "role": "ADMIN"
  }
}
```

### Vehicles

#### List Vehicles

```http
GET /vehicles?limit=10&offset=0

Response:
{
  "vehicles": [
    {
      "id": "v_001",
      "registration_number": "ABC123",
      "capacity": 100,
      "current_occupancy": 45,
      "status": "OPERATIONAL",
      "location": {"lat": 40.7128, "lon": -74.0060},
      "route_id": "r_001"
    }
  ],
  "total": 150,
  "limit": 10,
  "offset": 0
}
```

#### Get Vehicle Details

```http
GET /vehicles/:id

Response:
{
  "id": "v_001",
  "registration_number": "ABC123",
  "capacity": 100,
  "current_occupancy": 45,
  "status": "OPERATIONAL",
  "location": {"lat": 40.7128, "lon": -74.0060},
  "route_id": "r_001",
  "last_update": "2024-01-15T10:30:00Z",
  "occupancy_percentage": 45,
  "avg_occupancy_today": 52.3
}
```

#### Create Vehicle

```http
POST /vehicles
Content-Type: application/json

{
  "registration_number": "ABC123",
  "capacity": 100,
  "route_id": "r_001"
}

Response: 201 Created
{
  "id": "v_001",
  "registration_number": "ABC123",
  "capacity": 100,
  "created_at": "2024-01-15T10:00:00Z"
}
```

### Occupancy

#### Get Current Occupancy

```http
GET /vehicles/:id/occupancy

Response:
{
  "vehicle_id": "v_001",
  "person_count": 45,
  "occupancy_percentage": 45,
  "timestamp": "2024-01-15T10:30:00Z",
  "confidence": 0.92
}
```

#### Submit Occupancy Reading

```http
POST /occupancy/readings
Content-Type: application/json

{
  "vehicle_id": "v_001",
  "person_count": 45,
  "confidence": 0.92,
  "timestamp": "2024-01-15T10:30:00Z"
}

Response: 201 Created
{
  "id": "ocr_123",
  "vehicle_id": "v_001",
  "person_count": 45,
  "recorded_at": "2024-01-15T10:30:00Z"
}
```

#### Get Occupancy History

```http
GET /vehicles/:id/occupancy/history?start_time=2024-01-15T00:00:00Z&end_time=2024-01-15T23:59:59Z&interval=5m

Response:
{
  "vehicle_id": "v_001",
  "readings": [
    {"timestamp": "2024-01-15T10:00:00Z", "person_count": 30},
    {"timestamp": "2024-01-15T10:05:00Z", "person_count": 35},
    {"timestamp": "2024-01-15T10:10:00Z", "person_count": 45}
  ]
}
```

### Alerts

#### List Alerts

```http
GET /alerts?status=ACTIVE&limit=20

Response:
{
  "alerts": [
    {
      "id": "a_001",
      "vehicle_id": "v_001",
      "type": "CAPACITY_HIGH",
      "occupancy_percentage": 87,
      "created_at": "2024-01-15T10:30:00Z",
      "acknowledged_at": null,
      "severity": "HIGH"
    }
  ],
  "total": 5
}
```

#### Get Alert Details

```http
GET /alerts/:id

Response:
{
  "id": "a_001",
  "vehicle_id": "v_001",
  "type": "CAPACITY_HIGH",
  "occupancy_percentage": 87,
  "created_at": "2024-01-15T10:30:00Z",
  "acknowledged_at": null,
  "acknowledged_by": null,
  "severity": "HIGH"
}
```

#### Acknowledge Alert

```http
PUT /alerts/:id/acknowledge

Response: 200 OK
{
  "id": "a_001",
  "acknowledged_at": "2024-01-15T10:32:00Z",
  "acknowledged_by": "usr_123"
}
```

### Analytics

#### Get Occupancy Report

```http
GET /analytics/occupancy-report?start_date=2024-01-01&end_date=2024-01-31

Response:
{
  "period": "2024-01-01 to 2024-01-31",
  "total_readings": 8640,
  "average_occupancy": 62.5,
  "peak_occupancy": 98,
  "vehicles": [
    {
      "vehicle_id": "v_001",
      "avg_occupancy": 65.2,
      "peak_occupancy": 98,
      "total_alerts": 12
    }
  ]
}
```

#### Get Peak Hours

```http
GET /analytics/peak-hours?vehicle_id=v_001

Response:
{
  "vehicle_id": "v_001",
  "peak_hours": [
    {"hour": 8, "avg_occupancy": 85},
    {"hour": 9, "avg_occupancy": 88},
    {"hour": 17, "avg_occupancy": 82},
    {"hour": 18, "avg_occupancy": 80}
  ]
}
```

## WebSocket Endpoints

### Real-Time Occupancy Stream

```
WS /ws/live/:vehicle_id
```

**Message Format:**

```json
{
  "type": "occupancy_update",
  "vehicle_id": "v_001",
  "person_count": 45,
  "occupancy_percentage": 45,
  "timestamp": "2024-01-15T10:30:00Z",
  "confidence": 0.92
}
```

**Alert Message:**

```json
{
  "type": "alert",
  "alert_id": "a_001",
  "vehicle_id": "v_001",
  "alert_type": "CAPACITY_HIGH",
  "occupancy_percentage": 87,
  "severity": "HIGH"
}
```

## Error Responses

### 400 Bad Request

```json
{
  "error": "Invalid input",
  "details": "occupancy_percentage must be between 0 and 100"
}
```

### 401 Unauthorized

```json
{
  "error": "Authentication required",
  "message": "Missing or invalid JWT token"
}
```

### 403 Forbidden

```json
{
  "error": "Permission denied",
  "message": "User does not have permission to access this resource"
}
```

### 404 Not Found

```json
{
  "error": "Not found",
  "message": "Vehicle with ID v_999 not found"
}
```

### 500 Internal Server Error

```json
{
  "error": "Internal server error",
  "message": "An unexpected error occurred"
}
```

## Rate Limiting

- Standard: 1000 requests/hour
- Burst: 100 requests/minute
- WebSocket: Unlimited

## Pagination

List endpoints support pagination:

```
GET /vehicles?limit=10&offset=20

Parameters:
- limit: Number of items (default: 30, max: 100)
- offset: Starting position (default: 0)
```

## Filtering

Many endpoints support filtering:

```
GET /alerts?status=ACTIVE&severity=HIGH&vehicle_id=v_001
```

## Sorting

List endpoints support sorting:

```
GET /vehicles?sort_by=occupancy_percentage&sort_order=desc
```
