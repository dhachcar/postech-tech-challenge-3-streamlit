import streamlit as st
from tabs.analise.unsupervised.correlacao_tab import AnaliseCorrelacaoTab
from tabs.analise.unsupervised.processamento_machine_learning_unsupervised_bigquery_tab import (
    AnaliseProcessamentoMachineLearningUnsupervisedBigqueryTab,
)
from tabs.analise.unsupervised.processamento_machine_learning_unsupervised_tab import (
    AnaliseProcessamentoMachineLearningUnsupervisedTab,
)
from tabs.tab import TabInterface


class AnaliseModeloUnsupervisedTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            tab0, tab1, tab2 = st.tabs(
                tabs=["Matriz de correlação", "Modelo KMeans", "Modelo KMeans (BigQuery)"]
            )

            AnaliseCorrelacaoTab(tab0)
            AnaliseProcessamentoMachineLearningUnsupervisedTab(tab1)
            AnaliseProcessamentoMachineLearningUnsupervisedBigqueryTab(tab2)
