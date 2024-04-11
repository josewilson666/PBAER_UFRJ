import streamlit as st
import pandas as pd

# Título do aplicativo
st.title('PBAER')

with st.container():
    st.subheader("Teste com o Streamlit")
    st.title("Dashboard do Projeto ")

@st.cache_data
def carregar_dados():
    tabela = pd.read_excel('Media_EVA_RET_SUC_por_CENTRO.xlsx')
    return tabela

with st.container():
    st.write("---")
    centros = st.selectbox("Selecione o CENTRO", ['CCMN','CT'])
    dados = carregar_dados() 
    dados = dados.loc[dados.CENTRO == centros].copy()
    st.scatter_chart(dados, x="CO_ANO", y="EVASAO")
