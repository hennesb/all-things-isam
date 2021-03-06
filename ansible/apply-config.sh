#!/bin/bash
#
# TODO , need a break statement in the until loops
#

echo "Installing ansible roles to tmp"
ansible-galaxy install --roles-path /tmp git+https://github.com/IBM-Security/isam-ansible-roles.git

export ANSIBLE_ROLES_PATH="/tmp/isam-ansible-roles"

ansible-playbook configure-appliance.yml


if [ $? -ne 0 ]; then
   echo "Ansible script failed to run."
   exit -1
fi

until docker container logs docker_isam-webseal_1 | grep "Snapshot has become available"
do
    echo "Waiting for the webseal container to see reverse proxy config data written to shared volume ..." 
    sleep 2
done
echo "SUCCESS : Reverse proxy and sample junction created"

