#!/bin/sh
export FLASK_APP=./group-ride-api/app
source ./Scripts/activate
flask run -h 0.0.0.0
sleep 100