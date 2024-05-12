#!/bin/bash

if [[ "$(python3 -V)" =~ "Python 3" ]]
    then
        python3 -m venv .venv
        source .venv/bin/activate
        pip3 install -r requirements.txt
        clear
        python3 main.py
    else
        echo "You do not have Python3 installed"
        echo "Download Python 3 here https://www.python.org/downloads/"
fi

