import streamlit as st
from tabs.tab import TabInterface
import plotly.graph_objs as go
import pandas as pd

class AnaliseDemograficaTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":blue[Análise demográfica]", divider="blue")

            with st.container():
                st.markdown(
                    """
                    **:blue[Indicadores gerais]**
                """
                )

                indicadores_gerais = pd.read_csv("assets/csv/indicadores.csv")

                with st.container():
                    _, col1, col2, _ = st.columns([3, 2, 2, 3])

                    with col1:
                        st.metric(
                            label="Total de entrevistados",
                            value='{:.2f}'.format(indicadores_gerais.total_entrevistados.values[0]),
                            delta='{:.2f}%'.format(100),
                            delta_color="off",
                        )

                    with col2:
                        st.metric(
                            label="Média de idade",
                            value='{:.0f} anos'.format(indicadores_gerais.idade_media.values[0].round(0)),
                            delta='{:.2f}%'.format(100),
                            delta_color="off",
                        )

            with st.container():
                st.markdown(
                    """
                    **:blue[Por sexo]**
                """
                )

                sexo_cores = ["#983D3D", "#232066"]
                df_pnad_sexo = pd.read_csv("assets/csv/segmentacao-sexo.csv")

                col1, col2 = st.columns([1, 1])

                with col1:
                    fig = go.Figure()
                    fig.add_trace(
                        go.Pie(
                            labels=df_pnad_sexo.nome,
                            values=df_pnad_sexo.total,
                            hole=0.65,
                            marker=dict(colors=sexo_cores),
                        )
                    )
                    fig.update_layout(
                        title="Segmentação dos entrevistados por sexo", width=500
                    )
                    st.plotly_chart(fig)

                with col2:
                    st.image(
                        "assets/img/analise-segmentacao-sexo-1.png",
                        caption="Gráfico de waffle",
                    )

            with st.container():
                st.markdown(
                    """
                    **:blue[Por UF]**
                """
                )

                df_pnad_uf = pd.read_csv("assets/csv/segmentacao-uf.csv")

                fig = go.Figure()
                fig.add_trace(
                    go.Bar(x=df_pnad_uf.nome.tolist(), y=df_pnad_uf.total.tolist())
                )
                fig.update_layout(title="Segmentação dos entrevistados por UF")
                fig.update_layout(xaxis=dict(tickangle=-45))
                st.plotly_chart(fig)

            with st.container():
                st.markdown(
                    """
                    **:blue[Por região metropolitana]**
                """
                )

                df_pnad_regiao_metropolitana = pd.read_csv(
                    "assets/csv/segmentacao-regiao-metropolitana.csv"
                )

                fig = go.Figure()
                fig.add_trace(
                    go.Bar(
                        x=df_pnad_regiao_metropolitana.nome.tolist(),
                        y=df_pnad_regiao_metropolitana.total.tolist(),
                    )
                )
                fig.update_layout(
                    title="Segmentação dos entrevistados por região metropolitana",
                    height=800,
                )
                fig.update_layout(xaxis=dict(tickangle=-45))
                st.plotly_chart(fig)

            with st.container():
                st.markdown(
                    """
                    **:blue[Por escolaridade]**
                """
                )

                df_pnad_escolaridade = pd.read_csv(
                    "assets/csv/segmentacao-escolaridade.csv"
                )

                col1, _, col2 = st.columns([0.4, 0.1, 0.5])

                with col1:
                    fig = go.Figure()
                    fig.add_trace(
                        go.Bar(
                            x=df_pnad_escolaridade.nome.tolist(),
                            y=df_pnad_escolaridade.total.tolist(),
                        )
                    )
                    fig.update_layout(
                        title="Segmentação dos entrevistados por escolaridade"
                    )
                    fig.update_layout(xaxis=dict(tickangle=-45), width=600)
                    st.plotly_chart(fig)

                with col2:
                    st.image(
                        "assets/img/analise-segmentacao-escolaridade-1.png",
                        caption="Gráfico de waffle",
                    )

            with st.container():
                st.markdown(
                    """
                    **:blue[Por faixa etária]**
                """
                )

                df_pnad_idade = pd.read_csv("assets/csv/segmentacao-idade.csv")
                faixas_etarias = df_pnad_idade.nome.values.astype(str)
                populacao = df_pnad_idade.total.values

                fig = go.Figure(go.Bar(x=populacao, y=faixas_etarias, orientation="h"))

                fig.update_layout(
                    title="Segmentação dos entrevistados por faixa etária",
                    xaxis_title="Número de indivíduos",
                    yaxis_title="Faixas etárias",
                    height=400,
                    width=600,
                )

                st.plotly_chart(fig)

            with st.container():
                st.markdown(
                    """
                    **:blue[Por plano de saúde]**
                """
                )

                df_pnad_plano_saude = pd.read_csv(
                    "assets/csv/segmentacao-plano-saude.csv"
                )

                col1, _, col2 = st.columns([0.4, 0.1, 0.5])

                with col1:
                    fig = go.Figure()
                    fig.add_trace(
                        go.Pie(
                            labels=df_pnad_plano_saude.nome,
                            values=df_pnad_plano_saude.total,
                            hole=0.65,
                        )
                    )
                    fig.update_layout(
                        title="Segmentação dos entrevistados por plano de saúde",
                        width=500,
                    )
                    st.plotly_chart(fig)

                with col2:
                    st.image(
                        "assets/img/analise-segmentacao-plano-saude-1.png",
                        caption="Gráfico de waffle",
                    )