import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(Glucose,BP,Insulin,BMI):
    
    """Let's Test the Diabetes 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: Glucose
        in: query
        type: number
        required: true
      - name: BP
        in: query
        type: number
        required: true
      - name: Insulin
        in: query
        type: number
        required: true
      - name: BMI
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[Glucose,BP,Insulin,BMI]])
    print(prediction)
    return prediction



def main():
    st.title("Diabetes")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Glucose = st.text_input("Glucose","Type Here")
    BP = st.text_input("BP","Type Here")
    Insulin = st.text_input("Insulin","Type Here")
    BMI = st.text_input("BMI","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_Diabetes(Glucose,BP,Insulin,BMI)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()