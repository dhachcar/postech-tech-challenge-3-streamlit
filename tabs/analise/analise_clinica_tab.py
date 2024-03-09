import streamlit as st
from tabs.tab import TabInterface
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
from util.layout import format_number


class AnaliseClinicaTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":blue[Análise clínica]", divider="blue")

            st.markdown(
                """
                Ao longo desta seção, analisamos como os entrevistados estão distribuídos em relação ao conjunto total de dados estudados, agora com foco no quésito **:blue[clínico]**.\n
                Logo na primeira parte, são apresentados os indicadores gerais da análise clínica. Tais indicadores foram divididos em 2 categorias:
                * A primeira categoria considera todos os entrevistados, independente do resultado de seu exame
                * A segunda categoria considera todos os entrevistados que tiveram algum resultado em seu exame

                Isto foi feito para melhorar a visualização das porcentagens de entrevistados infectados e não infectados.
            """
            )

            with st.container():
                st.markdown(
                    """
                    **:blue[Indicadores gerais]**\n
                """
                )

                indicadores_gerais = pd.read_csv("assets/csv/indicadores.csv")
                total_positivos = indicadores_gerais.total_casos_positivos.values[0]

                with st.container():
                    col1_raiz, col2_raiz = st.columns([1, 1])

                    with col1_raiz:
                        st.subheader(':blue[Todos independente do resultado]', divider="blue")

                        with st.container():
                            st.metric(
                                label="Total de entrevistados",
                                value=format_number(
                                    indicadores_gerais.total_entrevistados.values
                                ),
                                delta=format_number(100, "%0.2f") + "%",
                                delta_color="off",
                            )

                        with st.container():
                            col1, col2, _ = st.columns([1, 1, 1])

                            with col1:
                                st.metric(
                                    label="Casos COVID-19 positivos",
                                    value=format_number(
                                        indicadores_gerais.total_casos_positivos.values[
                                            0
                                        ]
                                    ),
                                    delta=format_number(
                                        indicadores_gerais.porcentagem_total_casos_positivos.values,
                                        "%0.2f",
                                    )
                                    + "%",
                                )

                            with col2:
                                st.metric(
                                    label="Casos COVID-19 negativos",
                                    value=format_number(
                                        indicadores_gerais.total_casos_negativos.values
                                    ),
                                    delta=format_number(
                                        indicadores_gerais.porcentagem_total_casos_negativos.values,
                                        "%0.2f",
                                    )
                                    + "%",
                                )

                    with col2_raiz:
                        st.subheader(':blue[Todos com resultado não ignorado]', divider="blue")

                        with st.container():
                            st.metric(
                                label="Total de entrevistados",
                                value=format_number(
                                    indicadores_gerais.total_casos_negativos_nao_ignorados.values + indicadores_gerais.total_casos_positivos_nao_ignorados.values
                                ),
                                delta=format_number(100, "%0.2f") + "%",
                                delta_color="off",
                            )

                        with st.container():
                            col1, col2, _ = st.columns([1, 1, 1])

                            with col1:
                                st.metric(
                                    label="Casos COVID-19 positivos",
                                    value=format_number(
                                        indicadores_gerais.total_casos_positivos_nao_ignorados.values
                                    ),
                                    delta=format_number(
                                        indicadores_gerais.porcentagem_total_casos_positivos_nao_ignorados.values,
                                        "%0.2f",
                                    )
                                    + "%",
                                )

                            with col2:
                                st.metric(
                                    label="Casos COVID-19 negativos",
                                    value=format_number(
                                        indicadores_gerais.total_casos_negativos_nao_ignorados.values
                                    ),
                                    delta=format_number(
                                        indicadores_gerais.porcentagem_total_casos_negativos_nao_ignorados.values,
                                        "%0.2f",
                                    )
                                    + "%",
                                )

            with st.container():
                df_total_por_sintoma = pd.read_csv(
                    "assets/csv/segmentacao-total-por-sintoma.csv"
                ).sort_values(by="total")

                df_total_sintomas_categorizado = pd.read_csv(
                    "assets/csv/segmentacao-agrupada-total-por-sintoma.csv"
                )

                df_sintomas_sorted = df_total_por_sintoma.sort_values(
                    by=["total"], ascending=False
                )
                top1_sintoma = df_sintomas_sorted.iloc[0]
                top2_sintoma = df_sintomas_sorted.iloc[1]
                top3_sintoma = df_sintomas_sorted.iloc[2]
                porcentagem_total_top1_sintoma = (
                    (top1_sintoma["total"] / total_positivos) * 100
                ).round(2)
                porcentagem_total_top2_sintoma = (
                    (top2_sintoma["total"] / total_positivos) * 100
                ).round(2)
                porcentagem_total_top3_sintoma = (
                    (top3_sintoma["total"] / total_positivos) * 100
                ).round(2)

                st.markdown(
                    f"""
                    **:blue[Por sintoma]**\n
                    Neste tópico, analisamos a distribuição de sintomas pelos entrevistados. Os sintomas foram considerados de todos os entrevistados, independentemente da confirmação clínica da COVID-19. Nesta primeira parte, é apresentado os sintomas mais comuns entre os entrevistados. Assim, conforme abaixo, é possível visualizar que as principais complicações foram:
                    * **\"{top1_sintoma['sintoma']}\"** com :blue[{format_number(top1_sintoma['total'])}] casos (:orange[{format_number(porcentagem_total_top1_sintoma, '%0.2f')}%]) 
                    * **\"{top2_sintoma['sintoma']}\"** com :blue[{format_number(top2_sintoma['total'])}] casos (:orange[{format_number(porcentagem_total_top2_sintoma, '%0.2f')}%]) 
                    * **\"{top3_sintoma['sintoma']}\"** com :blue[{format_number(top3_sintoma['total'])}] casos (:orange[{format_number(porcentagem_total_top3_sintoma, '%0.2f')}%]) 

                    Vale notar que os sintomas podem ter ocorrido em paralelo (o que explica as porcentagens aproximadas entre si).
                """
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

                st.markdown(
                    f"""
                    Agora, na segunda parte, é apresentado os sintomas agrupados em :blue[3 categorias principais] e as relações entre cada uma delas. As :blue[3 categorias] escolhidas para segmentar os sintomas foram:
                    * Sintomas respiratórios
                    * Sintomas gastrointestinais
                    * Sintomas gerais
                """
                )

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
                # TODO: o total aqui está estranho
                # TODO: o total aqui está estranho
                # TODO: o total aqui está estranho
                # TODO: o total aqui está estranho
                df_escolaridade_covid = pd.read_csv(
                    "assets/csv/segmentacao-escolaridade-x-casos-positivos.csv"
                )

                ids_escolaridade_precaria = [1, 2, 3, 4, 5]
                total_escolaridade_precaria = df_escolaridade_covid.query(
                    f"id in @ids_escolaridade_precaria"
                ).contagem.sum()
                porcentagem_total_escolaridade_precaria = (
                    (total_escolaridade_precaria / total_positivos) * 100
                ).round(2)

                st.markdown(
                    f"""
                    **:blue[Segmentação de escolaridade X COVID-19 positivo]**\n
                    Nesta parte, relacionamos o grau de escolaridade com a classificação de COVID-19 positivo entre os entrevistados. Alguns pontos importantes que devem ser observados nesta análise:
                    * :blue[{format_number(total_escolaridade_precaria)}] (:orange[{format_number(porcentagem_total_escolaridade_precaria, '%0.2f')}%]) dos casos foram confirmados em entrevistados que possuem do ensino médio para baixo;
                    * É importante frisar que casos onde o status foi "Aguardando resulado" ou qualquer outro de indefinição, diferente de negativo, não foram considerados nesta análise;
                    * Aqui há 2 hipóteses consideradas:
                        1) Muitos dos entrevistados são jovens (crianças ou adolescentes), conforme visto na seção de \"Análise demográfica\";
                        2) Boa parte dos entrevistados com menor grau de instrução, estão sujeitos à empregos mais manuais, que demandam a sua presença física no local de trabalho;
                """
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
                        title="Segmentação de escolaridade X COVID-19 positivo",
                        width=500,
                    )
                    st.plotly_chart(fig)

                with col2:
                    st.image(
                        "assets/img/analise-segmentacao-escolaridade-x-covid-positivo.png",
                        caption="Gráfico de waffle",
                    )

            # TODO: o total aqui está estranho
            # TODO: o total aqui está estranho
            with st.container():
                st.markdown(
                    """
                    **:blue[Segmentação de plano de saúde X COVID-19 positivo]**\n
                    Nesta seção, é possível verificar que a maioria dos casos positivos de COVID-19 são em pessoas que não possuem um plano de saúde que possam suprir suas necessidades.
                """
                )

                df_plano_saude_covid = pd.read_csv(
                    "assets/csv/segmentacao-plano-saude-x-casos-positivos.csv"
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
                        title="Segmentação de plano de saúde X COVID-19 positivo",
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
                    "assets/csv/evolucao-casos-positivos-mes-a-mes.csv"
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
                    "assets/csv/evolucao-casos-positivos-mes-a-mes-por-uf.csv"
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
