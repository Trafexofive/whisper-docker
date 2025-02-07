
# Use an official Python image as a base
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements.txt file into the working directory
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the working directory
COPY . .

# Expose the port for the web UI
EXPOSE 80

# Run the command to start the service when the container launches
ENTRYPOINT [ "python ./app.py" ]
