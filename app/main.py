# main.py

from flask import Flask, render_template, jsonify
from api import get_current_prices, get_historical_data

app = Flask(__name__)

@app.route('/')
def index():
    prices = get_current_prices()
    return render_template('index.html', prices=prices)

@app.route('/history/<crypto_id>')
def history(crypto_id):
    data = get_historical_data(crypto_id)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
