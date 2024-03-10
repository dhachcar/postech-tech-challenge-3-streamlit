import streamlit as st
from tabs.analise.modelo_ensemble import AnaliseModeloEnsembleTab
from tabs.analise.modelo_unsupervised import AnaliseModeloUnsupervisedTab
from util.layout import output_layout
from tabs.analise.analise_clinica_tab import AnaliseClinicaTab
from tabs.analise.analise_demografica_tab import AnaliseDemograficaTab

st.set_page_config(
    page_title="Explorações, descobertas e análises | Tech Challenge 3 | FIAP",
    layout="wide",
)
output_layout()

with st.container():
    st.header(":orange[Explorações, descobertas e análises]")

    tab0, tab1, tab2, tab3 = st.tabs(
        tabs=[
            "Análise demográfica",
            "Análise clínica",
            "Machine Learning: Ensemble",
            "Machine Learning: Não-supervisionado",
        ]
    )

    AnaliseDemograficaTab(tab0)
    AnaliseClinicaTab(tab1)
    AnaliseModeloEnsembleTab(tab2)
    AnaliseModeloUnsupervisedTab(tab3)
