# Step 1: Use a lightweight, official Python image
FROM python:3.11-slim AS builder

# Step 2: Prevent Python from writing .pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Step 3: Set up the working directory inside the container
WORKDIR /app

# Step 4: Install system dependencies needed for compiling certain Python packages (e.g., psycopg2)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Step 5: Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Step 6: Copy the rest of your Django application code
COPY . /app/

# Step 7: Security Best Practice - Create a non-root user to run the app
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Step 8: Expose the port Gunicorn will run on
EXPOSE 8000

# Step 9: Run database migrations and start Gunicorn (Replace 'myproject' with your actual project config folder name)
CMD ["sh", "-c", "python manage.py migrate --noinput && gunicorn myproject.wsgi:0.0.0.0:8000"]
