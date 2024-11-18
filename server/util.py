import pickle
import json
import numpy as np

__data_columns = None
__model = None
__locations = None

def get_estimated_price (location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if loc_index>=0:
        x[loc_index] = 1
    return round(__model.predict([x])[0],2)

import os
import json
import pickle

__data_columns = None
__locations = None
__model = None

def load_artifacts():
    print("loading artifacts")
    global __data_columns
    global __locations
    global __model

    # Get the directory of this script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the correct paths
    columns_path = os.path.join(current_dir, 'artifacts', 'columns.json')
    model_path = os.path.join(current_dir, 'artifacts', 'bengaluru_home_prices_model.pickle')

    # Load columns.json
    with open(columns_path, 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    # Load the model
    if __model is None:
        with open(model_path, 'rb') as f:
            __model = pickle.load(f)

    print("loading of artifacts done")



def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_artifacts()
    print (get_estimated_price('1st Phase JP Nagar', 1000,2,2))