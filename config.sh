#!/bin/bash

# Get flags as inputs
while getopts u:p:d:t: flag
do
    case "${flag}" in
       u) user=${OPTARG};;
       p) password=${OPTARG};;
       d) database=${OPTARG};;
       t) table=${OPTARG};;
    esac
done

# Create the config file if does not exist
# otherwise, delete the file and re-create it using user's permission
file=dbms/dbnn_config.ini

if [ ! -e "$file" ]
then
   touch "$file"
else
   rm -i -v "$file"
   touch "$file"
fi

# Open the file and write the settings
sudo tee -a "$file" > /dev/null  <<EOT
[starting_point]
host=db
database=template1
user=$user
password=$password

[ending_point]
host=db
database=$database
user=$user
password=$password

[postgresql]
name_of_db=$database
name_of_table=$table
rootdir=/app/imgs/originals
savedir=/app/imgs/rendered
EOT

# Create secret files for user and password
# otherwise, delete them and re-create them using user's permission
postgres_user=POSTGRES_USER.txt
postgres_password=POSTGRES_PASSWORD.txt

if [ ! -e "$postgres_user" ] || [ ! -e "$postgres_password" ]
then
   touch "$postgres_user" "$postgres_password"
   echo $user >> "$postgres_user"
   echo $password >> "$postgres_password"
else
   rm -i -v "$postgres_user" "$postgres_password"
   touch "$postgres_user" "$postgres_password"
   echo $user >> "$postgres_user"
   echo $password >> "$postgres_password"
fi