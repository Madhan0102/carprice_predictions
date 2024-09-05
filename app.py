import streamlit as st
import pandas as pd
import joblib

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = joblib.load(file)

# Apply custom CSS styles for better UI
st.markdown("""
    <style>
        .main {
            background-color: #f5f5f5;
        }
        h1 {
            color: #ff4b4b;
        }
        .stButton button {
            background-color: #ff4b4b;
            color: white;
            font-size: 18px;
            border-radius: 10px;
        }
        .stSelectbox, .stNumberInput {
            font-size: 16px;
        }
        .stSuccess {
            color: green;
            font-size: 22px;
        }
    </style>
""", unsafe_allow_html=True)

# App title with subheading
st.title("🚗 Car Price Prediction App")
st.subheader("Get an accurate estimate of your car's selling price!")

# Add a header for user inputs
st.markdown("<h2 style='color: #ff4b4b;'>Input Car Details</h2>", unsafe_allow_html=True)

# Input fields for car details
name = st.selectbox("🚘 Select Car Name", ['Maruti 800 AC', 'Maruti Wagon R LXI Minor',
       'Hyundai Verna 1.6 SX', 'Mahindra Verito 1.5 D6 BSIII',
       'Toyota Innova 2.5 VX (Diesel) 8 Seater BS IV',
       'Hyundai i20 Magna 1.4 CRDi'])
year = st.number_input("📅 Year of Purchase", min_value=1990, max_value=2024, value=2015)
km_driven = st.number_input("🛣️ Kilometers Driven", min_value=0, value=50000)

# Categorical feature encodings
fuel_options = {"Diesel": 0, "Petrol": 1, "CNG": 2, "LPG": 3, "Electric": 4}
fuel = st.selectbox("⛽ Fuel Type", list(fuel_options.keys()))
fuel_encoded = fuel_options[fuel]

seller_type_options = {"Individual": 0, "Dealer": 1, "Trustmark Dealer": 2}
seller_type = st.selectbox("🧑‍💼 Seller Type", list(seller_type_options.keys()))
seller_type_encoded = seller_type_options[seller_type]

transmission_options = {"Manual": 0, "Automatic": 1}
transmission = st.selectbox("⚙️ Transmission Type", list(transmission_options.keys()))
transmission_encoded = transmission_options[transmission]

owner_options = {"Test Drive Car": 0, "First Owner": 1, "Second Owner": 2, "Third Owner": 3, "Fourth & Above Owner": 4}
owner = st.selectbox("👥 Number of Previous Owners", list(owner_options.keys()))
owner_encoded = owner_options[owner]

# Add a section for the prediction button
st.markdown("<h2 style='color: #ff4b4b;'>Ready to Get Your Estimate?</h2>", unsafe_allow_html=True)

# Predict button with custom styling
if st.button("🚀 Predict Price"):
    # Create input DataFrame
    input_data = pd.DataFrame([[year, km_driven, fuel_encoded, seller_type_encoded, transmission_encoded, owner_encoded]],
                              columns=['year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner'])
    
    # Predict the price
    predicted_price = model.predict(input_data)[0]

    # Display the prediction in a styled format
    st.markdown(f"<h3 style='color: green;'>The estimated selling price of the car is: ₹{predicted_price:,.2f}</h3>", unsafe_allow_html=True)