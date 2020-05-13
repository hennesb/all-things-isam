# Setting up an ISAM development lab
This repo contains the bare minimum needed to start up an ISAM docker webseal instance using a Trial licence.
Once the licence agreements are accepted and applied , the ansible script supplied with this repo configures
a runtime based on an embedded ldap, a default webseal instance and configures a test junction. 
The junction at this point is configured with a docker platform specific host.

## Docker Directory
The docker directory contains the following files
 - **start-isam.sh** , this script runs the docker-compose process that starts the ISAM config and ISAM webseal containers
 - **docker-compose.yaml** , the docker compose file that has the ISAM docker config. This is a cut down version taken from the [IBM ISAM site](https://www.ibm.com/support/knowledgecenter/en/SSPREK_9.0.6/com.ibm.isam.doc/admin/concept/con_docker_compose.html) and has an updated version of 9.0.7.1_IF4. 
 - **.env** , environment specific entries for the docker compose file
 - **clear-down-environment.sh** , stops and removes the ISAM containers and clears down the shared volumes. Please be aware that 
   this will remove any ISAM config you've applied not performed through the ansible playbook.

## Getting Started
1. Navigate to the docker directory and run `./start-isam.sh`
2. This should start the ISAM configuration appliance
  ![alt text](https://github.com/hennesb/all-things-isam/issues/1#issue-617686427 "ISAM login Page")

