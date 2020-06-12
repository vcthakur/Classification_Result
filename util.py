import json
import pickle
print(pickle.__doc__)
import sklearn
import numpy as np

def predict_species(sepal_length,sepal_width,petal_length,petal_width):
    x = np.zeros(len(__data_columns))
    x[0] = sepal_length
    x[1] = sepal_width
    x[2] = petal_length
    x[3] = petal_width

    return __model.predict([x])[0]


def load_saved_artifacts():
    print('loading saved artifacts..')
    global __data_columns
    global __model

    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']

    with open("./artifacts/iris_data.pickle", 'rb') as f:
        __model = pickle.load(f)

    print('loading arifacts done......')

if __name__ == '__main__':
    load_saved_artifacts()

