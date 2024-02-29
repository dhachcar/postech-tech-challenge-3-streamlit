import streamlit as st
from tabs.analise.correlacao_tab import AnaliseCorrelacaoTab
from util.layout import output_layout
from tabs.analise.analise_clinica_tab import AnaliseClinicaTab
from tabs.analise.analise_demografica_tab import AnaliseDemograficaTab
from tabs.analise.processamento_machine_learning_ensemble_tab import AnaliseProcessamentoMachineLearningEnsembleTab
from tabs.analise.processamento_machine_learning_unsupervised_tab import AnaliseProcessamentoMachineLearningUnsupervisedTab
from tabs.analise.processamento_machine_learning_unsupervised_bigquery_tab import AnaliseProcessamentoMachineLearningUnsupervisedBigqueryTab

st.set_page_config(page_title="Explorações, descobertas e análises | Tech Challenge 3 | FIAP", layout='wide')
output_layout()

with st.container():
    st.header(':orange[Explorações, descobertas e análises]')

    tab0, tab1, tab2, tab3, tab4, tab5 = st.tabs(tabs=['Análise demográfica', 'Análise clínica', 'Correlação', 'Machine Learning: Ensemble', 'Machine Learning: Não-supervisionado', 'Machine Learning: Não-supervisionado no BigQuery'])

    AnaliseDemograficaTab(tab0)
    AnaliseClinicaTab(tab1)
    AnaliseCorrelacaoTab(tab2)
    AnaliseProcessamentoMachineLearningEnsembleTab(tab3)
    AnaliseProcessamentoMachineLearningUnsupervisedTab(tab4)
    AnaliseProcessamentoMachineLearningUnsupervisedBigqueryTab(tab5)