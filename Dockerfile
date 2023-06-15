# Use an official Python runtime as the base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install "setuptools<58.0.0"
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code into the container
COPY . /code/

# Run database migrations
# RUN python manage.py makemigrations
# RUN python manage.py migrate

# Expose the port that the application will run on
EXPOSE 8000

# Start the application
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]