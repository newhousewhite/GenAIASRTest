#!/bin/bash

# parameters
VENV_DIR=$1

# install python3.10
brew install python@3.10

# create VENV
python3.10 -m venv $VENV_DIR

# activate the VENV
source $VENV_DIR/bin/activate

# pip install
pip install -r requirements.txt

## export OPENAI_API_KEY
#export OPENAI_API_KEY="<FILL ME>"

# get voice data