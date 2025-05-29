# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the backend application code into the container
COPY app.py .
# Note: users.json will be created by the app if it doesn't exist,
# or managed by a volume in docker-compose.

# Install Python dependencies
# For this app, we need Flask, Flask-CORS, and Werkzeug (for hashing)
RUN pip install --no-cache-dir Flask Flask-CORS Werkzeug

# Expose the port the app runs on
EXPOSE 5001

# Command to run the application
# app.py already has app.run(host='0.0.0.0', port=5001, debug=True)
CMD ["python", "app.py"]
