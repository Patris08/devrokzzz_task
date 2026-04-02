# Use official Python 3.11 image as base
FROM python:3.11

# Set working directory inside the container
WORKDIR /app

# Copy application file into the container
COPY app.py .

# Install Flask without caching to reduce image size
RUN pip install --no-cache-dir flask

# Run the application
CMD ["python", "app.py"]