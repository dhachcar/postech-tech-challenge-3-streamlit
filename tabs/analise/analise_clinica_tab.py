import streamlit as st
from tabs.tab import TabInterface
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd


class AnaliseClinicaTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":blue[Análise clínica]", divider="blue")

            with st.container():
                st.markdown(
                    """
                    **:blue[Por sintoma]**
                """
                )

                df_total_por_sintoma = pd.read_csv(
                    "assets/segmentacoes/segmentacao-total-por-sintoma.csv"
                ).sort_values(by="total")

                df_total_sintomas_categorizado = pd.read_csv(
                    "assets/segmentacoes/segmentacao-agrupada-total-por-sintoma.csv"
                )

                # plot 1
                fig = go.Figure(
                    go.Bar(
                        x=df_total_por_sintoma.total.values.tolist(),
                        y=df_total_por_sintoma.sintoma.values.tolist(),
                        orientation="h",
                    )
                )
                fig.update_layout(
                    title="Segmentação dos entrevistados por tipo de sintoma",
                    xaxis_title="Número de indivíduos",
                    yaxis_title="Sintoma",
                    height=600,
                )

                st.plotly_chart(fig)

                # plot 2
                fig = px.treemap(
                    df_total_sintomas_categorizado,
                    path=[px.Constant("Todos"), "categoria", "sintoma"],
                    values="total",
                    custom_data=["total", "porcentagem"],
                )
                fig.update_layout(
                    title="Sintomas categorizados",
                    margin=dict(t=50, l=25, r=25, b=25),
                )
                fig.update_traces(
                    hovertemplate="<b>%{label}</b><br>Total: %{customdata[0]}<br>Porcentagem: %{customdata[1]:.2f}%",
                    texttemplate="<b>%{label}</b><br>%{customdata[1]:.2f}%",
                    hoverlabel=dict(font=dict(color="white")),
                    textposition="middle center",
                )

                st.plotly_chart(fig)

            with st.container():
                st.markdown(
                    """
                    **:blue[Segmentação de escolaridade X covid19 positivo]**
                """
                )

                df_escolaridade_covid = pd.read_csv(
                    "assets/segmentacoes/segmentacao-escolaridade-x-casos-positivos.csv"
                )

                col1, col2 = st.columns([1, 1])

                with col1:
                    fig = go.Figure()
                    fig.add_trace(
                        go.Pie(
                            labels=df_escolaridade_covid.nome,
                            values=df_escolaridade_covid.contagem,
                            hole=.65
                        )
                        )
                    fig.update_layout(title='Segmentação de plano de saúde X covid19 confirmada', width=500)
                    st.plotly_chart(fig)

                with col2:
                    st.image(
                        "assets/img/analise-segmentacao-escolaridade-x-covid-positivo.png",
                        caption="Gráfico de waffle",
                    )

            with st.container():
                st.markdown(
                    """
                    **:blue[Segmentação de plano de saúde X covid19 positivo]**
                """
                )

                df_plano_saude_covid = pd.read_csv(
                    "assets/segmentacoes/segmentacao-plano-saude-x-casos-positivos.csv"
                )

                col1, col2 = st.columns([1, 1])

                with col1:
                    fig = go.Figure()
                    fig.add_trace(
                        go.Pie(
                            labels=df_plano_saude_covid.nome,
                            values=df_plano_saude_covid.contagem,
                            hole=0.65,
                        )
                    )
                    fig.update_layout(
                        title="Segmentação de plano de saúde X covid19 confirmada",
                        width=500,
                    )
                    st.plotly_chart(fig)

                with col2:
                    st.image(
                        "assets/img/analise-segmentacao-plano-saude-x-covid-positivo.png",
                        caption="Gráfico de waffle",
                    )

            with st.container():
                st.markdown(
                    """
                    **:blue[Evolução dos casos positivos (mês a mês)]**
                """
                )

                st.markdown(
                    "Aqui foram utilizados queries que rodaram diretamente no BigQuery e foram consumidos através de um id de job"
                )

                st.image(
                    "assets/img/bigquery-evolucao-casos-mes-a-mes.png",
                    caption="TODO: Melhorar esta legenda",
                )
                st.image(
                    "assets/img/bigquery-evolucao-casos-mes-a-mes-por-uf.png",
                    caption="TODO: Melhorar esta legenda",
                )
