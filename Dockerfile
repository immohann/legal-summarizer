# Use the official Python base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application code into the container
COPY . /app

# Install the dependencies
RUN pip install -r requirements.txt


# Expose the port that the Flask app will listen on
EXPOSE 5000

# Set the entrypoint command
CMD ["python", "app.py"]
