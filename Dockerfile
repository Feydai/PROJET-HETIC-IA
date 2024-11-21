FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Create a virtual environment in the /app directory
RUN python3 -m venv /app/env

# Copy the current directory contents into the container at /app
COPY . .

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/app

# Activate the virtual environment and start a shell
CMD ["/bin/bash", "-c", "source /app/env/bin/activate && exec /bin/bash"]