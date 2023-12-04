# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory to /app
WORKDIR /app

# Install OpenCV dependencies

RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libfontconfig1


# Copy the requirements file from the machine-learning-client directory
# This assumes that the Dockerfile is located at the root of your project and the requirements.txt is in the machine-learning-client folder.
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
# Using --no-cache-dir option with pip to keep the docker image size small
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of the machine-learning-client into /app
COPY . .

# Expose the port your application runs on
EXPOSE 5003

# Environment variables for MongoDB
ENV MONGO_HOST=mongodb
ENV MONGO_PORT=27017
ENV MONGO_URI=mongodb://mongodb:27017
ENV MONGO_DBNAME=object_recognition_db

# Command to run your application
# Make sure app.py is the correct filename and it's located in the root of machine-learning-client
CMD ["python", "app.py"]
