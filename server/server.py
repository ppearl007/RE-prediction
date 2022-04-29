from urllib import response
from flask import Flask, request, jsonify
from itsdangerous import json
from pyparsing import removeQuotes
import util

app = Flask(__name__)
# app.config[‘JSONIFY_PRETTYPRINT_REGULAR’] = False

# define the path or route through which you can get to the page
@app.route("/")

# define the pages that will be displayed on the website using functions
def hello():
    return "hi"

@app.route("/get_location_names")
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/predict_home_price", methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server for Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()