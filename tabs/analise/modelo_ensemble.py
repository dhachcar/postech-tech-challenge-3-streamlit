import streamlit as st
from tabs.tab import TabInterface
from tabs.analise.ensemble.correlacao_tab import AnaliseCorrelacaoTab
from tabs.analise.ensemble.processamento_machine_learning_ensemble_tab import AnaliseProcessamentoMachineLearningEnsembleTab

class AnaliseModeloEnsembleTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            tab0, tab1 = st.tabs(tabs=['Matriz de correlação', 'Modelo XGBoost'])

            AnaliseCorrelacaoTab(tab0)
            AnaliseProcessamentoMachineLearningEnsembleTab(tab1)