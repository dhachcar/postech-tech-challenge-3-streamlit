import streamlit as st
from tabs.tab import TabInterface
import joblib
import pandas as pd


class AnaliseProcessamentoMachineLearningUnsupervisedTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":blue[Machine Learning: Unsupervised]", divider="blue")
            st.markdown(
                """
                
            """
            )

            # TODO: mostrar um grafico dos grupos (plotly ou img?)

            kmeans = joblib.load('/assets/modelos/unsupervised/kmeans.pkl')
            scaler = joblib.load('/assets/modelos/unsupervised/scaler.pkl')
            pca = joblib.load('/assets/modelos/unsupervised/pca.pkl')


