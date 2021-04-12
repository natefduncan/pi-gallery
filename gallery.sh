#!/bin/bash

SERVER_ADDRESS="100.68.53.128"
SERVER_PORT=8888
DELAY=5

#Check photos folder has enough files
photo_count=ls -l | grep -v ^d | wc -l
echo ${photo_count}
download_photos=$(( 5 - photo_count ))
echo ${download_photos}

for photo in $( seq 1 $download_photos )
do
    curl -o ./photos/temp${photo}.jpg http://${SERVER_ADDRESS}:${SERVER_PORT}/random-photo 
done

#Start slideshow
trap break INT
sudo fbi -a -noverbose -T 1 -t ${DELAY} --cachemem 0 ./photos & #Start FBI
sleep ${DELAY} #Sleep so it can move to next photo before trying to overwrite. 
while :
    for counter in {1..5}
        do
            curl -o /temp${counter}.jpg http://${SERVER_ADDRESS}:${SERVER_PORT}/random-photo && #Download new photo
            sleep ${DELAY} 
        done
trap - INT

