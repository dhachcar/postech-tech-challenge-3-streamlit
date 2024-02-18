import streamlit as st
from util.layout import output_layout
from tabs.analise.analise_clinica_tab import AnaliseClinicaTab
from tabs.analise.analise_demografica_tab import AnaliseDemograficaTab
from tabs.analise.processamento_machine_learning_tab import AnaliseProcessamentoMachineLearningTab

st.set_page_config(page_title="Explorações, descobertas e análises | Tech Challenge 3 | FIAP", layout='wide')
output_layout()

with st.container():
    st.header(':orange[Explorações, descobertas e análises]')

    tab0, tab1, tab2 = st.tabs(tabs=['Análise demográfica', 'Análise clínica', 'Machine Learning'])

    AnaliseDemograficaTab(tab0)
    AnaliseClinicaTab(tab1)
    AnaliseProcessamentoMachineLearningTab(tab2)