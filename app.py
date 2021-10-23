# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from flask import  flask, request
import pickle
import numpy as np

app = Flask(__name__)

@app.router("/")
def home ():
    return 'Deploy Ml'

@app.router("/predecir", methods=[POST])
def prediccion():
    json = request.get_json(force=True)
    xin = json['Datos']
    print(xin)
    yout = model.predict(xin)
    print(yout)
    mensaje = ''
    for y_out in yout:
        mensaje = mensaje + 'El paciente corresponde a la clase {]'.format(labels[y_out])

    return mensaje

pkl filename = 'modelo.pkl'
with open(pkl_filename, 'rb') as file:
    model = pickle.load(file)

labels = ['Sano', 'Diabetes']

if __name__ == '__main__':
    app.run()


