import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved model
pickle_in = open('finalized_model.sav', 'rb')
model = pickle.load(pickle_in)

# sidebar for navigation
with st.sidebar.header('Navigation'):
    selected = option_menu('Go to', ['Crop Prediction'])

if selected == 'Crop Prediction':
    st.title('Crop Prediction')

    # getting the input data from the user
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

    with col1:
        nitrogen = st.text_input('Nitrogen in soil', value='')

    with col2:
        phosphorus = st.text_input('Phosphorus in soil', value='')

    with col3:
        potassium = st.text_input('Potassium in soil', value='')

    with col4:
        temperature = st.text_input('Temperature', value='')

    with col5:
        humidity = st.text_input('Humidity', value='')

    with col6:
        ph = st.text_input('pH', value='')

    with col7:
        rainfall = st.text_input('Rainfall', value='')

    # code for prediction
    crop_prediction = ''

    if st.button('Predict'):
        crop_prediction = model.predict([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]])

    crop_names = ['Rice', 'Jute', 'Coconut', 'Maize', 'Papaya', 'Coffee', 'Orange', 'Pigeonpeas', 'Cotton', 'Pomegranate', 'Banana']

    if isinstance(crop_prediction, list) and len(crop_prediction) > 0:
        crop_index = crop_prediction[0]
        st.write(f'The crop is {crop_names[crop_index]}')

    st.success(str(crop_prediction))