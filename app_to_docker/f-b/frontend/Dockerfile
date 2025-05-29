# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the frontend application code into the container
# This includes app.py and the templates/ directory
COPY . /app

# Install Python dependencies
# For this app, we need Flask and requests
RUN pip install --no-cache-dir Flask requests

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
# app.py already has app.run(host='0.0.0.0', port=5000, debug=True)
# The BACKEND_API_URL will be passed as an environment variable by Docker Compose
CMD ["python", "app.py"]
