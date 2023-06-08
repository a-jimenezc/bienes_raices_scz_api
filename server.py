from flask import Flask, request, jsonify
from src.predict import predict
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/predict', methods=['POST'])  # Use post method
def make_prediction():
    try:
        # Validate and extract the input from the request
        data = request.get_json()
        if 'input' not in data:
            return jsonify({'error': 'Invalid request. Missing "input" field.'}), 400

        to_predict_list = data['input']
        logger.info(f'Received input: {to_predict_list}')

        # Perform prediction
        prediction = predict(to_predict_list)
        logger.info(f'Prediction result: {prediction}')

        # Return the response
        response = {'response': prediction}
        return jsonify(response), 200

    except Exception as e:
        logger.exception('Error occurred during prediction')
        return jsonify({'error': 'An error occurred during prediction.'}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
