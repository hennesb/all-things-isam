# Setting up an IBM Security Access Manager development lab
This repository contains instructions to standup an IBM security access manager webseal docker instance.
Trial licence acceptance is performed manually through the LMI but the runtime and reverse proxy configurations are performed using 
the IBM Security Access Manager ansible roles. Outcomes I hope to achieve with this repo are

- a development environment where webseal acts a reverse proxy to your application
- use the ISAM REST APIs against your own dedicated environment
- demonstrate ansible working with IBM 
- connect to the OpenLDAP registry using Apache Directory Studio


<aside class="warning">
I use a default passwords in this demo lab and LDAP is running on a plaintext port of 389. All passwords are admin. Usual warnings , please change these for your environment. 

</aside>




## Before you start
- Ensure docker , docker compose and ansible are installed on the host machine.
- Install the IBM security Python packages `pip install ibmsecurity` . 
- If you're using the vagrant image all the pre-requisite software will be installed on the `vagrant up` command



<aside class="notice">
This video instructions below are for MacOS, the vagrant instructions (Linux) are coming soon.

</aside>

## Docker Directory
The docker directory contains the following files
 - **start-isam.sh** , this script runs the docker-compose process that starts the ISAM config and ISAM webseal containers
 - **docker-compose.yaml** , the docker compose file that has the ISAM docker config. This is a cut down version taken from the [IBM site](https://www.ibm.com/support/knowledgecenter/en/SSPREK_9.0.6/com.ibm.isam.doc/admin/concept/con_docker_compose.html) and has an updated version of 9.0.7.1_IF4. 
 - **.env** , environment specific entries for the docker compose file
 - **clear-down-environment.sh** , stops and removes the ISAM containers and clears down the shared volumes. Please be aware that 
   this will remove any ISAM config you've applied.


## Ansible directory
- ***apply-config.sh*** This shell installs the ISAM ansible roles, runs the ansible playbook to configure the appliance and waits for the webseal container to receive the config published from the LMI. 
- ***accept_agreement.json*** JSON for accepting the licence agreement. Not really needed for this as the Trial version requires some
manual configuration but might be useful for non Trial versions of the product.
- ***runtime-config.json*** The configuration needed to use the embedded ldap for the runtime config.

## Getting Started MacOS
1. Security Access Manager protects applications , I've used this as sample [application](https://github.com/spring-guides/gs-spring-boot/tree/master/complete) to sit behind the reverse proxy. This runs on my host machine , not a docker container , on port 8080.

[![Step 1](https://res.cloudinary.com/dnrfrgcar/image/upload/v1589628519/SAM-thumbnail_ptkpgo.png )](http://www.youtube.com/watch?v=chhJCSivNnM "Step 1")

2. Start the ISAM containers . Clone this repo , navigate to the docker directory and run `./start-isam.sh`

[![Step 2](https://res.cloudinary.com/dnrfrgcar/image/upload/v1589635988/Screenshot_2020-05-16_at_14.32.33_ovfczk.png)](https://youtu.be/gIDX8AkmT_A "Step 2")



3. This should start the ISAM configuration appliance [login page ](https://localhost:9443/core/login). The default username is ***admin*** and password is ***admin***. It also starts a webseal container but that remains in an unhealthy state until the configuration container publishes the reverse proxy config to the shared volumes. You'll need to download a Trial licence from IBM and activate it within the appliance. IBM have a good [YouTube video](https://youtu.be/2gmlr8sjkkE) on this but the video below shows the steps needed once you have the licence certificate.
[![Step 3](/images/isam-login.png )](https://youtu.be/DDjX1yKlc7I "Step 3")


4. Once you've completed the initial setup , navigate to the ansible directory. Run the `./apply-config.sh` 
   Using the ISAM ansible roles this step
    - configures a runtime environment with the openldap registry
    - configures a reverse proxy called default
    - adds a junction to our application started in Step 1

[![Step 4](https://res.cloudinary.com/dnrfrgcar/image/upload/v1589637467/Screenshot_2020-05-16_at_14.57.18_hv94bz.png)](https://youtu.be/kne8zdncOsw "Step 4")


5. Navigate to https://localhost/isam-test , you should receive the ISAM reverse proxy default login page,  use the sec_master user and credentials to login to the Spring boot appliation.

[![Step 5](https://res.cloudinary.com/dnrfrgcar/image/upload/v1589639237/Screenshot_2020-05-16_at_15.26.56_eezbvw.png)](https://youtu.be/3xUtH6UcyIA "Step 5")



## Getting Started with IBM Security Access Manager with Linux running in Vagrant
1. Download the repo and navigate to the vagrant directory. 
2. Issue `vagrant up` . This will provision an Ubuntu18 OS , install docker , docker-compose, ansible and the ibmsecurity python dependencies.
3. When the vagrant vm is provisioned issue a `vagrant ssh`
4. In the home directory /home/vagrant you should find the repo in the ***all-things-isam*** directory
5. `cd /home/vagrant/all-things-isam/docker` and then issue `sudo ./start-isam.sh` . This will start the isam and ldap containers.
6. Install the Trial licence by following the same steps from the MacOS instructions. Youtube video is below.
   [![Step 3](/images/isam-login.png )](https://youtu.be/DDjX1yKlc7I "Step 3")
7. Within the vagrant vm , `cd /home/vagrant/all-things-isam/ansible` from here issue `sudo ./apply-config.sh`
8. Navigate to https://localhost/isam-test , you should receive the ISAM reverse proxy default login page,  use the sec_master user and credentials to login to  the Spring boot appliation.

### This may run on Windows10 but I have not tested it yet.


 

