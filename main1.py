import streamlit as st
import pandas as pd
import tensorflow as tf
import numpy as np
import joblib
background_color = """
<style>
body {
    background-color: #f8f7f2; 
}
</style>
"""

# Adding a local image
st.image("img.png", caption=" ", use_column_width=True)


st.markdown(background_color, unsafe_allow_html=True)

# Load the pre-trained model
model = tf.keras.models.load_model("model/model1.h5")

# Create a function to predict water potability
def predict_potability(input_data):
    # Ensure input data is in the correct order
    input_data = input_data[['Turbidity', 'Hardness', 'Sulfate', 'Solids', 'Trihalomethanes', 'Chloramines', 'Conductivity', 'Organic_carbon', 'pH']]
    input_array = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_array)
    return prediction[0][0]

# Streamlit app
st.title(" ")

st.write("Enter the values for the following water parameters:")

turbidity = st.number_input("Turbidity")
hardness = st.number_input("Hardness")
sulfate = st.number_input("Sulfate")
solids = st.number_input("Solids")
trihalomethanes = st.number_input("Trihalomethanes")
chloramines = st.number_input("Chloramines")
conductivity = st.number_input("Conductivity")
organic_carbon = st.number_input("Organic Carbon")
pH = st.number_input("pH")

input_data = pd.DataFrame({
    'Turbidity': [turbidity],
    'Hardness': [hardness],
    'Sulfate': [sulfate],
    'Solids': [solids],
    'Trihalomethanes': [trihalomethanes],
    'Chloramines': [chloramines],
    'Conductivity': [conductivity],
    'Organic_carbon': [organic_carbon],
    'pH': [pH]
})

if st.button("Predict Potability"):
    prediction = predict_potability(input_data)
    if prediction > 0.5:
        st.write("The water is potable.")
    else:
        st.write("The water is not potable.")

