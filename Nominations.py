"""# Import Packages
import streamlit as st
import pandas as pd 
import plotly.express as px
import oscarUDFs as osc

# Streamlit Config Settings
st.set_page_config(layout="wide",page_title='Oscars 2024')


# Main App
appDetails = "Adi's Final Project"
with st.expander("See app info"):
    st.write(appDetails)


# Pick Year
year = st.sidebar.selectbox("Select Year", ('2024','2023','2022'))
csvs = {'2022': "Oscars2022_Nominees.csv", '2023':"Oscars2023_Nominees.csv", '2024':"Oscars2024_Nominees.csv" }
baftas = {'2022':'75th', '2023':'76th', '2024':'77th'}
oscars = {'2022':'94th', '2023':'95th', '2024':'96th'} 

# Data
csv = csvs[year]
urlBAFTA = f"https://en.wikipedia.org/wiki/{baftas[year]}_British_Academy_Film_Awards"
urlOSCARS = f"https://en.wikipedia.org/wiki/{oscars[year]}_Academy_Awards"


# Import Data
nominees = osc.grab_nominees(csv) 
nominations = osc.oscars_vs_bafta(urlBAFTA, urlOSCARS)
# st.write(nominees)
selectPage = st.sidebar.selectbox("Select Page", ("Oscars Nominees", "Oscars vs BAFTA"))

if selectPage == "Oscars Nominees":
    st.title(f"🏆Oscars {year} Nominees🎥")
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
        figNom = px.bar(nomineesFilter, x='Movie', y='Count', color="Category", hover_name="Nominee", barmode='stack', height=600).update_xaxes(categoryorder="total descending")
        st.plotly_chart(figNom)
elif selectPage == "Oscars vs BAFTA":
    st.header("Oscars vs BAFTA Nominations")
    figOscVsBAFTA = px.strip(nominations, x='Nominations_OSCAR', y='Nominations_BAFTA',
                     hover_name='Film', title=f'{year} Oscar Nominations vs BAFTA Nominations')
    st.plotly_chart(figOscVsBAFTA) #strip plot creates a jitter plot (slightly offsets markers for overlaping pts)
    st.write(nominations)"""


# Import Packages
import streamlit as st
import pandas as pd 
import plotly.express as px
import oscarUDFs as osc

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
nominees = osc.grab_nominees(csv) 
nominations = osc.oscars_vs_bafta(BAFTA2024, OSCARS2024)
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
        figNom = px.bar(nomineesFilter, x='Movie', y='Count', color="Category", hover_name="Nominee", barmode='stack', height=600).update_xaxes(categoryorder="total descending")
        st.plotly_chart(figNom)
elif selectPage == "Oscars vs BAFTA":
    st.header("Oscars vs BAFTA Nominations")
    figOscVsBAFTA = px.strip(nominations, x='Nominations_OSCAR', y='Nominations_BAFTA',
                     hover_name='Film', title=f'{year} Oscar Nominations vs BAFTA Nominations')
    st.plotly_chart(figOscVsBAFTA) #strip plot creates a jitter plot (slightly offsets markers for overlaping pts)
    st.write(nominations)

