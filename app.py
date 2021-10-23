# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 18:06:12 2021

@author: dreve
"""
import numpy as np
import pickle
import streamlit as st 



pkl_filename = "diabetes_model.pkl"
with open(pkl_filename, 'rb') as file:
    model = pickle.load(file)

labels = ['Sano','Diabetes']       

def prediccion(xin):
    print(xin)
    yout=model.predict(xin)
    print(yout)
    mensaje = ''
    for y_out in yout:
        mensaje =mensaje + 'El paciente corresponde a la clase {}\n'.format(labels[y_out])  
    return mensaje
   

def main():
    # Título
    html_temp = """
    <h1 style="color:#181082;text-align:center;">SISTEMA DE DIAGNOSTICO DE DIABETES </h1>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    # Lecctura de datos
    Datos = st.text_input("Ingrese los valores : ")

    
    # El botón predicción se usa para iniciar el procesamiento
    if st.button("Predicción :"): 
        x_in = list(np.float_((Datos.title().split('\t'))))
        x_in = np.asarray(x_in).reshape(1,8)
        print(x_in.shape)

        predictS = prediccion(x_in)
        st.success(predictS)

if __name__=='__main__':
    main()
    