from flask import Flask
import jsonify
from visualizer import finnhub

app = Flask(__name__)

@app.route('/')
def init():
    return finnhub()

if __name__ == '__main__':
    app.run()
