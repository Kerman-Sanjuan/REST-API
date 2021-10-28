#!/bin/bash

cd /code/nodejs
npm start & 

cd /code/python
flask run --host=0.0.0.0
    
#wait 