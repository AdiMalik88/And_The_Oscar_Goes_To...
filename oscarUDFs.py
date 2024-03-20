"""# Import Packages
import pandas as pd 
import streamlit as st

# Functions
@st.cache
def grab_nominees(csv):
    #csv = "Oscars2024_Nominees.csv"
    df = pd.read_csv(csv,encoding='latin1')
    df['Count'] = 1
    df['Nominee Full'] = df.apply(lambda x: x['Nominee'] + " (" + x['Movie'] + ")", axis=1)
    return df

def fixFootnotes(messyNum):
    messyNum = str(messyNum)
    if "(" in messyNum:
        messyNum = messyNum.split("(")[0].strip()
    elif "[" in messyNum:
        messyNum = messyNum.split("[")[0].strip()
    clean = int(messyNum)
    return clean

urlBase = "https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films"
@st.cache
def grab_past_winners(url=urlBase):
    dfs = pd.read_html(url)
    df = dfs[0]
    df['Awards'] = df['Awards'].apply(fixFootnotes)
    df['Nominations'] = df['Nominations'].apply(fixFootnotes)
    return df

urlBAFTA2023 = "https://en.wikipedia.org/wiki/77th_British_Academy_Film_Awards"
urlOSCARS2023 = "https://en.wikipedia.org/wiki/96th_Academy_Awards"
@st.cache
def oscars_vs_bafta(urlBAFTA=urlBAFTA2023, urlOSCARS=urlOSCARS2023):
    dfs = pd.read_html(urlBAFTA, match='Nominations')
    baftas = dfs[0]
    baftas['Film'] = baftas['Film'].apply(lambda x: x.split('[')[0].strip()) #sometimes footnotes in film name e.g. "[0]"
    dfs = pd.read_html(urlOSCARS, match='Nominations')
    oscars = dfs[0]
    nominations = baftas.merge(oscars, how='outer',on=['Film'], suffixes=("_BAFTA","_OSCAR"))
    nominations = nominations.fillna(0)
    return nominations"""

# Import Packages
import pandas as pd 
import streamlit as st

# Functions
@st.cache
def grab_nominees(csv):
    csv = "/Users/adimalik/Documents/Final Projects Awards/Streamlit/Oscars2024_Nominees.csv"
    df = pd.read_csv(csv,encoding='latin1')
    df['Count'] = 1
    df['Nominee Full'] = df.apply(lambda x: x['Nominee'] + " (" + x['Movie'] + ")", axis=1)
    return df

def fixFootnotes(messyNum):
    messyNum = str(messyNum)
    if "(" in messyNum:
        messyNum = messyNum.split("(")[0].strip()
    elif "[" in messyNum:
        messyNum = messyNum.split("[")[0].strip()
    clean = int(messyNum)
    return clean

urlBase = "https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films"
@st.cache
def grab_past_winners(url=urlBase):
    dfs = pd.read_html(url)
    df = dfs[0]
    df['Awards'] = df['Awards'].apply(fixFootnotes)
    df['Nominations'] = df['Nominations'].apply(fixFootnotes)
    return df

@st.cache

def oscars_vs_bafta(csv_bafta='/Users/adimalik/Documents/Final Projects Awards/Streamlit/BAFTA2024 - Sheet1.csv', csv_oscars='/Users/adimalik/Documents/Final Projects Awards/Streamlit/OSCARS2024 - Sheet1.csv'):
    baftas = pd.read_csv(csv_bafta)
    oscars = pd.read_csv(csv_oscars)
    nominations = baftas.merge(oscars, how='outer', on='Film', suffixes=("_BAFTA", "_OSCAR"))
    nominations = nominations.fillna(0)
    return nominations


"""def oscars_vs_bafta(BAFTA=BAFTA2024, OSCARS=OSCARS2024):
    dfs = pd.read_csv(BAFTA)
    baftas = dfs[0]
    baftas['Film'] = baftas['Film'].apply(lambda x: x.split('[')[0].strip()) # Sometimes footnotes in film name e.g. "[0]"
    dfs = pd.read_csv(OSCARS)
    oscars = dfs[0]
    nominations = baftas.merge(oscars, how='outer',on=['Film'], suffixes=("_BAFTA","_OSCAR"))
    nominations = nominations.fillna(0)
    return nominations"""
