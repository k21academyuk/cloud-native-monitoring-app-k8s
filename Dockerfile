# Use the official Python 3.9 image based on Debian Buster as the base image.
FROM python:3.9-buster

# Set the working directory inside the container to /app.
WORKDIR /app

# Copy the requirements.txt file from the host machine to the /app directory inside the container.
COPY requirements.txt .

# Run pip3 inside the container to install the Python packages listed in requirements.txt.
# --no-cache-dir flag is used to avoid caching the downloaded package files, reducing image size.
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the current directory (the entire application code) from the host machine to /app inside the container.
COPY . .

# Set an environment variable to configure the Flask application to listen on all available network interfaces.
ENV FLASK_RUN_HOST=0.0.0.0

# Expose port 5000 in the container, allowing it to accept incoming network connections on that port.
EXPOSE 5000

# Define the default command to run when the container starts.
# In this case, it starts the Flask application using the "flask run" command.
CMD ["flask", "run"]
