# Use official Python slim image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy all files into the container
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV FLASK_RUN_PORT=5000

# Expose port 5000 to outside world
EXPOSE 5000

# Run with Gunicorn (2 workers)
CMD ["gunicorn", "--workers=2", "--bind=0.0.0.0:5000", "app:app"]
