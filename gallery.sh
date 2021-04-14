#!/bin/bash

SERVER_ADDRESS=
SERVER_PORT=
DELAY=5

feh -x -F -Y -Z -z -R $DELAY --auto-rotate http://$SERVER_ADDRESS:$SERVER_PORT/random-photo
