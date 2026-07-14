# Count-Me-In Backend Service

## Overview

This is the FastAPI-based backend service for the Count-Me-In passenger detection system. It provides:

- RESTful API endpoints for vehicle and occupancy management
- Real-time data persistence with PostgreSQL
- Caching layer with Redis
- Authentication and authorization
- Alert management and notifications
- Analytics and reporting

## Project Structure

```
backend/
├── app.py                 # Main FastAPI application
├── core/
│   ├── config.py         # Configuration management
│   └── logging_config.py # Logging setup
├── database/
│   ├── db.py             # Database connection and session
│   └── models/           # SQLAlchemy ORM models
├── schemas/              # Pydantic validation schemas
├── api/
│   └── routes/           # API endpoint implementations
├── services/             # Business logic services
├── middleware/           # Custom middleware
├── utils/                # Helper utilities
├── tests/                # Test suite
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Setup Instructions

### Prerequisites

- Python 3.9+
- PostgreSQL 12+ (or use SQLite for development)
- Redis (optional, for caching)

### Installation

1. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment:**
   ```bash
   cp .env.local .env
   # Edit .env with your settings
   ```

4. **Initialize database:**
   ```bash
   # For SQLite (dev)
   python -c "from database.db import init_db; init_db()"
   
   # For PostgreSQL (production)
   # Update DATABASE_URL in .env first
   alembic upgrade head
   ```

### Running the Server

```bash
python app.py
```

Server will be available at `http://localhost:5000`

### API Documentation

- **Swagger UI**: `http://localhost:5000/docs`
- **ReDoc**: `http://localhost:5000/redoc`

## Key Components

### Models

- **User**: Authentication and authorization
- **Vehicle**: Vehicle information and configuration
- **OccupancyReading**: Person count data from edge devices
- **Alert**: System alerts and notifications

### API Routes

#### Authentication (`/api/auth`)
- `POST /login` - User login
- `POST /register` - User registration
- `POST /logout` - User logout
- `POST /refresh` - Token refresh

#### Vehicles (`/api/vehicles`)
- `GET /` - List vehicles
- `POST /` - Create vehicle
- `GET /{id}` - Get vehicle details
- `PUT /{id}` - Update vehicle
- `DELETE /{id}` - Delete vehicle

#### Occupancy (`/api/occupancy`)
- `POST /readings` - Submit occupancy reading
- `GET /vehicles/{id}/current` - Get current occupancy
- `GET /vehicles/{id}/history` - Get occupancy history

#### Alerts (`/api/alerts`)
- `GET /` - List alerts
- `POST /` - Create alert
- `GET /{id}` - Get alert details
- `PUT /{id}/acknowledge` - Acknowledge alert

#### Analytics (`/api/analytics`)
- `GET /occupancy-report` - Generate occupancy report
- `GET /peak-hours` - Get peak occupancy hours
- `GET /vehicle-stats` - Get vehicle statistics
- `GET /fleet-overview` - Get fleet overview

## Testing

### Run all tests
```bash
pytest tests/ -v
```

### Run with coverage
```bash
pytest tests/ --cov=. --cov-report=html
```

### Run specific test
```bash
pytest tests/test_health.py -v
```

## Configuration

See `.env.local` for available configuration options:

- Database connection strings
- Redis configuration
- JWT settings
- Model parameters
- Alert thresholds
- Logging levels

## Development Notes

### TODO Items

The following endpoints are marked with TODO and need implementation:

1. **Authentication Service**
   - User login/registration
   - Password hashing and verification
   - JWT token generation
   - Token refresh logic

2. **Vehicle Management**
   - CRUD operations with database
   - Vehicle filtering and search
   - Device registration and heartbeat

3. **Occupancy Service**
   - Occupancy reading storage and retrieval
   - Historical data aggregation
   - Real-time updates via WebSocket

4. **Alert System**
   - Alert creation and management
   - Alert acknowledgment workflow
   - Webhook and email notifications

5. **Analytics**
   - Report generation
   - Peak hours analysis
   - Vehicle statistics
   - Fleet-wide metrics

### Adding New Endpoints

1. Create schema in `schemas/`
2. Create route in `api/routes/`
3. Implement business logic in `services/`
4. Add database queries in models
5. Add tests in `tests/`

## Dependencies

### Core
- **FastAPI**: Web framework
- **SQLAlchemy**: ORM
- **Pydantic**: Data validation

### Database
- **PostgreSQL**: Production database
- **SQLite**: Development database
- **Alembic**: Database migrations

### Caching & Real-time
- **Redis**: Caching and pub/sub
- **python-socketio**: WebSocket support

### Security
- **PyJWT**: JWT token handling
- **passlib**: Password hashing
- **python-jose**: JOSE token support

### Testing
- **pytest**: Testing framework
- **httpx**: HTTP testing
- **faker**: Test data generation

## Troubleshooting

### Import Errors

Ensure virtual environment is activated and dependencies are installed:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Database Connection Error

Verify DATABASE_URL in .env and ensure PostgreSQL is running.

### Port Already in Use

Change API_PORT in .env or kill the process:
```bash
lsof -i :5000
kill -9 <PID>
```

## Next Steps

1. Implement authentication service with JWT
2. Add database operations for CRUD endpoints
3. Implement occupancy reading submission and retrieval
4. Add alert generation logic
5. Implement analytics and reporting
6. Add WebSocket support for real-time updates
7. Set up database migrations with Alembic
8. Implement comprehensive test coverage

## Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
