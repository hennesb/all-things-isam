# Setting up an ISAM development lab
This repository contains instructions to standup an IBM security access manager webseal docker instance.
Trial licence acceptance manually through the LMI but the runtime and reverse proxy configuration is performed using 
the IBM ISAM ansible roles.


## Docker Directory
The docker directory contains the following files
 - **start-isam.sh** , this script runs the docker-compose process that starts the ISAM config and ISAM webseal containers
 - **docker-compose.yaml** , the docker compose file that has the ISAM docker config. This is a cut down version taken from the [IBM ISAM site](https://www.ibm.com/support/knowledgecenter/en/SSPREK_9.0.6/com.ibm.isam.doc/admin/concept/con_docker_compose.html) and has an updated version of 9.0.7.1_IF4. 
 - **.env** , environment specific entries for the docker compose file
 - **clear-down-environment.sh** , stops and removes the ISAM containers and clears down the shared volumes. Please be aware that 
   this will remove any ISAM config you've applied not performed through the ansible playbook.


## Ansible directory
- ***apply-config.sh*** This shell runs the ansible playbook to configure the appliance and co-ordinates container restarts. It depends on the IBM [isam ansible roles](https://github.com/IBM-Security/isam-ansible-roles) and downloads and places the roles in a /tmp directory. 
- ***accept_agreement.json*** JSON for accepting the licence agreement. Not really needed for this as the Trial version requires some
manual configuration but might be useful for non Trial versions of the product.
- ***runtime-config.json*** The configuration needed to use the embedded ldap for the runtime config.

## Getting Started
1. Security Access Manager protects applications , I've used this as sample [application](https://github.com/spring-guides/gs-spring-boot/tree/master/complete) to sit behind the reverse proxy. This runs on localhost on my host machine not a docker container on port 8080.

[![](http://img.youtube.com/vi/chhJCSivNnM/0.jpg)](http://www.youtube.com/watch?v=chhJCSivNnM "Part 1")

2. Start the ISAM containers . Navigate to the docker directory and run `./start-isam.sh`
3. This should start the ISAM configuration appliance [login page ](https://localhost:9443/core/login). The default username is ***admin*** and password is ***admin***. It also starts a webseal container but that remains in an unhealthy state until the configuration container publishes the reverse proxy config to the shared volumes. 
![ISAM Login Page](/images/isam-login.png )
4. You'll need to download a Trial licence from IBM and activate it within the appliance.
   IBM have a good [YouTube video](https://youtu.be/2gmlr8sjkkE) on this.
5. Once you've completed the initial setup , navigate to the ansible directory. Run the `./apply-config.sh` , it will configure a runtime    environment using an embedded ldap, create a default reverse proxy , create a test junction connecting to the host:8080 and publish the config . Once the webseal container receives that config the script restarts the ISAM configuration container.
6. Navigate to https://localhost/isam-test , you should receive the ISAM login page,  use the sec_master user and credentials to login and it should take you to the Spring boot 

 

