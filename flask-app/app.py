from flask import Flask, render_template
import random

app = Flask(__name__)

# list of fresh prince images
images = [
    "https://media3.giphy.com/media/wqPWKOtW2AD9S/giphy.gif",
    "https://media2.giphy.com/media/KCnqcjvskbT68/giphy.gif",
    "https://media3.giphy.com/media/127x6jFzUcdnJC/giphy.gif",
    "https://media2.giphy.com/media/oczL9Vzsb8m64/giphy.gif",
    "https://media2.giphy.com/media/lH7unKQMtFd9m/giphy.gif",
    "https://media0.giphy.com/media/icpEsPKjP7DZ6/giphy.giff",
    "https://media3.giphy.com/media/8yP9i5T7TB3dC/giphy.gif",
    "https://media3.giphy.com/media/Aapa7lPMJ8wE/giphy.gif",
    "https://media1.giphy.com/media/Y2Y8H0Dbq3kEo/giphy.gif",
    "https://media1.giphy.com/media/H44QlOordAvxS/giphy.gif",
    "https://media2.giphy.com/media/WniXUTI0UhVzG/giphy.gif",
    "https://media0.giphy.com/media/bNZMY3GkWEFLq/giphy.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
