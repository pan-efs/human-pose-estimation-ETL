#!/bin/bash

while getopts b:u: flag
do
    case "${flag}" in
       b) build=${OPTARG};;
       u) up=${OPTARG};;
    esac
done

echo "Build: ${build}, Up: ${up}"

if [ "$build" = yes ]
then
   docker-compose build
   echo "Docker-compose build is finished."
elif [ "$build" = no ]
then
   echo "Docker-compose has not built."
else
   echo "Warning '${build}': Accepatable inputs are only yes/no." 
fi


if [ "$up" = yes ]
then
   docker-compose up -d
   echo "Docker-compose up is finished."
elif [ "$up" = no ]
then
   echo "Docker-compose is not up."
else
   echo "Warning '${up}': Acceptable inputs are only yes/no."
fi