#!/bin/bash

SERVER_ADDRESS="100.68.53.128"
SERVER_PORT=8888
DELAY=5

#Check photos folder has enough files
cd photos
photo_count=ls | wc -l
download_photos=$(( 5 - photo_count ))
cd ..

echo ${photo_count}
echo ${download_photos}

for photo in $( seq 1 $download_photos )
do
    curl -o ./photos/temp${photo}.jpg http://${SERVER_ADDRESS}:${SERVER_PORT}/random-photo
    python rotate.py ./photos/temp${photo}.jpg
    echo "Adding temp${photo}.jpg"
done

#Start slideshow
trap break INT
sudo fbi -a -noverbose -T 1 -t ${DELAY} --cachemem 0 photos/*jpg & #Start FBI
sleep $DELAY #Sleep so it can move to next photo before trying to overwrite. 
while :
do
    for counter in {1..5}
    do
        start=$SECONDS
        curl -o ./photos/temp${counter}.jpg http://${SERVER_ADDRESS}:${SERVER_PORT}/random-photo 
        ./photos/temp${counter}.jpg
        duration=$(( SECONDS - start ))
        new_sleep=$(( DELAY - duration ))
        if (( $new_sleep > 0 ))
        then
            sleep $new_sleep
        fi
    done
done
trap - INT

