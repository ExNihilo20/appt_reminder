# Use the official Python 3.12 slim base image
FROM python:3.12-slim

# Set the working directory inside the container 
WORKDIR /app

# Copy the config file
COPY ./appt_reminder.config ./

# Copy and install the dependencies
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Expose the port (optional _ for clarity/documentation)
EXPOSE 5000

# Set Environment variables
ENV FLASK_APP=flaskr
ENV FLASK_ENV=development

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]