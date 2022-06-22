
import json
import pickle
import numpy as np
from pyparsing import col

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())  # this returns the location index- locations are now columns
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index]=1        #set this column of the x index i.e. location to 1 so that the model can predict price
    
    return round(__model.predict([x])[0],2)

# read the column.json and return the columns of location starting from 4th col

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loading saved artifacts ...start")
    global __data_columns
    global __locations

    with open("/Users/Peluoluwa/Code/RE-prediction/server/artifacts/columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    
    global __model
    with open("/Users/Peluoluwa/Code/RE-prediction/server/artifacts/bangalore_home_prices_model.pickle",'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts ... done")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    # print(get_estimated_price('1st Phase JP Nagar',1000,3,3))
