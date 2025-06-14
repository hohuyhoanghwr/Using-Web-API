# Use an official Python runtime as a parent image
FROM python:3.12-slim-bookworm

# Set working directory
WORKDIR /iss-tracker-app

# Set environment variables

# Copy files
COPY iss-tracker-app/requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY iss-tracker-app/ /iss-tracker-app

# Expose Streamlit's default port
EXPOSE 8501

# Start the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
