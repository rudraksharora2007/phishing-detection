# API Documentation

Base URL: `http://localhost:5000/api`

## Auth

### POST `/auth/register`
Request:
```json
{ "email": "user@example.com", "password": "strongPass123" }
```

### POST `/auth/login`
Request:
```json
{ "email": "user@example.com", "password": "strongPass123" }
```

## Prediction

### POST `/predict` (JWT required)
Request:
```json
{ "url": "https://example.com" }
```
Response includes `prediction`, `confidence`, `risk_level`, `explanation`, `features`.

### GET `/history` (JWT required)
Returns user scan history.

### GET `/history/export` (JWT required)
Downloads CSV report.

## Admin

### GET `/admin/stats` (Admin JWT)
System analytics.

### POST `/admin/retrain` (Admin JWT)
Retrains model from dataset.

## Health

### GET `/health`
Returns service status.
