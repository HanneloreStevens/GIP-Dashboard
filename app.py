import pandas as pd  
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="GIP Dashboard", 
    page_icon=":bar_chart:", 
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"}
    )

# ---- READ EXCEL LIQUIDITEIT ----
@st.cache
def get_liquiditeit_from_excel():
    df = pd.read_excel(
        io="data/GIP_analyse van de jaarrekening_Stevens_Hannelore.xlsx",
        engine="openpyxl",
        sheet_name="Liquiditeit",
        usecols="A:D",
        nrows=40,
        skiprows=1
    )

    #change column names
    # change column names
    df.columns = ["Type","Boekjaar 1","Boekjaar 2","Boekjaar 3"]
    # filter row on column value
    liquiditeit = ["Liquiditeit in ruime zin","Liquiditeit in enge zin"]
    df = df[df["Type"].isin(liquiditeit)]

    df = df.T #Transponeren
    df = df.rename(index={"Boekjaar 1":"1","Boekjaar 2":"2",
                    "Boekjaar 3":"3"})
    df = df.iloc[1: , :] # Drop first row 
    df.insert(0,"Boekjaar",["Boekjaar 1","Boekjaar 2",
                    "Boekjaar 3"],True)
    df.columns = ["Boekjaar","Liquiditeit in ruime zin","Liquiditeit in enge zin"] # change column names
    
    
    return df

df_liquiditeit = get_liquiditeit_from_excel()



# ---- READ EXCEL SOLVABILITEIT ----
@st.cache
def get_solvabiliteit_from_excel():
    df = pd.read_excel(
        io="data/GIP_analyse van de jaarrekening_Stevens_Hannelore.xlsx",
        engine="openpyxl",
        sheet_name="Solvabiliteit",
        usecols="A:D",
        nrows=40,
        skiprows=1
    )

    # change column names
    df.columns = ["Type","Boekjaar 1","Boekjaar 2","Boekjaar 3"]
    # filter row on column value
    sol = ["Solvabiliteit"]
    df = df[df["Type"].isin(sol)]

    df = df.T #Transponeren
    df = df.rename(index={"Boekjaar 1":"1","Boekjaar 2":"2",
                    "Boekjaar 3":"3"})
    df = df.iloc[1: , :] # Drop first row 
    df.insert(0,"Boekjaar",["Boekjaar 1","Boekjaar 2",
                    "Boekjaar 3"],True)
    df.columns = ["Boekjaar","Solvabiliteit"] # change column names
    
    
    return df

df_solvabiliteit = get_solvabiliteit_from_excel()


# ---- READ EXCEL RENTABILITEIT ----
@st.cache
def get_rev_from_excel():
    df = pd.read_excel(
        io="data/GIP_analyse van de jaarrekening_Stevens_Hannelore.xlsx",
        engine="openpyxl",
        sheet_name="REV",
        usecols="A:D",
        nrows=20,
        skiprows=1
    )

    # change column names
    df.columns = ["Type","Boekjaar 1","Boekjaar 2","Boekjaar 3"]
    # filter row on column value
    rev = ["REV"]
    df = df[df["Type"].isin(rev)]

    df = df.T #Transponeren
    df = df.rename(index={"Boekjaar 1":"1","Boekjaar 2":"2",
                    "Boekjaar 3":"3"})
    df = df.iloc[1: , :] # Drop first row 
    df.insert(0,"Boekjaar",["Boekjaar 1","Boekjaar 2",
                    "Boekjaar 3"],True)
    df.columns = ["Boekjaar","REV"] # change column names
    
    
    return df

df_rev = get_rev_from_excel()


# ---- READ EXCEL VOORRAAD----
@st.cache
def get_voorraad_from_excel():
    df = pd.read_excel(
        io="data/GIP_analyse van de jaarrekening_Stevens_Hannelore.xlsx",
        engine="openpyxl",
        sheet_name="Voorraad",
        usecols="A:D",
        nrows=40
    )

    # change column names
    df.columns = ["Type","Boekjaar 1","Boekjaar 2","Boekjaar 3"]
    # filter row on column value
    omlooptijd = ["Omlooptijd","Omloopsnelheid voorraden"]
    df = df[df["Type"].isin(omlooptijd)]

    df = df.T #Transponeren
    df = df.rename(index={"Boekjaar 1":"1","Boekjaar 2":"2",
                    "Boekjaar 3":"3"})
    df = df.iloc[1: , :] # Drop first row 
    df.insert(0,"Boekjaar",["Boekjaar 1","Boekjaar 2",
                    "Boekjaar 3"],True)
    df.columns = ["Boekjaar","Omlooptijd","Omloopsnelheid"] # change column names
    
    
    return df

df_omlooptijd = get_voorraad_from_excel()

# ---- READ EXCEL Klanten- en Leverancierskrediet----
@st.cache
def get_klantlev_from_excel():
    df = pd.read_excel(
        io="data/GIP_analyse van de jaarrekening_Stevens_Hannelore.xlsx",
        engine="openpyxl",
        sheet_name="KlantLevKrediet",
        usecols="A:D",
        nrows=40
    )

    # change column names
    df.columns = ["Klantenkrediet","Leverancierskrediet","Boekjaar 1","Boekjaar 2","Boekjaar 3"]
    # filter row on column value
    krediet = ["Klantenkrediet","Leverancierskrediet"]
    df = df.astype({'Klantenkrediet': 'float64','Leverancierskrediet': 'float64'})
    df = df[df["Type"].isin(krediet)]

    df = df.T #Transponeren
    df = df.rename(index={"Boekjaar 1":"1","Boekjaar 2":"2",
                    "Boekjaar 3":"3"})
    df = df.iloc[1: , :] # Drop first row 
    df.insert(0,"Boekjaar",["Boekjaar 1","Boekjaar 2",
                    "Boekjaar 3"],True)
    df.columns = ["Boekjaar","Klantenkrediet","Leverancierskrediet"] # change column names
    
    
    return df

df_klantlev = get_klantlev_from_excel()

# ---- SIDEBAR ----
st.sidebar.header("Gelieve hier te filteren:")
boekjaar = st.sidebar.radio(
    "Selecteer boekjaar:",
    ("Boekjaar 1","Boekjaar 2","Boekjaar 3"),
    index=0
)

# ---- MAINPAGE ----
st.title(":bar_chart: Dashboard Dritto")
st.markdown("##")

st.write(df_liquiditeit)
# Samenstelling activa boekjaar [TAART DIAGRAM]
fig = px.line(df_liquiditeit, x="Boekjaar", y=["Liquiditeit in ruime zin", "Liquiditeit in enge zin"], markers=True)
fig.update_layout({
'plot_bgcolor': 'rgba(0, 0, 0, 0)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)',})

fig.update_traces(line=dict(width=3))
st.plotly_chart(fig, use_container_width=True)

# rentabiliteit eigen vermogen boekjaar [TAART DIAGRAM]
st.write(df_rev)
fig = px.line(df_rev, x="Boekjaar", y="REV", markers=True)
fig.update_layout({
'plot_bgcolor': 'rgba(0, 0, 0, 0)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)',})

fig.update_traces(line=dict(width=3))
st.plotly_chart(fig, use_container_width=True)


# solvabiliteit boekjaar [TAART DIAGRAM]
st.write(df_solvabiliteit)
fig = px.line(df_solvabiliteit, x="Boekjaar", y="Solvabiliteit", markers=True)
fig.update_layout({
'plot_bgcolor': 'rgba(0, 0, 0, 0)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)',})

fig.update_traces(line=dict(width=3))
st.plotly_chart(fig, use_container_width=True)

#omlooptijd voorraden [STAAFDIAGRAM]
st.write(df_omlooptijd)

#klanten- en leverancierskrediet [staafdiagram]
st.write(df_klantlev)
#x=["Klantenkrediet","Leverancierskrediet"]
fig = px.bar(df_klantlev, x=["Klantenkrediet","Leverancierskrediet"], y="Boekjaar", orientation="h", barmode="group",title="Klant-en Leverancierskrediet")
fig.update_traces()
fig.update_layout({
'plot_bgcolor': 'rgba(0, 0, 0, 0)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)',})

#fig.update_traces(base=dict(width=3))
st.plotly_chart(fig, use_container_width=True)

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)