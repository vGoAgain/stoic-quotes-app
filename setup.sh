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

echo "Going to run the app, execute: python app.py"

python app.py
