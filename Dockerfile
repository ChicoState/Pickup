# Start from a Python base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /code

# Copy the entire local directory into the container's /code directory
COPY . /code/

# Install vim and dependencies
RUN apt-get update && apt-get install -y vim

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose the port the app will run on
EXPOSE 8000

# Set the command to run the Django app
CMD ["python", "/code/mysite/manage.py", "runserver", "0.0.0.0:8000"]