#!/bin/bash

#Read in vars from .env
set -o allexport
source .env
set +o allexport

#Start slideshow
fbi -a -T 1 static/tmp.jpg -noverbose -T 1 -t ${DELAY} --cachemem 0 temp &

#Update temp.jpg file on loop
trap break INT
while :
    do
        curl -o temp.jpg http://${SERVER_ADDRESS}:${SERVER_PORT}/random-photo
        sleep ${DELAY}
    done
trap - INT

