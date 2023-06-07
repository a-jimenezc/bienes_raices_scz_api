import unittest
import requests

class PredictionTest(unittest.TestCase):

    def test_prediction(self):
        data_in = [5, 2, 60, 2018, 2, 60, 1, -17.787357, -63.213448, 'Departamento', 'Santa Cruz de la Sierra', 'Oeste']

        URL = 'http://127.0.0.1:8080/predict'
        data = {"input": data_in}

        r = requests.get(URL, json=data)

        self.assertEqual(r.status_code, 200)
        response = r.json()
        self.assertIn('response', response)
        prediction = response['response']
        self.assertEqual(prediction, 70000)

if __name__ == "__main__":
    unittest.main()
