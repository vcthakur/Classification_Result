from copyreg import pickle
from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route('/predict_species', methods=['POST'])
def predict_species():
    sepal_length = float(request.form['sepal_length'])
    sepal_width = float(request.form['sepal_width'])
    petal_length = float(request.form['petal_length'])
    petal_width = float(request.form['petal_width'])

    response = jsonify({
        'predicted_species': util.predict_species(sepal_length,sepal_width,petal_length,petal_width)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == '__main__':
    util.load_saved_artifacts()
    app.run(debug=True)