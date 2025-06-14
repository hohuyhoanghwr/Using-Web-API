# Use an official Python runtime as a parent image
FROM python:3.12-slim-bookworm

# Set working directory
WORKDIR /app

# Copy files
COPY iss-tracker-app/requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY iss-tracker-app/ /app

# Expose Streamlit's default port
EXPOSE 8502

# Start the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8502", "--server.address=0.0.0.0","--server.runOnSave=true"]
