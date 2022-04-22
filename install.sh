#!/bin/bash

sudo apt install gnupg
chmod +x codice.py
sudo ln -s $(readlink -f codice.py) ${PATH%%:*}/codice

