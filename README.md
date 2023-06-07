# API endpoint: estimador de precios de vivienda Santa Cruz de la Sierra

Este es el repositorio para la API implementada en **Flask** para el modelo predictor de precios de de la ciudad de Santa Cruz de la Sierra. Link al repositorio del proyecto original: 
[bienes_raices_scz](https://github.com/a-jimenezc/bienes_raices_scz)

## Endpoint

La API se puede acceder al siguiente link:

```
GET /predict
```

## Request

### Method

La API admite el metodo HTTP GET.

### Parámetros

La API espera una *payload* JSON con el siguiente campo:

- `input` (requerido): una lista con los datos para el modelo.

El orden y el tipo de las variables esperadas por el modelo son:

**[número de ambientes, número de baños, terreno en m2, año de construcción, número de dormitorios, área de construcción, número de estacionamientos, latitud, longitud, tipo de propiedad, ciudad, zona]**

- numéricas (integer/float): [número de ambientes, número de baños, terreno en m2, año de construcción, número de dormitorios, área de construcción, número de estacionamientos, latitud, longitud]
- Categóricas (string):
  - Categorías aceptadas para **tipo de propiedad**: "Departamento", "Casa", "Casa con Espacio Comercial", "Estudio/Monoambiente".
  - Categorías aceptadas para **ciudad**: "Santa Cruz de la Sierra", "Porongo".
  - Categorías aceptadas para **zona**: 'Norte', 'Sur', 'Este', 'Equipetrol/NorOeste', 'Urubo', 'Oeste', 'Sureste', 'Urbari', 'Centro (Casco Viejo)', 'ESTE', 'Noreste', 'Suroeste', 'Noroeste'.

Ejemplo request payload:

```python
{
  "input": [5, 2, 60, 2018, 2, 60, 1, -17.785357, -63.215448, "Departamento", "Santa Cruz de la Sierra", "Oeste"]
}
```

## Response

### Success

Si el request fue exitoso, la API responderá con un *JSON object* con el resultado del estimado.

Example response:

```json
{
  "response": "resultado_estimado"
}
```

### Errores

En caso de error, la API responderá con un código de estado de HTTP apropiado en formato JSON. 

Posibles errores:

- `400 Bad Request`:  Request inválido o sin el requerido *input*.
  ```json
  {
    "error": "Invalid request. Missing 'input' field."
  }
  ```

- `500 Internal Server Error`: Un error ocurrió durante el proceso de estimación.
  ```json
  {
    "error": "An error occurred during prediction."
  }
  ```

## Examples

### Python

Se puede hacer predicción utiizado la librería requests de Python:

```python
import requests

url = 'http://localhost:5000/predict'
data = {
        'input': [5, 2, 60, 2018, 2, 60, 1, -17.785357, 
                -63.215448, "Departamento", "Santa Cruz de la Sierra", "Oeste"]
            }
response = requests.get(url, json=data)

if response.status_code == 200:
    prediction = response.json()['response']
    print(f"Prediction: {prediction}")
else:
    print(f"Error: {response.json()['error']}")
```


## Deployment

La API se colocó en producción utilizando el servivio *serverless* de Google **Cloud Run**.

## Licencia

GNU General Public License v2.0

## Autor

Antonio Jimenez Caballero

## Contacto

[Linkedin](https://www.linkedin.com/in/antonio-jimnzc/)
