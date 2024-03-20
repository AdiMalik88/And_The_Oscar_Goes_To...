# Import Packages
import streamlit as st
import pandas as pd 
import plotly.express as px
import builtins
from sys import builtin_module_names

# Streamlit Config Settings
st.set_page_config(layout="wide",page_title= "My Predictions")

# Main Map
appDetails = """Adi's Final Project"""

with st.expander("See app info"):
    st.write(appDetails)

st.title("🤔 Oscar Predictions 🤔")

st.header("My ML Model 🎰")
"""
    - To meet the March 10th, 2024 deadline before the Oscars, I gathered data from various sources, excluding web-scraping IMDB due to time constraints.
    - Fortunately, I obtained data on past winners and nominations from major movie awards like the Oscars, Golden Globes, Baftas, and SAG Awards, though not all were updated to 2024, supplemented by information from Wikipedia.
    - Organizing the data into four separate data frames in Jupyter Notebook, I focused on six key categories (Actor, Actress, Supporting Actor, Supporting Actress, Director, and Movie), starting from 1997.
    - After cleaning and standardizing, I merged the data frames, noting an imbalance with 680 false (nominations), 156 true (winners), and 35 TBA (to be awarded on March 10th).
    - Segregating the 35 TBA entries into a separate data frame, I experimented with both under-sampling and over-sampling techniques, using three classifiers: DecisionTreeClassifier, GridSearch CSV, and RandomForestClassifier.
    - Results varied for each approach:
    1. DecisionTreeClassifier:
    -     Accuracy for under-sampled data: 0.7778
    -     Accuracy for over-sampled data: 0.8466
    2. GridSearch CSV:
    -     Accuracy for under-sampled data: 0.7619
    -     Accuracy for over-sampled data: 0.8455
    3. RandomForestClassifier:
    -     Accuracy for under-sampled data: 0.8125
    -     Accuracy for over-sampled data: 0.8509

    - Hyper-tuning the RandomForestClassifier yielded an accuracy of 0.8676470588235294.
    - Following this, the model successfully predicted the outcomes."""

def main():
    st.title("Model's Predictions")

    # Read CSV file
    df = pd.read_csv("df_oscar_goes_to_copy.csv")
    
    # Display the dataframe
    st.write(df)

if __name__ == "__main__":
    main()


def main():
    st.title("Concise Predictions")

    # Read CSV file
    df2 = pd.read_csv("Predicted_Winners.csv")
    
    # Display the dataframe
    st.write(df2)

if __name__ == "__main__":
    main()

# Add an image to the app
def main():
    st.title("Two Important Critics (Me (AAM) & My Wife (AFC)) Predictions")
    
    image = 'Our Predictions.JPG'
    st.image(image, caption='Two Important Critics', use_column_width=True)

if __name__ == "__main__":
    main()


"""def main():
    st.title("Two Important Critics (Me (AAM) & My Wife (AFC)) Predictions")

image = 'Our Predictions.JPG'

st.image(image, caption='Two Important Critics', use_column_width=True)

if __name__ == "__main__":
    main()"""
