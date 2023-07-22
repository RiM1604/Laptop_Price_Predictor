from flask import Flask, request, jsonify, render_template
import util
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def interface():
    return render_template(app.html)


@app.route('/get_location_names')
def get_locations():
    location_names = util.get_location_names()
    response = jsonify({
        'locations': location_names
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# making a dict and jsonify then send as response
# to get info from the form in the front end use request.form['term]
@app.route('/predict_prices', methods=['POST', 'GET'])
def predict_prices():
    company = request.form['company']
    memory = float(request.form['memory'])
    ram = float(request.form['ram'])
    os = float(request.form['os'])
    size_in_inches = float(request.form['size_in_inches'])
    estimated_price = util.get_price(company, memory, ram, os, size_in_inches)
    response = jsonify({
        "estimated_price": estimated_price,
        "message": 'route working'
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    util.load_saved_artifacts()
    print("Starting the server...")
    app.run(debug=True)
