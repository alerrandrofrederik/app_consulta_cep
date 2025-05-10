
import requests
import pandas as pd
import streamlit as st


st.title('Consulta de CEP')
cep = st.text_input('Digite o CEP')


url = "http://viacep.com.br/ws/{cep}/json/"
response = requests.get(url.format(cep=cep))
if response.status_code == 200:
    dados = response.json()
    st.write(dados)

