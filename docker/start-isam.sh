#!/bin/bash
#
# Kick off the docker compose file and wait for the ISAM Config appliance to start
# The compose file has 2 containers , the WebSEAL one only becomes healthy when it receives
# the config published from the ISAM containers and a reverse proxy, named default, is configured 
#
echo "Starting the ISAM config and webseal containers"
docker-compose -f docker-compose.yaml up -d

until docker ps --filter name=docker_isam-config_1 | grep healthy 
do
    
    echo "Waiting for the isam configuration container to start with a status of healthy." 
    sleep 20
    
done

echo `docker ps --filter name=docker_isam-config_1`