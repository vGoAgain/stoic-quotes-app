#!/bin/bash

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

echo "✓ Virtual environment created and dependencies installed!"
echo "Going To activate the environment, run: source venv/bin/activate"
source venv/bin/activate

echo "Going to run the appin background, execute: python app.py"

nohup python app.py > app.log 2>&1 &
