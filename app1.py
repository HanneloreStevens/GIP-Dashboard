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
    voorraad = ["Omlooptijd","Omloopsnelheid voorraden"]
    df = df[df["Type"].isin(voorraad)]

    df = df.T #Transponeren
    df = df.rename(index={"Boekjaar 1":"1","Boekjaar 2":"2",
                    "Boekjaar 3":"3"})
    df = df.iloc[1: , :] # Drop first row 
    df.insert(0,"Boekjaar",["Boekjaar 1","Boekjaar 2",
                    "Boekjaar 3"],True)
    df.columns = ["Boekjaar","Omlooptijd","Omloopsnelheid voorraden"] # change column names
    df = df.astype({'Omlooptijd': 'float64','Omloopsnelheid voorraden': 'float64'})
    
    
    return df

df_voorraad = get_voorraad_from_excel()

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
    df.columns = ["Type","Boekjaar 1","Boekjaar 2","Boekjaar 3"]
    # filter row on column value
    krediet = ["Klantenkrediet","Leverancierskrediet"]
    df = df[df["Type"].isin(krediet)]

    df = df.T #Transponeren
    df = df.rename(index={"Boekjaar 1":"1","Boekjaar 2":"2",
                    "Boekjaar 3":"3"})
    df = df.iloc[1: , :] # Drop first row 
    df.insert(0,"Boekjaar",["Boekjaar 1","Boekjaar 2",
                    "Boekjaar 3"],True)
    df.columns = ["Boekjaar","Klantenkrediet","Leverancierskrediet"] # change column names
    df = df.astype({'Klantenkrediet': 'float64','Leverancierskrediet': 'float64'})
    
    
    return df

df_klantlev = get_klantlev_from_excel()

# ---- SIDEBAR ----
#st.sidebar.color_picker()
st.sidebar.image("data/dritto logo.jpg")
st.sidebar.header("Gelieve hier te filteren:")
grafiek = st.sidebar.selectbox(
    "Selecteer ratio:",
    ("Kies een ratio","Liquiditeit","Rentabiliteit","Solvabiliteit","Omlooptijd en Omloopsnelheid voorraad","Klanten- en Leverancierskrediet"),
    #index=0
)


# ---- MAINPAGE ----
st.title(":bar_chart: Dashboard Dritto")
st.markdown("##")

if grafiek =="Kies een ratio":
    st.subheader("Dritto")
    st.image("data/dritto.png")
    
# Liquiditeit boekjaar [LIJNDIAGRAM]
elif grafiek == "Liquiditeit":
    st.header("Liquiditeit")
    st.write(df_liquiditeit)
    fig = px.line(df_liquiditeit, x="Boekjaar", y=["Liquiditeit in ruime zin", "Liquiditeit in enge zin"], markers=True)
    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',})
      
    fig.update_traces(line=dict(width=5))
    st.plotly_chart(fig, use_container_width=True)

    liq=st.sidebar.selectbox(
        "Filter tussen liquiditeit in ruime zin en liquiditeit in enge zin",
        ("Selecteer soort liquiditeit","Liquiditeit in ruime zin","Liquiditeit in enge zin"))

    
    if liq == "Liquiditeit in ruime zin":
        st.header("Liquiditeit in ruime zin")
        fig = px.line(df_liquiditeit, x="Boekjaar", y="Liquiditeit in ruime zin", markers=True)
        fig.update_layout({
            'plot_bgcolor': 'rgba(0, 0, 0, 0)',
         'paper_bgcolor': 'rgba(0, 0, 0, 0)',})
        fig.update_traces(line=dict(width=5))
        st.plotly_chart(fig, use_container_width=True)

    elif liq =="Liquiditeit in enge zin":
        st.header("Liquiditeit in enge zin")
        fig = px.line(df_liquiditeit, x="Boekjaar", y="Liquiditeit in enge zin", markers=True)
        fig.update_layout({
            'plot_bgcolor': 'rgba(0, 0, 0, 0)',
            'paper_bgcolor': 'rgba(0, 0, 0, 0)',})
        fig.update_traces(line=dict(width=5))
        st.plotly_chart(fig, use_container_width=True)
    
    else:
        ""

# rentabiliteit eigen vermogen boekjaar [LIJNDIAGRAM]
elif grafiek == "Rentabiliteit":
    st.header("Rentabiliteit")
    st.write(df_rev)
    fig = px.line(df_rev, x="Boekjaar", y="REV", markers=True)
    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',})

    fig.update_traces(line=dict(width=3))
    st.plotly_chart(fig, use_container_width=True)

# solvabiliteit boekjaar [LIJNDIAGRAM]
elif grafiek =="Solvabiliteit":
    st.header("Solvabiliteit")
    st.write(df_solvabiliteit)
    fig = px.line(df_solvabiliteit, x="Boekjaar", y="Solvabiliteit", markers=True)
    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',})
        
    fig.update_traces(line=dict(width=3))
    st.plotly_chart(fig, use_container_width=True)

#omlooptijd voorraden [STAAFDIAGRAM]
elif grafiek =="Omlooptijd en Omloopsnelheid voorraad":
    st.header("Omlooptijd en Omloopsnelheid")
    st.write(df_voorraad)
    fig = px.bar(df_voorraad, x=["Omlooptijd","Omloopsnelheid voorraden"], y="Boekjaar", orientation="h", barmode="group")
    fig.update_traces()
    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',})
    #fig.update_traces(base=dict(width=3))
    st.plotly_chart(fig, use_container_width=True)

    voorraad=st.sidebar.selectbox(
        "Filter tussen Omlooptijd en Omloopsnelheid",
        ("Selecteer soort voorraad","Omlooptijd","Omloopsnelheid"))
    
    if voorraad =="Omlooptijd":
        fig = px.bar(df_voorraad, x="Omlooptijd", y="Boekjaar", orientation="h", barmode="group")
        fig.update_traces()
        fig.update_layout({
            'plot_bgcolor': 'rgba(0, 0, 0, 0)',
            'paper_bgcolor': 'rgba(0, 0, 0, 0)',})
        #fig.update_traces(base=dict(width=3))
        st.plotly_chart(fig, use_container_width=True)
    
    elif voorraad =="Omloopsnelheid":
        fig = px.bar(df_voorraad, x="Omloopsnelheid voorraden", y="Boekjaar", orientation="h", barmode="group")
        fig.update_traces()
        fig.update_layout({
            'plot_bgcolor': 'rgba(0, 0, 0, 0)',
            'paper_bgcolor': 'rgba(0, 0, 0, 0)',})
        #fig.update_traces(base=dict(width=3))
        st.plotly_chart(fig, use_container_width=True)
    
    else:
        ""

#klanten- en leverancierskrediet [staafdiagram]
else:
    st.header("Klantenkrediet en Leverancierskrediet")
    st.write(df_klantlev)
    fig = px.bar(df_klantlev, x=["Klantenkrediet","Leverancierskrediet"], y="Boekjaar", orientation="h", barmode="group")
    fig.update_traces()
    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',})
    #fig.update_traces(base=dict(width=3))
    st.plotly_chart(fig, use_container_width=True)

    klantlev=st.sidebar.selectbox(
        "Filter tussen Klantenkrediet en Leverancierskrediet",
        ("Selecteer soort krediet","Klantenkrediet","Leverancierskrediet"))
    
    if klantlev =="Klantenkrediet":    
        fig = px.bar(df_klantlev, x="Klantenkrediet", y="Boekjaar", orientation="h", barmode="group")
        fig.update_traces()
        fig.update_layout({
            'plot_bgcolor': 'rgba(0, 0, 0, 0)',
            'paper_bgcolor': 'rgba(0, 0, 0, 0)',})
        #fig.update_traces(base=dict(width=3))
        st.plotly_chart(fig, use_container_width=True)

    elif klantlev =="Leverancierskrediet":
        fig = px.bar(df_klantlev, x="Leverancierskrediet", y="Boekjaar", orientation="h", barmode="group")
        fig.update_traces()
        fig.update_layout({
            'plot_bgcolor': 'rgba(0, 0, 0, 0)',
            'paper_bgcolor': 'rgba(0, 0, 0, 0)',})
        #fig.update_traces(base=dict(width=3))
        st.plotly_chart(fig, use_container_width=True)
    
    else:
        ""
    
# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)