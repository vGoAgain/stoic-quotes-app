from flask import Flask, render_template
import random

app = Flask(__name__)

# Stoic wisdom quotes
STOIC_QUOTES = [
    {
        "text": "You have power over your mind - not outside events. Realize this, and you will find strength.",
        "author": "Marcus Aurelius"
    },
    {
        "text": "The obstacle is the way.",
        "author": "Marcus Aurelius"
    },
    {
        "text": "You cannot control what happens to you, but you can control your attitude toward what happens to you, and in that, you will be mastering change rather than allowing it to master you.",
        "author": "Brian Tracy (Stoic Philosophy)"
    },
    {
        "text": "Wealth consists not in having great possessions, but in having few wants.",
        "author": "Epictetus"
    },
    {
        "text": "It is not things that disturb us, but our judgments about things.",
        "author": "Epictetus"
    },
    {
        "text": "Everything we hear is an opinion, not a fact. Everything we see is a perspective, not the truth.",
        "author": "Marcus Aurelius"
    },
    {
        "text": "Our life is what our thoughts make it.",
        "author": "Marcus Aurelius"
    },
    {
        "text": "He who fears death will never do anything worthy of a man who is alive.",
        "author": "Seneca"
    },
    {
        "text": "If you wish to improve, be content to appear foolish and stupid regarding externals.",
        "author": "Epictetus"
    },
    {
        "text": "Freedom is not procured by a full enjoyment of what is desired, but by controlling the desire.",
        "author": "Epictetus"
    }
]

@app.route('/')
def index():
    quote = random.choice(STOIC_QUOTES)
    return render_template('index.html', quote=quote, all_quotes=STOIC_QUOTES)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
