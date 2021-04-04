#!/bin/bash

SERVER_ADDRESS="100.68.53.128"
SERVER_PORT=8888
DELAY=5

#Start slideshow

#Update temp.jpg file on loop
trap break INT
while :
    do
        sudo fbi -a -noverbose -T 1 --cachemem 0 temp.jpg &
        curl -o temp.jpg http://${SERVER_ADDRESS}:${SERVER_PORT}/random-photo &
        sleep ${DELAY} 
    done
trap - INT

