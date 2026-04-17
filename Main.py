import streamlit as st
import pandas as pd

# 1️⃣ Load CSV file
df = pd.read_csv("Chennai_RealEstate1.csv")

# 2️⃣ ✅ HERE add this line
df = df.dropna(how="all")

# 3️⃣ Next steps: encoding, feature selection, etc.
 
