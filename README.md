# Stoic Wisdom Quotes - Flask Application

A beautiful Flask web application displaying stoic wisdom quotes from ancient philosophers.

## Features

- Display random stoic quotes on page load
- Browse all 10 quotes at the bottom
- Responsive design that works on mobile and desktop
- Beautiful gradient background and modern styling
- "Get Another Quote" button to refresh with a new random quote

## Setup

### 1. Create Virtual Environment and Install Dependencies

```bash
chmod +x setup.sh
./setup.sh
```

This creates a virtual environment and installs all dependencies.

### 2. Activate Virtual Environment

```bash
source venv/bin/activate
```

### 3. Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

### To Deactivate Virtual Environment

```bash
deactivate
```

## Project Structure

```
stoic-quotes-app/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # HTML template with quotes
└── README.md           # This file
```

## Featured Philosophers

- **Marcus Aurelius** - Roman Emperor and Stoic philosopher
- **Epictetus** - Stoic teacher born a slave
- **Seneca** - Roman statesman and Stoic philosopher

## How It Works

- The Flask app loads a random quote each time you visit
- All quotes are displayed in a scrollable list below
- Click "Get Another Quote" to refresh the main quote
- Fully responsive design for all devices

Enjoy the wisdom of the Stoics!
