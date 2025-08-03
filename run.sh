#!/bin/bash

# Set image and container name
IMAGE_NAME=appt-rem-be
CONTAINER_NAME=appt-rem-be

echo $CONTAINER_NAME

# Create logs dir if not exists
mkdir -p ./logs

# Stop and remove the container only if it exists
if docker ps -a --format '{{.Names}}' | grep -Eq "^$CONTAINER_NAME\$"; then
  echo "Removing existing container $CONTAINER_NAME..."
  docker stop $CONTAINER_NAME
  docker rm $CONTAINER_NAME
fi

# build the image
echo "Building Docker image $IMAGE_NAME..."
docker build -t $IMAGE_NAME .


# Run the container 
# NOTE: 
# If necessary, change:
#   1. timezone
#   2. data directory
#   3. log directory
echo "Running the container $CONTAINER_NAME..."
docker run -d \
-p 5000:5000 \
--name $CONTAINER_NAME \
-v "$PWD/logs":/logs \
-v "$PWD/flaskr/data":/app/instance \
-e TZ=America/New_York \
$IMAGE_NAME


# TODO: add volume for data like logs
# -e TZ=America/New_York \


# tail the logs to see live logs in the console window
echo "✅ Container $CONTAINER_NAME is running."

docker exec -it $CONTAINER_NAME sh
# tail -f ./logs/app.log