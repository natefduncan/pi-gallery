#!/bin/bash

SERVER_ADDRESS="100.68.53.128"
SERVER_PORT=8888
DELAY=5

#Check photos folder has enough files
photo_count=ls ./photos | wc -l
download_photos=$(( 10 - photo_count ))

echo ${photo_count}
echo ${download_photos}

for photo in $( seq 1 $download_photos )
do
    curl -N -o ./photos/temp${photo}.jpg http://${SERVER_ADDRESS}:${SERVER_PORT}/random-photo
    echo "Adding temp${photo}.jpg"
done

#Start slideshow
trap break INT
sudo fbi -a -noverbose -T 1 -t ${DELAY} --cachemem 0 photos/*jpg & #Start FBI
sleep $DELAY #Sleep so it can move to next photo before trying to overwrite. 
while :
do
    for counter in {1..10}
    do
        start=$SECONDS
        curl -N -o ./photos/temp${counter}.jpg http://${SERVER_ADDRESS}:${SERVER_PORT}/random-photo 
        jpegtran -rot 90 -trim ./photos/temp${counter}.jpg > ./photos/temp${counter}.jpg
        duration=$(( SECONDS - start ))
        new_sleep=$(( DELAY - duration ))
        sleep $new_sleep; 
    done
done
trap - INT

