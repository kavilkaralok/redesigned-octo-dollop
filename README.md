# 📝 Flask Log App

Welcome to **Flask Log App**, a minimalist logging service built with Flask. It exposes a single endpoint to receive and print logs — ideal for quick integrations, prototypes, or development-time debugging.

## 🚀 Overview

This app provides a `/log` endpoint that accepts `POST` requests containing log data in JSON format. It logs the received information to the server console.

## 📫 API Endpoint

### `POST /log`

Accepts JSON payloads for logging purposes.

#### Example Request

```bash
curl -X POST http://localhost:5000/log \
     -H "Content-Type: application/json" \
     -d '{
           "level": "INFO",
           "message": "Something happened!",
           "timestamp": "2025-05-09T12:00:00Z"
         }'
