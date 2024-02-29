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
                    "A query foi executada dentro do BigQuery, o que criou um job id. Posteriormente, este job id foi consumido dentro do Colabs."
                )

                st.image(
                    "assets/img/bigquery-evolucao-casos-mes-a-mes.png",
                    caption="Query utilizada pelo job, dentro do BigQuery",
                )

                df_casos_positivos_mes_a_mes = pd.read_csv(
                    "assets/segmentacoes/evolucao-casos-positivos-mes-a-mes.csv"
                )

                fig = go.Figure(
                    go.Bar(
                        x=df_casos_positivos_mes_a_mes.mes_label,
                        y=df_casos_positivos_mes_a_mes.total,
                        name="Meses",
                    )
                )
                fig.add_trace(
                    go.Scatter(
                        x=df_casos_positivos_mes_a_mes.mes_label,
                        y=df_casos_positivos_mes_a_mes.total,
                        mode="lines",
                        name="Tendência",
                    )
                )
                fig.update_layout(
                    title="Evolução dos casos positivos nos últimos 3 meses",
                    xaxis_title="Mês",
                    yaxis_title="Número de casos positivos",
                )

                st.plotly_chart(fig)

            with st.container():
                st.markdown(
                    """
                    **:blue[Evolução dos casos positivos (mês a mês e UF)]**
                """
                )
                st.image(
                    "assets/img/bigquery-evolucao-casos-mes-a-mes-por-uf.png",
                    caption="Query utilizada pelo job, dentro do BigQuery",
                )

                df_casos_positivos_mes_a_mes_por_uf = pd.read_csv(
                    "assets/segmentacoes/evolucao-casos-positivos-mes-a-mes-por-uf.csv"
                )

                # quantidade de cores únicas
                num_colors = len(df_casos_positivos_mes_a_mes_por_uf["estado"].unique())
                # cor final
                colors = [
                    f"hsl({h}, 50%, 50%)" for h in range(0, 320, int(320 / num_colors))
                ]

                # plottando o gráfico
                fig = go.Figure()

                for i, state in enumerate(
                    df_casos_positivos_mes_a_mes_por_uf["estado"].unique()
                ):
                    state_data = df_casos_positivos_mes_a_mes_por_uf[
                        df_casos_positivos_mes_a_mes_por_uf["estado"] == state
                    ]
                    fig.add_trace(
                        go.Bar(
                            x=state_data["mes"],
                            y=state_data["total_casos_confirmados"],
                            name=state,
                            marker_color=colors[i],
                        )
                    )

                fig.update_layout(
                    title="Evolução dos casos positivos nos últimos 3 meses, agrupado por UF",
                    xaxis=dict(title="Mês"),
                    yaxis=dict(title="Total de casos confirmados"),
                    barmode="group",
                    width=1000,
                    height=600,
                )

                st.plotly_chart(fig)
