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
                Na análise da matriz de correlação dos sintomas da COVID-19, é evidente a relação entre eles, como tosse, febre e falta de ar, sugerindo ocorrência simultânea. Essa clareza é crucial para identificação precoce, diagnóstico e tratamento, além de priorização de recursos médicos e implementação de medidas preventivas.
            """
            )

            matriz_correlacao = pd.read_csv("assets/csv/correlacao.csv")

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

            fig.update_layout(title="Matriz de correlação", height=1200, width=1200)
            fig.update_layout(xaxis_side="top", xaxis=dict(tickangle=-45))

            st.plotly_chart(fig)

            st.markdown(
                """
                A matriz de correlação será utilizada para feature engineering dos modelos de machine learning nas próximas seções. Ela identifica e mensura os relacionamentos entre as colunas do conjunto de dados (principalmente entre os sintomas da COVID-19), o que possibilita criarmos modelos mais assertivos.\n
                Portanto, analisando o seu resultado, é possível confirmar que :blue[todos os sintomas estão altamente correlacionados] uns aos outros, o que indica que são colunas importantes para considerar durante o treinamento dos modelos.
            """
            )
