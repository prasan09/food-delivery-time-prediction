import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("delivery_time_model.pkl")

st.title("🚀 Food Delivery Time Prediction System")

st.write("Enter Delivery Details")

# ---- USER INPUTS ----

age = st.number_input("Delivery Person Age", min_value=18, max_value=60)
rating = st.number_input("Delivery Person Rating", min_value=1.0, max_value=5.0)
distance = st.number_input("Distance (in km)", min_value=0.1)

order_type = st.selectbox(
    "Type of Order",
    ["Drinks", "Meal", "Snack"]
)

vehicle_type = st.selectbox(
    "Type of Vehicle",
    ["electric_scooter", "motorcycle", "scooter"]
)

# ---- PREDICTION ----

if st.button("Predict Delivery Time"):

    # Create full feature dictionary (ALL columns initialized to 0)
    input_dict = {
        "Delivery_person_Age": age,
        "Delivery_person_Ratings": rating,
        "distance_km": distance,
        "Type_of_order_Drinks ": 0,
        "Type_of_order_Meal ": 0,
        "Type_of_order_Snack ": 0,
        "Type_of_vehicle_electric_scooter ": 0,
        "Type_of_vehicle_motorcycle ": 0,
        "Type_of_vehicle_scooter ": 0
    }

    # Activate selected order type
    input_dict[f"Type_of_order_{order_type} "] = 1

    # Activate selected vehicle type
    input_dict[f"Type_of_vehicle_{vehicle_type} "] = 1

    # Convert to DataFrame
    input_df = pd.DataFrame([input_dict])

    # Ensure column order matches training
    input_df = input_df[model.feature_names_in_]

    # Predict
    prediction = model.predict(input_df)

    st.success(f"⏱ Estimated Delivery Time: {prediction[0]:.2f} minutes")
