import streamlit as st
import pandas as pd
import plotly.express as px

# CONFIGURAÇÃO
st.set_page_config(page_title="Violência Contra a Mulher", layout="wide")

st.title("📊 Violência Contra a Mulher no Piauí")

# LER O EXCEL
df = pd.read_excel("violencia_mulher_piaui.xlsx")

# MOSTRAR NOMES DAS COLUNAS
st.write("Colunas do Excel:")
st.write(df.columns)

# CORRIGIR NOMES DAS COLUNAS
df.columns = [
    "Ano",
    "Cidade",
    "Feminicidios",
    "Violencia_Domestica",
    "Medidas_Protetivas",
    "Denuncias_180",
    "BO_Registrados"
]

# FILTRO
anos = st.sidebar.multiselect(
    "Selecione o ano",
    df["Ano"].unique(),
    default=df["Ano"].unique()
)

df_filtrado = df[df["Ano"].isin(anos)]

# MÉTRICAS
total_violencia = df_filtrado["Violencia_Domestica"].sum()

st.metric("Total de Violência Doméstica", total_violencia)

# GRÁFICO
grafico = px.bar(
    df_filtrado,
    x="Cidade",
    y="Violencia_Domestica",
    color="Cidade",
    title="Violência Doméstica por Cidade"
)

st.plotly_chart(grafico, use_container_width=True)

