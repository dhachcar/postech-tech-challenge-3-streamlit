import streamlit as st
from tabs.tab import TabInterface
import plotly.graph_objs as go
import pandas as pd


class AnaliseCorrelacaoTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":blue[Matriz de correlação]", divider="blue")
            st.markdown(
                """
                A matriz de correlação apresentada a seguir, foi utilizada para verificar/validar a correlação dos dados escolhidos para o modelo KMeans, apresentado na próxima seção. 
            """, unsafe_allow_html=True
            )

            matriz_correlacao = pd.read_csv("assets/csv/correlacao-unsupervised.csv")

            # plot do heatmap (correlação)
            fig = go.Figure(
                data=go.Heatmap(
                    z=matriz_correlacao.values[::-1],
                    x=matriz_correlacao.columns,
                    y=matriz_correlacao.columns[::-1],
                    colorbar=dict(title="Correlação"),
                    colorscale="Viridis",
                    xgap=1,
                    ygap=1,
                )
            )

            fig.update_layout(title="Matriz de correlação", height=600, width=700)
            fig.update_layout(xaxis_side="top", xaxis=dict(tickangle=-45))

            st.plotly_chart(fig)


