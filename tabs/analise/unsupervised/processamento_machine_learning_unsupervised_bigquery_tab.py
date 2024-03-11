import streamlit as st
from tabs.tab import TabInterface


class AnaliseProcessamentoMachineLearningUnsupervisedBigqueryTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(
                ":blue[Modelo KMeans BigQuery]", divider="blue"
            )
            st.markdown(
                """
                TESTE
            """
            )

            st.image(
                "assets/img/bigquery-ml-1.png", caption="TODO: Melhorar esta legenda"
            )
            st.image(
                "assets/img/bigquery-ml-2.png", caption="TODO: Melhorar esta legenda"
            )
            st.image(
                "assets/img/bigquery-ml-3.png", caption="TODO: Melhorar esta legenda"
            )
