import streamlit as st

# Streamlit Config Settings
st.set_page_config(layout="wide", page_title="And_The_Oscar_Goes_To...")

# Main header
st.title("⌛ Adi's Final Project ⌛")

# Introduction
st.header("Introduction:")
st.write("Welcome to the culmination of eight weeks of intensive learning in Data Analytics at IronHack! "
         "My final project, titled 'And_The_Oscar_Goes_To...', represents the fusion of newfound skills in Python programming, "
         "data analysis, and visualization.")

# Project Overview
st.header("Project Overview:")
st.write("At its core, 'And_The_Oscar_Goes_To...' is an exploration of the capabilities of the Streamlit Python package, "
         "showcasing a blend of dashboard components and interactive charts crafted with Python. This application serves "
         "as a testament to my journey through data analytics, offering users an immersive experience navigating through "
         "four main pages accessible via a dropdown menu in the sidebar:")

# List of main pages
st.subheader("1. Oscar 2024 Nominees:")
st.write("Delve into the current year's Oscar nominees, categorized by movie and award category, presented through "
         "interactive Plotly bar charts and detailed tables.")

st.subheader("2. My Predictions:")
st.write("Utilizing machine learning techniques, this section provides insights into Oscar predictions. By aggregating "
         "data from major movie awards and employing classifiers, I've crafted a model to forecast potential winners.")

st.subheader("3. Past Oscar Winners:")
st.write("Drawing live data from Wikipedia, this page offers a comprehensive overview of historical Oscar winners. "
         "The standout feature here is the interactive 'jitter' plot, revealing nuanced insights into the relationship "
         "between nominations and awards won by movies.")

st.subheader("4. Best Picture Emoji Quiz:")
st.write("As a lighthearted addition, this page invites users to test their knowledge with an engaging emoji-based quiz. "
         "Each of the ten Best Picture nominees is represented by a unique set of emojis, challenging participants in both "
         "easy and hard modes.")

st.write("Throughout this project, I've applied a diverse array of skills, from data gathering and preprocessing to "
         "machine learning model implementation and interactive visualization techniques. Join me as we embark on an "
         "immersive journey through the world of Oscars and data analytics!")
