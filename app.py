import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Save කරගත් Model එක සහ Dataframe එක Load කිරීම
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

st.set_page_config(page_title="Laptop Price Predictor", page_icon="💻", layout="centered")

st.title("💻 Laptop Price Predictor")
st.write("Enter the specifications below to estimate the laptop price.")

# Form Layout එක සකස් කිරීම
col1, col2 = st.columns(2)

with col1:
    # Brand Selectbox
    company = st.selectbox('Brand', df['brand'].unique())

    # RAM Selectbox
    ram = st.selectbox('RAM (in GB)', sorted(df['Ram'].unique()))

    # RAM Type
    ram_type = st.selectbox('RAM Type', df['Ram_type'].unique())

    # ROM (Storage) Capacity
    rom = st.selectbox('Storage Capacity (in GB)', sorted(df['ROM'].unique()))

    # ROM Type
    rom_type = st.selectbox('Storage Type', df['ROM_type'].unique())

with col2:
    # CPU Brand
    cpu = st.selectbox('CPU / Processor', df['Cpu brand'].unique())

    # GPU Brand
    gpu = st.selectbox('GPU Brand', df['Gpu brand'].unique())

    # OS
    os = st.selectbox('Operating System', df['os'].unique())

    # Display Size
    display_size = st.number_input('Display Size (Inches)', min_value=10.0, max_value=20.0, value=15.6, step=0.1)

    # Warranty
    warranty = st.selectbox('Warranty (in Years)', sorted(df['warranty'].unique()))

# Resolution Inputs
resolution_option = st.selectbox(
    'Screen Resolution',
    [
        '1920x1080 (Full HD)',
        '1366x768 (HD)',
        '2560x1440 (2K / QHD)',
        '3840x2160 (4K Ultra HD)',
        '1440x900',
        '1600x900',
        '2880x1800 (Retina Display)'
    ]
)

# Resolution එකෙන් Width සහ Height වෙන් කරගැනීම
res_parts = resolution_option.split(' ')[0].split('x')
res_width = int(res_parts[0])
res_height = int(res_parts[1])
# Spec Rating (Average Value Default)
spec_rating = st.slider('Spec Rating', min_value=30, max_value=100, value=70)

# Predict Button
if st.button('Predict Price 🚀', use_container_width=True):
    # Query DataFrame එක සෑදීම
    query = pd.DataFrame([{
        'brand': company,
        'spec_rating': spec_rating,
        'Ram': ram,
        'Ram_type': ram_type,
        'ROM': rom,
        'ROM_type': rom_type,
        'display_size': display_size,
        'resolution_width': res_width,
        'resolution_height': res_height,
        'warranty': warranty,
        'Cpu brand': cpu,
        'Gpu brand': gpu,
        'os': os
    }])

    # Prediction එක ලබාගැනීම
    predicted_log_price = pipe.predict(query)
    
    # log1p transform කරපු නිසා expm1 භාවිතයෙන් මුල් Price එක ලබාගැනීම
    predicted_price = np.expm1(predicted_log_price)[0]

    st.success(f"💰 Estimated Laptop Price: **INR. {predicted_price:,.2f}** (or approx RS. {predicted_price * 3.6:,.2f})")