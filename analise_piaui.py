import streamlit as st
import pandas as pd
import plotly.express as px

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Violência Contra a Mulher no Piauí",
    page_icon="📊",
    layout="wide"
)

# TÍTULO
st.title("📊 Dashboard - Violência Contra a Mulher no Piauí")
st.markdown("Análise de indicadores de violência de gênero no estado do Piauí.")

# LEITURA DO EXCEL
df = pd.read_excel("violencia_mulher_piaui.xlsx")

# SIDEBAR
st.sidebar.header("Filtros")

anos = st.sidebar.multiselect(
    "Selecione os anos",
    options=df["Ano"].unique(),
    default=df["Ano"].unique()
)

cidades = st.sidebar.multiselect(
    "Selecione as cidades",
    options=df["Cidade"].unique(),
    default=df["Cidade"].unique()
)

# FILTRO
df_filtrado = df[
    (df["Ano"].isin(anos)) &
    (df["Cidade"].isin(cidades))
]

# MÉTRICAS
total_feminicidios = df_filtrado["Feminicidios"].sum()
total_violencia = df_filtrado["Violencia_Domestica"].sum()
total_medidas = df_filtrado["Medidas_Protetivas"].sum()

col1, col2, col3 = st.columns(3)

col1.metric("Total de Feminicídios", total_feminicidios)
col2.metric("Casos de Violência Doméstica", total_violencia)
col3.metric("Medidas Protetivas", total_medidas)

st.divider()

# GRÁFICO 1 - FEMINICÍDIOS POR ANO
graf1 = px.bar(
    df_filtrado.groupby("Ano")["Feminicidios"].sum().reset_index(),
    x="Ano",
    y="Feminicidios",
    color="Feminicidios",
    title="Feminicídios por Ano",
    text_auto=True
)

st.plotly_chart(graf1, use_container_width=True)

# GRÁFICO 2 - VIOLÊNCIA DOMÉSTICA POR CIDADE
graf2 = px.pie(
    df_filtrado,
    names="Cidade",
    values="Violencia_Domestica",
    title="Distribuição da Violência Doméstica por Cidade"
)

st.plotly_chart(graf2, use_container_width=True)

# GRÁFICO 3 - DENÚNCIAS 180
graf3 = px.line(
    df_filtrado.groupby("Ano")["Denuncias_180"].sum().reset_index(),
    x="Ano",
    y="Denuncias_180",
    markers=True,
    title="Evolução das Denúncias - Ligue 180"
)

st.plotly_chart(graf3, use_container_width=True)

# GRÁFICO 4 - BOLETINS DE OCORRÊNCIA
graf4 = px.area(
    df_filtrado.groupby("Ano")["BO_Registrados"].sum().reset_index(),
    x="Ano",
    y="BO_Registrados",
    title="Boletins de Ocorrência Registrados"
)

st.plotly_chart(graf4, use_container_width=True)

# TABELA
st.subheader("📋 Dados Utilizados")

st.dataframe(df_filtrado)

# RODAPÉ
st.markdown("---")
st.caption("Fonte: SSP-PI, SEMPI e Observatório da Mulher Piauiense.")
