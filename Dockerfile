# Use the official Python image from Docker Hub
FROM python:3.12.4-slim

# Set the working directory inside the container
WORKDIR /mlapp

# Copy the contents of the local requirements.txt to the working directory
COPY ./requirements.txt /mlapp/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the Regression Directory
COPY ./Regression /mlapp/Regression

# Expose port 8000 to the outside world
EXPOSE 8000

# Command to run the FastAPI application using Uvicorn server
CMD [ "uvicorn", "Regression.app:app" , "--host", "0.0.0.0", "--port", "8000"]
