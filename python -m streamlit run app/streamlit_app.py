import streamlit as st
import pandas as pd

# Page config MUST be first
st.set_page_config(layout="wide")

# Page title
st.title("Chennai Real Estate Analyzer")
st.write("Location: Chennai")

# Load dataset (you can keep absolute path for now)
df = pd.read_csv(
    r"C:\Users\7359211\OneDrive - Western Digital\Desktop\Real_Estate_WhatIf_Analyzer\data\Chennai_RealEstate.csv"
)

# Display ONLY full dataset
st.subheader("Full Housing Dataset (All Rows & Columns)")
st.dataframe(df)


