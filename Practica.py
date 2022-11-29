import plotly.express as px
import pandas as pd
dfVel = pd.read_excel("https://github.com/tomasmcaceres98/StreamlitParcial1/blob/main/ARCHIVO.xlsx?raw=true")
import plotly.figure_factory as ff
import numpy as np
import streamlit as st
dfVel.rename(columns={'BITACORA DE MEDICIÓN DEL SERVICIO DE INTERNET':'Fecha','Unnamed: 1':'Hora','Unnamed: 2':'Download','Unnamed: 3':'Upload'},inplace=True)
dfVel.drop([0],inplace=True)
st.title("Datos iniciales")
dfVel
dfVel.head()
dfDatos = pd.DataFrame()
dfDatos = dfVel[["Fecha","Hora","Download","Upload"]]
dfDatos['Fecha'].unique()
st.title("Correciones de registro de fechas")
dfDatos[dfDatos["Fecha"]=='21/022022']
dfDatos.at[27,'Fecha']='2022/02/21'
dfDatos[dfDatos["Fecha"]=='02/032022']
dfDatos.at[37,'Fecha']='2022/03/02'
dfDatos[dfDatos["Fecha"]=='07/09/2022']
dfDatos[dfDatos["Download"]=='62.25']
dfDatos['Fecha'].unique()
dfDatos[dfDatos["Fecha"]=='07/09/2022']
dfDatos.at[109,'Fecha']='2022/09/07'
formato = '%Y/%m/%d'
dfDatos['Fecha'] = pd.to_datetime(dfDatos['Fecha'],format=formato)
st.title("Corrigiendo dato de Download")
dfDatos.at[109,'Download'] = 62.25
dfDatos['Download'] = pd.to_numeric(dfDatos['Download'])
dfDatos['Upload'] = pd.to_numeric(dfDatos['Upload'])
dfNuevo = dfDatos.groupby(dfDatos["Fecha"])[["Download","Upload"]].mean()
dfNuevo
st.title("Velocidad promedio de bajada de internet")
fig1=px.bar(dfNuevo,x=dfNuevo.index,y="Download", title="Velocidad Promedio de Internet")
st.plotly_chart(fig1, use_container_width=True)
st.title("Velocidad promedio de subida de internet")
fig2=px.line(dfNuevo,x=dfNuevo.index,y="Upload", title="Velocidad Promedio de Internet",markers=True)
st.plotly_chart(fig2, use_container_width=True)
st.title("Comparación de subida y bajada")
fig1.add_scatter(x=dfNuevo.index,y=dfNuevo['Upload'])
st.plotly_chart(fig1, use_container_width=True)



