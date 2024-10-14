# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Set working directory inside the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install dependencies
RUN pip install --no-cache-dir locust

# Expose the Locust web UI port
EXPOSE 8089

# Define the default command to run Locust
CMD ["locust"]
