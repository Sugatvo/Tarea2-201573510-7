# Use an official Python runtime as a parent image
FROM python:latest

RUN pip install --upgrade pip && \
    pip install grpcio && \
    pip install protobuf && \
    export bleah=$(hostname -i) && \
    echo $bleah;

# Set the working directory to /app
WORKDIR /cliente

# Copy the current directory contents into the container at /app
COPY . /cliente

# Define environment variable
ENV NAME World2

# Run app.py when the container launches
CMD ["python", "greeter_client.py"]
