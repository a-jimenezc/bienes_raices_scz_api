# API: Santa Cruz de la Sierra Housing Price Estimator

English | [Español](README_es.md)

This repository contains the Flask implementation of the API for the housing price prediction model for the city of Santa Cruz de la Sierra. (Link to the original project: [bienes_raices_scz](https://github.com/a-jimenezc/bienes_raices_scz)).

## Endpoint

The API can be accessed using the following link:

**:loudspeaker: Note: temporarily out of service, for more information, please contact the provided email.**

[https://bienes-raices-scz-api-ohh5653uva-uc.a.run.app/predict](https://bienes-raices-scz-api-ohh5653uva-uc.a.run.app/predict)

## Request

### Method

The API supports the HTTP GET method.

### Parameters

The API expects a JSON payload with the following field:

- `input` (required): a list containing data for the model.

The order and type of variables expected by the model are:

**[número de ambientes, número de baños, terreno en m2, año de construcción, número de dormitorios, área de construcción, número de estacionamientos, latitud, longitud, tipo de propiedad, ciudad, zona]**

- Numeric (integer/float): [número de ambientes, número de baños, terreno en m2, año de construcción, número de dormitorios, área de construcción, número de estacionamientos, latitud, longitud]
- Categorical (string):
  - Accepted categories for **tipo de propiedad**: "Departamento", "Casa", "Casa con Espacio Comercial", "Estudio/Monoambiente".
  - Accepted categories for **ciudad**: "Santa Cruz de la Sierra", "Porongo".
  - Accepted categories for **zona**: 'Norte', 'Sur', 'Este', 'Equipetrol/NorOeste', 'Urubo', 'Oeste', 'Sureste', 'Urbari', 'Centro (Casco Viejo)', 'ESTE', 'Noreste', 'Suroeste', 'Noroeste'.

Example request payload:

```python
{
    "input": [5, 2, 60, 2018, 2, 60, 1, -17.785357, -63.215448, "Departamento", "Santa Cruz de la Sierra", "Oeste"]
}
```

## Response

### Success

If the request was successful, the API will respond with a JSON object containing the estimated result.

Example response:

```json
{
  "response": "estimated_result"
}
```

### Errors

In case of an error, the API will respond with an appropriate HTTP status code in JSON format.

Possible errors:

- `400 Bad Request`: Invalid request or missing the required 'input' field.
  ```json
  {
    "error": "Invalid request. Missing 'input' field."
  }
  ```

- `500 Internal Server Error`: An error occurred during the estimation process.
  ```json
  {
    "error": "An error occurred during prediction."
  }
  ```

## Examples

### Python

You can make predictions using the Python requests library:

```python
import requests

url = 'https://bienes-raices-scz-api-ohh5653uva-uc.a.run.app/predict'
data = {
        'input': [5, 2, 60, 2018, 2, 60, 1, -17.786, 
                -63.216, "Departamento", "Santa Cruz de la Sierra", "Oeste"]
            }
response = requests.post(url, json=data)

if response.status_code == 200:
    prediction = response.json()['response']
    print(f"Prediction: {prediction}")
else:
    print(f"Error: {response}")
```

## Deployment

The API was deployed in production using the serverless Google Cloud Run service.

## License

GNU General Public License v2.0

## Author

Antonio Jimenez Caballero

## Contact

[Linkedin](https://www.linkedin.com/in/antonio-jimnzc/)
