import pandas as pd
import pickle
import math

def predict(input):
    '''
    Función que predice el precio de la propiedad a partir de los
    datos de entrada
    '''
    columns = ['ambientes', 'no_baños', 'terreno_m2', 'año_constr', 'no_dormitorios',
           'area_constr_m2', 'estacionamientos', 'latitud', 'longitud',
           'tipo_de_propiedad', 'ciudad', 'zona']

    data_df = pd.DataFrame([input], columns=columns)
    model_path = "models/model_file.p"
    loaded_model = pickle.load(open(model_path,"rb"))
    prediction = int(loaded_model['model'].predict(data_df))
    #rounding up
    multiple = 1000
    output = math.ceil(prediction / multiple) * multiple

    return int(output)