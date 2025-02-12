import streamlit as st
import joblib
import numpy as np

# Set page config (MUST be the first Streamlit command)
st.set_page_config(page_title="Item Sales Prediction", page_icon="🛍️", layout="centered")

# Load trained model
model = joblib.load("Asales.pkl")

# Mapping for dropdown values
fat_content_mapping = {"Low Fat": 0, "Regular": 1}
item_type_mapping = {
    "Baking Goods": 0, "Breads": 1, "Canned": 2, "Dairy": 3, "Frozen Foods": 4,
    "Fruits and Vegetables": 5, "Hard Drinks": 6, "Health and Hygiene": 7, "Household": 8,
    "Meat": 9, "Others": 10, "Seafood": 11, "Soft Drinks": 12, "Snack Foods": 13, "Starchy Foods": 14
}
outlet_size_mapping = {"High": 0, "Medium": 1, "Small": 2}
outlet_location_mapping = {"Tier 1": 0, "Tier 2": 1, "Tier 3": 2}
outlet_type_mapping = {
    "Grocery Store": 0, "Supermarket Type1": 1, "Supermarket Type2": 2, "Supermarket Type3": 3
}

# Streamlit UI Design
st.markdown(
    """
    <style>
        .main { background-color: #e8f5e9; padding: 20px; border-radius: 10px; }
        h1 { text-align: center; color: #ff5733; font-family: 'Arial', sans-serif; }
        .stButton>button { background-color: #ff5733; color: white; font-size: 18px; border-radius: 8px; padding: 10px; display: block; margin: auto; }
        .stTextInput, .stSelectbox, .stNumberInput { border-radius: 10px; padding: 8px; }
        .stMarkdown { text-align: center; font-size: 18px; color: #444; }
        .footer { text-align: center; padding: 20px; color: grey; font-size: 14px; }
        .center-button { display: flex; justify-content: center; }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown("<div class='main'>", unsafe_allow_html=True)

st.title("🛒 Item Outlet Sales Prediction")
st.markdown("Predict the sales of an item based on its attributes and outlet details.")
st.markdown("---")

# Input Fields
col1, col2 = st.columns(2)

with col1:
    item_weight = st.number_input("📦 Item Weight (kg)", min_value=0.0, format="%.2f")
    item_visibility = st.number_input("👁️ Item Visibility", min_value=0.0, format="%.4f")
    item_mrp = st.number_input("💲 Item MRP", min_value=0.0, format="%.2f")
    outlet_year = st.selectbox("🏢 Outlet Establishment Year", [1999, 2009, 1998, 1987, 1985, 2002, 2007, 1997, 2004])

with col2:
    fat_content = st.selectbox("🥛 Item Fat Content", list(fat_content_mapping.keys()))
    item_type = st.selectbox("🍽️ Item Type", list(item_type_mapping.keys()))
    outlet_size = st.selectbox("🏬 Outlet Size", list(outlet_size_mapping.keys()))
    outlet_location = st.selectbox("📍 Outlet Location Type", list(outlet_location_mapping.keys()))
    outlet_type = st.selectbox("🏪 Outlet Type", list(outlet_type_mapping.keys()))

# Convert user-friendly inputs to encoded values
fat_content_encoded = fat_content_mapping[fat_content]
item_type_encoded = item_type_mapping[item_type]
outlet_size_encoded = outlet_size_mapping[outlet_size]
outlet_location_encoded = outlet_location_mapping[outlet_location]
outlet_type_encoded = outlet_type_mapping[outlet_type]

# Prepare input array
features = np.array([[
    item_weight, fat_content_encoded, item_visibility, item_type_encoded, item_mrp,
    outlet_year, outlet_size_encoded, outlet_location_encoded, outlet_type_encoded
]]).reshape(1, -1)

# Prediction Button
st.markdown("---")
st.markdown("<div class='center-button'>", unsafe_allow_html=True)
if st.button("💰 Predict Sales"):
    prediction = model.predict(features)[0]
    st.success(f"Predicted Item Outlet Sales: ₹{prediction:.2f}")
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""<div class='footer'>
Developed by Hitanshu ❤️
</div>""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)