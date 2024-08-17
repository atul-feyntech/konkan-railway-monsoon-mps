import streamlit as st
import pandas as pd

# Load CSV files into dataframes
files = {
    "Coaching Stocks": pd.read_csv("KRCL_Coaching_Stocks_Speeds.csv"),
    "Diesel Locomotives": pd.read_csv("KRCL_Diesel_Locomotive_Speeds.csv"),
    "Electric Locomotives": pd.read_csv("KRCL_Electric_Locomotive_Speeds_Combined.csv"),
    "Maintenance Vehicles": pd.read_csv("KRCL_Maintenance_Vehicles_Speeds.csv"),
    "Wagons": pd.read_csv("KRCL_Wagon_Speeds_Combined.csv")
}

# App title and subtitle
st.title("Konkan Railway Monsoon MPS")
st.subheader("Maximum Permissible Speed for Different Rolling Stock of Konkan Railways")

# Dropdown for selecting the type of rolling stock
rolling_stock_type = st.selectbox("Select the Type of Rolling Stock", list(files.keys()))

# Dropdown for selecting the specific type within the selected rolling stock
df = files[rolling_stock_type]
type_column = "Type" if "Type" in df.columns else df.columns[0]
selected_type = st.selectbox(f"Select the {type_column}", df[type_column].unique())

# Display the relevant data row for the selected type
selected_row = df[df[type_column] == selected_type].squeeze()

# Display data in a clear, legible format with line breaks
for column, value in selected_row.items():
    st.write(f"**{column}:** {value}")

# Make the UI phone-friendly by using Streamlit's mobile layout features
st.markdown("""
    <style>
    /* Adjust the text and layout to be more readable on phones */
    .stSelectbox, .stTextInput, .stTextArea {
        font-size: 18px;
    }
    /* Ensure text wraps properly and is easy to read */
    .streamlit-expanderHeader {
        font-size: 16px !important;
    }
    </style>
    """, unsafe_allow_html=True)
