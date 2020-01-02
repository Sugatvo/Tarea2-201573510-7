# Use an official Python runtime as a parent image
FROM python:latest

RUN pip install --upgrade pip && \
    pip install pika

# Set the working directory to /app
WORKDIR /cliente

# Copy the current directory contents into the container at /app
COPY . /cliente

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "cliente.py"]
