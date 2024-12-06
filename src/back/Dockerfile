# Base image for Python
FROM python:3.9-slim

# Set working directory
WORKDIR /nuit dinfo 2024

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose the Flask port
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
