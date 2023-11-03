import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Load a sample dataset (you can replace this with your own data)
@st.cache_data
def load_data():
    data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
    return data

data = load_data()

# Sidebar for data selection
st.sidebar.header('Data Select')
year = st.sidebar.selectbox('Select Year', data['year'].unique())

filtered_data = data[data['year'] == year]

# Display the data table
st.write(f"## Data for {year}")
st.write(filtered_data)

# Data Filtering
st.subheader('Data Filtering')
continent = st.multiselect('Select Continent(s)', filtered_data['continent'].unique())
filtered_data = filtered_data[filtered_data['continent'].isin(continent)]

# Data Statistics
st.subheader('Data Statistics')
st.write(filtered_data.describe())

# Data Visualization
st.subheader('Data Visualization')
fig = px.scatter(filtered_data, x='gdpPercap', y='lifeExp', size='pop', color='country', hover_name='country', log_x=True, size_max=60)
st.plotly_chart(fig)

# Interactive Component
st.subheader('Interactive Component')
selected_country = st.selectbox('Select a Country', filtered_data['country'].unique())
st.write(f"You selected {selected_country}")

# Advanced Customization
st.markdown('## Advanced Customization')
if st.button('Click Me!'):
    st.write('You clicked the button!')

# Conclusion
st.markdown('## Conclusion')
st.write('This is a complicated Streamlit application with data analysis, visualization, and interactivity.')

