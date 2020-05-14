
#!/bin/bash

read -p 'This script REMOVES your docker webseal config. Confirm you want to proceed (Y/N) ' confirm_remove


if [ -z "$confirm_remove" ]; then
   echo "You have not entered a value. Please confirm with a Y or N character"
   exit -1
fi

# This is compatible with bash and zsh
input=`echo $confirm_remove | tr "[:lower:]" "[:upper:]" `

if [ $input == 'Y' ]; then
   docker stop $(docker ps --filter "name=docker_isam-webseal_1" --filter "name=docker_isam-config_1" -aq )
   docker rm $(docker ps --filter "name=docker_isam-webseal_1" --filter "name=docker_isam-config_1" -aq)
   if [ $? -eq 0 ]; then
      echo "Removing the following files"
      echo `ls /tmp/isam-dev-lab`
      rm -rf /tmp/isam-dev-lab
   fi

else
   echo "Script has been aborted due to input value $input"
fi

