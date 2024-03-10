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
                A matriz de correlação apresentada a seguir, foi utilizada para feature engineering dos modelos de machine learning Ensemble da próxima seção. Ela identifica e mensura os relacionamentos entre as colunas do conjunto de dados (principalmente entre os sintomas da COVID-19), o que possibilita criarmos modelos mais assertivos.\n
                Seguindo em frente e analisando o resultado da matriz de correlação dos entrevistados da PNAD 2020, é evidente a :blue[alta correlação] entre as colunas de sintomas, como tosse, febre e falta de ar, sugerindo ocorrência simultânea. Essa clareza é crucial para identificação precoce, diagnóstico e tratamento, além de priorização de recursos médicos e implementação de medidas preventivas.
                Outras colunas que demonstram uma correlação significativa são aquelas referentes à "Medida de restrição" e ao "Plano de saúde". Essa associação é plausível, dado que estão ligadas aos sintomas &ndash; por exemplo &ndash; um entrevistado que se manteve em completo isolamento provavelmente teve uma incidência menor de sintomas, e vice-versa.\n
                Obviamente, também temos uma alta correlação entre as colunas "Estado", "Capial" e "Região metropolitana", já que são posições geográficas e uma está sempre relacionada à outra.
            """, unsafe_allow_html=True
            )

            matriz_correlacao = pd.read_csv("assets/csv/correlacao-ensemble.csv")

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

            fig.update_layout(title="Matriz de correlação", height=1024, width=1024)
            fig.update_layout(xaxis_side="top", xaxis=dict(tickangle=-45))

            st.plotly_chart(fig)


