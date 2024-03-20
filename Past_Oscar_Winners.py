import streamlit as st
import pandas as pd
import plotly.express as px
import builtins
from sys import builtin_module_names

# Streamlit Config Settings
st.set_page_config(layout="wide", page_title='Past Oscar Winners')

# Functions
def fixFootnotes(messyNum):
    messyNum = str(messyNum)
    if "(" in messyNum:
        messyNum = messyNum.split("(")[0].strip()
    elif "[" in messyNum:
        messyNum = messyNum.split("[")[0].strip()
    clean = int(messyNum)
    return clean

def my_hash_func(func):
    return None

#@st.cache(hash_funcs={builtins.function: my_hash_func})
"""st.cache_resource
def get_data_from_url(url):
    dfs = pd.read_html(url)
    df = dfs[0]
    df['Awards'] = df['Awards'].apply(fixFootnotes)
    df['Nominations'] = df['Nominations'].apply(fixFootnotes)
    return df"""

"""@st.cache
def get_data_from_url(url):
    dfs = pd.read_html(url)
    df = dfs[0]
    df['Awards'] = df['Awards'].apply(fixFootnotes)
    df['Nominations'] = df['Nominations'].apply(fixFootnotes)
    return df"""

@st.cache_data
def get_data_from_url(url):
    dfs = pd.read_html(url)
    df = dfs[0]
    df['Awards'] = df['Awards'].apply(fixFootnotes)
    df['Nominations'] = df['Nominations'].apply(fixFootnotes)
    return df

def grab_past_winners():
    url = "https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films"
    return get_data_from_url(url)

def grab_other_awards():
    df = pd.read_excel("/Users/adimalik/Documents/Final Projects Awards/Streamlit/oscars comparison to sag.xlsx", sheet_name=1, header=3)
    df2 = pd.read_excel("/Users/adimalik/Documents/Final Projects Awards/Streamlit/oscars comparison to sag.xlsx", sheet_name=0, header=2, nrows=5)
    return df, df2

# Format Map
portFormats = {}

appDetails = """Adi's Final Project"""

with st.expander("See app info"):
    st.write(appDetails)

pastWinnersDF = grab_past_winners()
otherAwardsDF, summaryDF = grab_other_awards()

st.title("🎥 Past Oscar Winners 🏆")
selectPage = st.sidebar.radio("Select Page", ("Nominations vs Awards", "Oscars vs Other Awards"))
if selectPage == "Nominations vs Awards":
    aLinks = '''Live source from: <a href="https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films" target="_blank">https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films</a><br>'''
    st.markdown(aLinks, unsafe_allow_html=True)
    
    figPastWinners = px.scatter(pastWinnersDF, x='Nominations', y='Awards',
                   color='Year', hover_name='Film', title='Nominations vs Awards')
    figPastWinnersJitter = px.strip(pastWinnersDF, x='Nominations', y='Awards',
                   color='Year', hover_name='Film', title='Nominations vs Awards')
    
    st.plotly_chart(figPastWinnersJitter) #strip plot creates a jitter plot (slightly offsets markers for overlaping pts)
    st.write(pastWinnersDF)
else:
    st.header("Oscars vs Other Awards")
    awardsDetails = """
    Sources and details of other awards:
    - SAG - <a href="https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films" target="_blank">Screen Actors Guild Awards</a>: Awarded since 1995, overlaps in 5 major categories with Osacars (best leading and supporting actor/actress, best picture). Categories can also be filtered in a dropdown.
    - BAFTA - <a href="https://en.wikipedia.org/wiki/British_Academy_Film_Awards" target="_blank">British Academy Film Awards</a>: Similar categories to Oscars, but more focus on international films. Much lower correlations to Oscars than the SAG awards.
    """
    st.markdown(awardsDetails, unsafe_allow_html=True)
    # st.write(summaryDF)
    categories = otherAwardsDF['Category'].unique()
    years = otherAwardsDF['Year'].unique()
    categoriesPick = st.multiselect('Pick categories to filter:', categories, categories)
    # yearsPick = st.multiselect('Pick years to filter:', years, years)    
    years = st.slider('Select a range of years to filter', otherAwardsDF['Year'].min(), otherAwardsDF['Year'].max(), (otherAwardsDF['Year'].min(), otherAwardsDF['Year'].max()))
    # filterDF = otherAwardsDF[(otherAwardsDF['Category'].isin(categoriesPick)) & (otherAwardsDF['Year'].isin(yearsPick))]
    filterDF = otherAwardsDF[(otherAwardsDF['Category'].isin(categoriesPick)) & (otherAwardsDF['Year'].between(years[0],years[1], inclusive='both'))]

    summary = filterDF.groupby(['Category'])[['OSCARS','SAG','BAFTA']].sum()
    otherAwards = ['SAG','BAFTA']
    for award in otherAwards:
        summary[award + " Overlap %"] = summary[award] / summary['OSCARS']
        portFormats[award + " Overlap %"] = '{:0.1%}'

    st.dataframe(summary.style.highlight_max(axis=0).format(portFormats))
    fig = px.imshow(summary.iloc[:,-4:], text_auto=True)
    st.plotly_chart(fig)
    st.write(filterDF)
