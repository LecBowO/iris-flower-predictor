import streamlit as st
import pickle

model = pickle.load(open('model.pkl', 'rb'))

st.title("IRIS FLOWER PREDICTOR")

sepal_length = st.number_input("sepal length (cm)")
sepal_width = st.number_input("sepal width (cm)")
petal_length = st.number_input("petal length (cm)")
petal_width = st.number_input("petal width (cm)")

data = [[sepal_length, sepal_width, petal_length, petal_width]]

def display():
   st.title(f"The Predicted Flower Is: {prediction}")
    

if st.button("Predict"):
    prediction = model.predict(data)
    if prediction == 0:
        prediction = "Setosa"
    elif prediction == 1:
        prediction = "Versicolor"
    else:
        prediction = "Virginica"
    display()


    