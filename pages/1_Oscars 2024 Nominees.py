# Import Packages
import pandas as pd 
import streamlit as st

# Functions
@st.cache_data
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
@st.cache_data
def grab_past_winners(url=urlBase):
    dfs = pd.read_html(url)
    df = dfs[0]
    df['Awards'] = df['Awards'].apply(fixFootnotes)
    df['Nominations'] = df['Nominations'].apply(fixFootnotes)
    return df

@st.cache_data

def oscars_vs_bafta(csv_bafta='/Users/adimalik/Documents/Final Projects Awards/Streamlit/BAFTA2024 - Sheet1.csv', csv_oscars='/Users/adimalik/Documents/Final Projects Awards/Streamlit/OSCARS2024 - Sheet1.csv'):
    baftas = pd.read_csv(csv_bafta)
    oscars = pd.read_csv(csv_oscars)
    nominations = baftas.merge(oscars, how='outer', on='Film', suffixes=("_BAFTA", "_OSCAR"))
    nominations = nominations.fillna(0)
    return nominations

###################################################################################################################################################################################################################


# Import Packages
import streamlit as st
import pandas as pd 
import plotly.express as px

# Streamlit Config Settings
st.set_page_config(layout="wide",page_title='Oscars 2024')


# Main App
appDetails = """Adi's Final Project"""

with st.expander("See app info"):
    st.write(appDetails)


# Data
year = '2024'
csv = "/Users/adimalik/Documents/Final Projects Awards/Streamlit/Oscars2024_Nominees.csv"
BAFTA2024 = "/Users/adimalik/Documents/Final Projects Awards/Streamlit/BAFTA2024 - Sheet1.csv"
OSCARS2024 = "/Users/adimalik/Documents/Final Projects Awards/Streamlit/OSCARS2024 - Sheet1.csv"


# Import Data
nominees = grab_nominees(csv) 
nominations = oscars_vs_bafta(BAFTA2024, OSCARS2024)
# st.write(nominees)
selectPage = st.sidebar.selectbox("Select Page", ("Oscars Nominees", "Oscars vs BAFTA"))

if selectPage == "Oscars Nominees":
    st.title(f"🎥 Oscars {year} Nominees 🏆")
    nomineesFilter = nominees.copy()
    filterCategories = st.multiselect("Filter by category (leave blank to show all)", nominees['Category'].unique())
    if len(filterCategories)>0:
        nomineesFilter = nomineesFilter[nomineesFilter['Category'].isin(filterCategories)]
    nominationsOutput = st.radio('Output type',('Chart','Count Summary','Detailed Table'))
    if nominationsOutput == 'Detailed Table':
        st.header('Nominations Details')
        st.write(nomineesFilter)
    elif nominationsOutput == 'Count Summary':
        st.header("# of Nominations by Movie")
        st.write(nomineesFilter['Movie'].value_counts())
    else:
        st.header("Nominations Breakdown by Movie")
        figNom = px.bar(nomineesFilter, x='Movie', y='Count', color="Category", hover_name="Nominee", barmode='stack', height=700, width=800).update_xaxes(categoryorder="total descending")
        figNom.update_yaxes(tickvals=list(range(14)), ticktext=list(range(14)))  # Setting y-labels from 0 to 13 in steps of 1
        st.plotly_chart(figNom)
elif selectPage == "Oscars vs BAFTA":
    st.header("Oscars vs BAFTA Nominations")
    figOscVsBAFTA = px.strip(nominations, x='Nominations_OSCAR', y='Nominations_BAFTA',
                     hover_name='Film', title=f'{year} Oscar Nominations vs BAFTA Nominations')
    st.plotly_chart(figOscVsBAFTA) #strip plot creates a jitter plot (slightly offsets markers for overlaping pts)
    st.write(nominations)

