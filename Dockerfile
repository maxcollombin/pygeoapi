# Use the geopython/pygeoapi:latest as the base image
FROM geopython/pygeoapi:latest

# Copy the modified requirements-docker.txt file into the container
COPY requirements-docker.txt /requirements-docker.txt

# Install the required packages (including gdal)
RUN pip install -r /requirements-docker.txt
