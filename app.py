import streamlit as st

st.title('Hello, Lonely Octopus!')

st.header('This is a header')
st.subheader('This is a subheader')
st.text('This is some black text.')

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
st.line_chart(df)

# Generate a date range for a month
dates = pd.date_range(start="2024-01-01", end="2024-01-31")

# Weather data remains the same as the previous example
weather_data = {
    "Avg Temperature (°C)": np.round(np.random.normal(loc=18, scale=5, size=len(dates)), 1),
    "Humidity (%)": np.random.randint(40, 80, size=len(dates)),
    "Wind Speed (km/h)": np.round(np.random.uniform(5, 20, size=len(dates)), 1)
}
df_weather = pd.DataFrame(weather_data, index=dates)

# Generating monthly sales data for different services
services = ["Cruises", "Skydiving", "Water skiing"]
sales_data = {
    service: np.random.randint(200, 500, size=12) for service in services
}
months = pd.date_range(start="2024-01-01", end="2024-12-01", freq='MS')
df_sales = pd.DataFrame(sales_data, index=months.strftime('%B'))

chart_type = st.selectbox('Choose a chart type:', ['Line', 'Bar'])

if chart_type == 'Line':
    st.write("Weather Data Overview")
    st.line_chart(df_weather)
elif chart_type == 'Bar':
