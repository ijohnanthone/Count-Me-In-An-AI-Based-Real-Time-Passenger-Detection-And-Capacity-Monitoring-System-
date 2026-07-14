# Setup Instructions

## Prerequisites

- Python 3.9+
- Node.js 16+
- PostgreSQL 12+
- Docker & Docker Compose
- Git

## Development Environment Setup

### 1. Clone Repository

```bash
git clone https://github.com/ijohnanthone/Count-Me-In-An-AI-Based-Real-Time-Passenger-Detection-And-Capacity-Monitoring-System-.git
cd Count-Me-In-An-AI-Based-Real-Time-Passenger-Detection-And-Capacity-Monitoring-System-
```

### 2. Environment Configuration

```bash
cp .env.example .env
# Edit .env with your local settings
```

### 3. Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Initialize database
alembic upgrade head

# Run server
python app.py
```

Backend will be available at `http://localhost:5000`

### 4. Dashboard Setup

```bash
cd dashboard
npm install
npm start
```

Dashboard will be available at `http://localhost:3000`

### 5. Edge Service Setup

```bash
cd edge
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Configure camera source in config.py
python main.py
```

## Docker Setup

```bash
docker-compose up -d
```

This starts all services:
- Backend: http://localhost:5000
- Dashboard: http://localhost:3000
- PostgreSQL: localhost:5432
- Redis: localhost:6379

## Database Setup

### Local PostgreSQL

```bash
# Create database
psql -U postgres
CREATE DATABASE count_me_in;
\c count_me_in
```

### Run Migrations

```bash
cd backend
alembic upgrade head
```

## Testing

```bash
# Run all tests
pytest tests/ -v

# With coverage
pytest tests/ --cov=backend --cov-report=html

# Specific test file
pytest tests/unit/test_detector.py -v
```

## Troubleshooting

### Port Already in Use

```bash
# Find and kill process on port
lsof -i :5000
kill -9 <PID>
```

### Database Connection Error

- Verify PostgreSQL is running
- Check DATABASE_URL in .env
- Ensure database exists

### Model Download Issues

```bash
# Manually download YOLOv8
python -c "from ultralytics import YOLO; YOLO('yolov8n.pt')"
```

## Next Steps

- Read [ARCHITECTURE.md](ARCHITECTURE.md)
- Check [API.md](API.md) for endpoint documentation
- Review [CONTRIBUTING.md](../CONTRIBUTING.md)
