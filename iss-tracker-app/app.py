import streamlit as st
import requests
import pandas as pd
import numpy as np

st.title("🚀 People in Space & ISS Tracker")
st.markdown("""
This app shows:
- The current number of people in space 🧑‍🚀
- Their names
- The current position of the International Space Station (ISS) 🌍
""")

# --- Part 1: People in Space ---
people_url = "http://api.open-notify.org/astros.json"
people_res = requests.get(people_url).json()

st.subheader("👨‍🚀 People Currently in Space")
st.markdown(f"**Total number:** {people_res['number']}")
names = [person['name'] for person in people_res['people']]
st.markdown("**Names:**")
for name in names:
    st.markdown(f"- {name}")

# --- Part 2: ISS Current Location ---
iss_url = "http://api.open-notify.org/iss-now.json"
iss_res = requests.get(iss_url).json()

latitude = float(iss_res['iss_position']['latitude'])
longitude = float(iss_res['iss_position']['longitude'])

st.subheader("🛰️ Current ISS Location")
st.markdown(f"**Latitude:** {latitude}, **Longitude:** {longitude}")
st.markdown("Below is the current ISS location on the world map.")

# Map expects a DataFrame with lat/lon columns
location_df = pd.DataFrame([[latitude, longitude]], columns=["lat", "lon"])
st.map(location_df,zoom=2)


# lat, lon = 37.76, -122.4  # San Francisco
# df_san = pd.DataFrame([{"lat": lat, "lon": lon}])
# st.map(df_san)