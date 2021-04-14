#!/bin/bash

SERVER_ADDRESS="100.68.53.128"
SERVER_PORT=8888
DELAY=5

feh -x -F -Y -Z -z -R $DELAY --auto-rotate https://$SERVER_ADDRESS:$SERVER_PORT/random-photo