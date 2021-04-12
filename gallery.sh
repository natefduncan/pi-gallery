#!/bin/bash

SERVER_ADDRESS="100.68.53.128"
SERVER_PORT=8888
DELAY=5

#Start slideshow

#Update temp.jpg file on loop
trap break INT
sudo fbi -a -noverbose -T 1 -t ${DELAY} --cachemem 0 photos/ & 
sleep ${DELAY}
while :
    for counter in {1..10}
        do
            curl -o /temp${counter}.jpg http://${SERVER_ADDRESS}:${SERVER_PORT}/random-photo && 
            sleep ${DELAY}
        done
trap - INT

