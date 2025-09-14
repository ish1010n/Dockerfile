# syntax=docker/dockerfile:1
FROM python:3.10-alpine 

# Set the working directory inside the container
WORKDIR /code 

# Set environment variables for Flask
ENV FLASK_APP=app.py 
ENV FLASK_RUN_HOST=0.0.0.0 

# Install system dependencies
RUN apk add --no-cache gcc musl-dev linux-headers 

# Copy requirements.txt and install Python dependencies
COPY requirements.txt requirements.txt 
RUN pip install -r requirements.txt 

# Expose the port where the application listens
EXPOSE 5000 

# Copy the rest of the application code
COPY . . 

# Set the default command to run the application
CMD ["flask", "run", "--debug"] 
