FROM python:3.11-slim-bookworm

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    TZ=Asia/Amman \
    PIP_NO_CACHE_DIR=1

# Copy project files
COPY pyproject.toml uv.lock* ./
COPY bot ./bot
COPY main.py .

# Install Python dependencies
RUN pip install --upgrade pip setuptools wheel && \
    pip install -e .

# Create logs directory
RUN mkdir -p logs

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import sys; sys.exit(0)" || exit 1

# Run the application using aiogram (main.py only)
ENTRYPOINT ["python", "-u", "main.py"]
