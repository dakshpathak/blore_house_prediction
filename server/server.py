from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names', methods = ['GET'])

def get_location_names():
    response = jsonify(
        {
            'Locations' : util.get_location_names()
        }
    )

    response.headers.add('Access-Control-Allow-origin', '*')
    return response

@app.route('/predict_home_prices', methods = ['GET', 'POST'])

def predict_home_prices():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify(
        {
            'get_estimated_price' : util.get_estimated_price(location, total_sqft, bhk, bath)
        }
    )

    response.headers.add('Access-Control-Allow-origin', '*')
    return response

if __name__ == '__main__':
    print ('starting the server')
    util.load_artifacts()
    app.run()