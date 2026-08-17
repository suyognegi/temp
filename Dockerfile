FROM python:3.11-slim-bookworm

WORKDIR /app

# Install system dependencies for Playwright
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python packages with specific playwright version
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright dependencies and browsers
RUN python -m playwright install-deps && \
    python -m playwright install chromium

# Copy application code
COPY main.py .

# Create non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

# Use workers=1 to avoid memory issues with Playwright
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
