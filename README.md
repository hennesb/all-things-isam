# Setting up an ISAM development lab
This repo contains the bare minimum needed to start up an ISAM docker webseal instance using a Trial licence.
Once the licence agreements are accepted and applied , the ansible script supplied with this repo configures
a runtime based on an embedded ldap and configures a test junction. The junction at this point is configured with
a machine specific host ( for macOS ). 

## Docker Directory
The docker directory contains the following files
 - **start-isam.sh** , this script runs the docker-compose process that starts the ISAM config and ISAM webseal containers
 - **docker-compose.yaml** , the docker compose file that has the ISAM docker config. This is a cut down version taken from the [IBM ISAM site](https://www.ibm.com/support/knowledgecenter/en/SSPREK_9.0.6/com.ibm.isam.doc/admin/concept/con_docker_compose.html)
 - **.env** , environment specific entries for the docker compose file
 - **clear-down-environment.sh** , stops and removes the ISAM containers and clears down the shared volumes. Please be aware that 
   this will remove any ISAM config you've applied that hasn't been applied using ansible.
