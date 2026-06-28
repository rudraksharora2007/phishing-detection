# AI-Powered Phishing Detection System

Production-style full-stack cybersecurity project with Flask, React, MongoDB, and a Random Forest phishing classifier.

## Features
- JWT auth (register/login), role-based admin access
- Real-time URL phishing prediction + confidence + risk level
- Explainable AI reasons for predictions
- URL scan history + CSV export
- Admin analytics + model retraining endpoint
- VirusTotal submission integration
- Rate limiting, input sanitization, secure password hashing
- Docker-ready deployment

## Architecture
```
backend/
frontend/
extension/
API_DOCUMENTATION.md
DEPLOYMENT.md
docker-compose.yml
```

## Backend Setup
```bash
cd backend
cp .env.example .env
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python ml/train_model.py --dataset ml/dataset/sample_urls.csv --output ml/phishing_model.pkl
python app.py
```

## Frontend Setup
```bash
cd frontend
cp .env.example .env
npm install
npm run dev
```

## Docker Setup
```bash
cp backend/.env.example backend/.env
docker compose up --build
```

## Environment Variables
See `backend/.env.example` and `frontend/.env.example`.

## Sample Dataset Structure
Location: `backend/ml/dataset/sample_urls.csv`

Columns:
- `url_length`
- `subdomain_count`
- `uses_https`
- `has_ip`
- `special_char_count`
- `hyphen_count`
- `digit_count`
- `suspicious_keyword_count`
- `entropy`
- `redirect_count`
- `domain_age_days`
- `label` (0 legitimate, 1 phishing)

## Core APIs
- `POST /api/auth/register`
- `POST /api/auth/login`
- `POST /api/predict`
- `GET /api/history`
- `GET /api/admin/stats`
- `POST /api/admin/retrain`

Detailed reference: `API_DOCUMENTATION.md`

## Security Controls
- Bcrypt password hashing
- JWT signed auth tokens
- Rate limiting via Flask-Limiter
- URL/email validation and sanitization
- Role checks for admin endpoints

## Browser Extension Preparation
Sample manifest available at `extension/manifest.sample.json`.

## Future Enhancements
1. Email phishing classifier pipeline
2. Deep learning ensemble (URL + content features)
3. Threat intelligence feeds + blacklist cache
4. WebSocket alerts for SOC dashboards
