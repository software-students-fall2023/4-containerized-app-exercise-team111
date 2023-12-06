# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
# This assumes that the Dockerfile is located at the root of your project and the requirements.txt is in the web-app folder.
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose the port your application runs on
EXPOSE 8001

# Environment variables for MongoDB
ENV MONGO_HOST=mongodb
ENV MONGO_PORT=27017
ENV MONGO_URI=mongodb://mongodb:27017
ENV MONGO_DBNAME=object_recognition_db
ENV ML_CLIENT_URL=http://machine-learning-client:5003
# Command to run your application
CMD ["python", "app.py"]
