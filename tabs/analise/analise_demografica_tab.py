import streamlit as st
from tabs.tab import TabInterface
import plotly.graph_objs as go
import pandas as pd
from util.layout import format_number


class AnaliseDemograficaTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":blue[Análise demográfica]", divider="blue")

            st.markdown(
                """
                Nesta seção, investigamos como os entrevistados pela pesquisa estão distribuídos em relação ao conjunto total de dados estudados, com foco no quésito **:blue[demográfico]**. Vale notar que alguns gráficos que são apresentados nas próximas seções, possuem 2 visões do mesmo dado.
            """
            )

            indicadores_gerais = pd.read_csv("assets/csv/indicadores.csv")
            total_entrevistados = indicadores_gerais.total_entrevistados.values[0]

            with st.container():
                st.markdown(
                    """
                    **:blue[Indicadores gerais]**
                """
                )

                with st.container():
                    _, col1, col2, _ = st.columns([3, 2, 2, 3])

                    with col1:
                        st.metric(
                            label="Total de entrevistados",
                            value=format_number(total_entrevistados),
                            delta=format_number(100, "%0.2f") + "%",
                            delta_color="off",
                        )

                    with col2:
                        st.metric(
                            label="Média de idade",
                            value=format_number(
                                indicadores_gerais.idade_media.values[0].round(0),
                            )
                            + " anos",
                            delta=format_number(100, "%0.2f") + "%",
                            delta_color="off",
                        )

            with st.container():
                sexo_cores = ["#983D3D", "#232066"]
                df_pnad_sexo = pd.read_csv("assets/csv/segmentacao-sexo.csv")
                total_mulheres = df_pnad_sexo.query("id == 2").total.values[0]
                porcentagem_mulheres = (
                    (total_mulheres / total_entrevistados) * 100
                ).round(2)

                st.markdown(
                    f"""
                    **:blue[Por sexo]**\n\n
                    Neste tópico, podemos observar como os entrevistados estão segregados em relação ao seu sexo. É observado que a maioria dos respondentes é do sexo :blue[feminino], com cerca de :blue[{format_number(total_mulheres)}] (:orange[{format_number(porcentagem_mulheres, '%0.2f')}%]) do total de entrevistados do conjunto de dados.
                """
                )

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
                df_pnad_uf = pd.read_csv("assets/csv/segmentacao-uf.csv")
                total_uf_mg = df_pnad_uf.query('nome == "Minas Gerais"').total.values[0]
                total_uf_sp = df_pnad_uf.query('nome == "São Paulo"').total.values[0]
                total_uf_rj = df_pnad_uf.query('nome == "Rio de Janeiro"').total.values[
                    0
                ]
                total_sudeste = total_uf_mg + total_uf_sp + total_uf_rj
                porcentagem_uf_mg = ((total_uf_mg / total_entrevistados) * 100).round(2)
                porcentagem_uf_sp = ((total_uf_sp / total_entrevistados) * 100).round(2)
                porcentagem_uf_rj = ((total_uf_rj / total_entrevistados) * 100).round(2)
                porcentagem_sudeste = (
                    (total_sudeste / total_entrevistados) * 100
                ).round(2)

                st.markdown(
                    f"""
                    **:blue[Por UF]**\n
                    A próxima segmentação realizada é feita com base no estado (UF) do entrevistado.\n
                    Assim, no gráfico à seguir, é possível observar que a maioria dos entrevistados se concentram na região Sudeste do Brasil (considerando os últimos 3 meses da pesquisa, foco deste projeto). Isso também pode ter relação à quantidade de pessoas que vivem nesta região do país, sendo ela a mais populosa dentre todas as outras. \n
                    Especificamente, Minas Gerais teve :blue[{format_number(total_uf_mg)}] entrevistados (:orange[{format_number(porcentagem_uf_mg, '%0.2f')}%] do total), enquanto que São Paulo e Rio de Janeiro tiveram :blue[{format_number(total_uf_sp)}] (:orange[{format_number(porcentagem_uf_sp, '%0.2f')}%]) e :blue[{format_number(total_uf_rj)}] (:orange[{format_number(porcentagem_uf_rj, '%0.2f')}%]) respectivamente. Os três estados em conjunto respondem por cerca de :blue[{format_number(total_sudeste)}] entrevistados ou :orange[{format_number(porcentagem_sudeste, '%0.2f')}%] do total.
                """
                )

                fig = go.Figure()
                fig.add_trace(
                    go.Bar(x=df_pnad_uf.nome.tolist(), y=df_pnad_uf.total.tolist())
                )
                fig.update_layout(title="Segmentação dos entrevistados por UF")
                fig.update_layout(xaxis=dict(tickangle=-45))
                st.plotly_chart(fig)

            with st.container():
                df_pnad_regiao_metropolitana = pd.read_csv(
                    "assets/csv/segmentacao-regiao-metropolitana.csv"
                )
                id_mg = 31
                id_sp = 35
                id_rj = 33
                total_rm_mg = df_pnad_regiao_metropolitana.query(
                    f"id == {id_mg}"
                ).total.values[0]
                total_rm_sp = df_pnad_regiao_metropolitana.query(
                    f"id == {id_sp}"
                ).total.values[0]
                total_rm_rj = df_pnad_regiao_metropolitana.query(
                    f"id == {id_rj}"
                ).total.values[0]
                total_sudeste = total_rm_mg + total_rm_sp + total_rm_rj
                porcentagem_rm_mg = ((total_rm_mg / total_entrevistados) * 100).round(2)
                porcentagem_rm_sp = ((total_rm_sp / total_entrevistados) * 100).round(2)
                porcentagem_rm_rj = ((total_rm_rj / total_entrevistados) * 100).round(2)
                porcentagem_sudeste = (
                    (total_sudeste / total_entrevistados) * 100
                ).round(2)

                st.markdown(
                    f"""
                    **:blue[Por região metropolitana]**\n
                    Nesta seção, os entrevistados foram segmentados pela região metropolitana a qual pertencem.
                    Conforme o gráfico à seguir, é possível observar que a maioria dos entrevistados se concentram na região Sudeste do Brasil (da mesma maneira que na segmentação anterior por UF).\n
                    Entretanto, a ordem das regiões com mais entrevistados se altera, deixando a região de Rio de Janeiro (RJ) com :blue[{format_number(total_rm_rj)}] entrevistados (:orange[{format_number(porcentagem_rm_rj, '%0.2f')}%] do total), enquanto que em 2º e 3º colocados, estão as regiões de São Paulo (SP) e Belo Horizonte (MG), respectivamente com :blue[{format_number(total_rm_sp)}] (:orange[{format_number(porcentagem_rm_sp, '%0.2f')}%]) e :blue[{format_number(total_rm_mg)}] (:orange[{format_number(porcentagem_rm_mg, '%0.2f')}%]). As três regiões em conjunto respondem por cerca de :blue[{format_number(total_sudeste)}] entrevistados ou :orange[{format_number(porcentagem_sudeste, '%0.2f')}%] do total.
                """
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
                df_pnad_escolaridade = pd.read_csv(
                    "assets/csv/segmentacao-escolaridade.csv"
                )
                ids_escolaridade_precaria = [1, 2, 3, 4, 5]
                total_escolaridade_precaria = df_pnad_escolaridade.query(
                    f"id in @ids_escolaridade_precaria"
                ).total.sum()
                porcentagem_escolaridade_precaria = (
                    (total_escolaridade_precaria / total_entrevistados) * 100
                ).round(2)

                st.markdown(
                    f"""
                    **:blue[Por escolaridade]**\n
                    No próximo tópico, é analisado a distribuição dos entrevistados em relação à sua escolaridade. Aqui, o dado que mais chama a atenção, é a quantidade dos entrevistados que teve uma educação precária (considerado como abaixo de Ensino Superior Incompleto), com cerca de :blue[{format_number(total_escolaridade_precaria)}] pessoas ou :orange[{format_number(porcentagem_escolaridade_precaria, '%0.2f')}%] do total de entrevistados. Estas pessoas provavelmente estavam em empregos considerados mais físicos, ou seja, com necessidade de presença física para exercer suas atividades. Este simples fato já demonstra que boa parte da população brasileira teve uma exposição maior ao vírus da COVID-19, devido ao seu grau de escolaridade.\n
                    Também há uma outra forma de interpretar estes dados: a idade dos entrevistados pode ter influenciado negativamente este número grande de pessoas com escolaridade considerada inadequada. A relação entre ambos é estabelecida na seção seguinte.
                """
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
                df_pnad_idade = pd.read_csv("assets/csv/segmentacao-idade.csv")
                faixas_etarias = df_pnad_idade.nome.values.astype(str)
                populacao = df_pnad_idade.total.values
                qtd_total_faixa_ate_18 = df_pnad_idade[df_pnad_idade.index == 0].total[
                    0
                ]
                porcentagem_qtd_total_faixa_ate_18 = (
                    (qtd_total_faixa_ate_18 / total_entrevistados) * 100
                ).round(2)

                st.markdown(
                    f"""
                    **:blue[Por faixa etária]**\n
                    Neste tópico, os entrevistados foram segmentados em grupos de idade, conforme a seguir:
                    * De 0 até 18 anos
                    * De 18 anos e 1 dia até 35 anos
                    * De 35 anos e 1 dia até 50 anos
                    * De 50 anos e 1 dia até 65 anos
                    * De 65 anos e 1 dia até 80 anos
                    * De 80 anos e 1 dia até 120 anos

                    É possível observar que uma parte considerável dos entrevistados (:blue[{format_number(qtd_total_faixa_ate_18)}] ou :orange[{format_number(porcentagem_qtd_total_faixa_ate_18, '%0.2f')}%] do total) está dentro da faixa de 0 até 18 anos. Isso pode explicar em partes, os resultados obtidos na segmentação anterior por escolaridade, mas não excluí o fato de quão precário é o ensino no Brasil.
                """
                )

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
                    **:blue[Por plano de saúde]**\n
                    Por último, é apresentado a quantidade de entrevistados que possui ou não um plano de saúde.\n
                    Infelizmente, conforme observado, a maioria dos entrevistados não possuía um plano de saúde durante a pandemia de COVID-19, o que denota sua vulnerabilidade diante de qualquer agente patogênico (e não exclusivamente a COVID), evidenciando a importância de acesso a cuidados médicos adequados.
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
