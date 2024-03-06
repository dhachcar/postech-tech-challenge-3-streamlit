import streamlit as st
from tabs.tab import TabInterface


class IntroGoogleBigQueryTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":blue[Google BigQuery]", divider="blue")
            st.markdown(
                """
                O **:blue[Google BigQuery]** é um serviço de armazenamento e análise de dados na nuvem oferecido pelo Google. Ele permite que as organizações armazenem, consultem e analisem grandes volumes de dados de maneira rápida e eficiente, usando a linguagem de consulta SQL padrão. O **:blue[BigQuery]** é altamente escalável, oferecendo capacidade de processamento sob demanda e integração fácil com outras ferramentas e serviços do ecossistema do Google Cloud Platform (GCP).\n\n
                O **:blue[BigQuery]** é o serviço em nuvem escolhido para a realização deste trabalho. Ele tem como seus principais concorrentes, o :blue[AWS Redshift] e o :blue[Azure Synapse Analytics].
            """
            )

            st.subheader(":blue[Tabelas]", divider="blue")
            st.markdown(
                """
                Dentro do banco de dados no **:blue[BigQuery]**, temos :blue[5] tipos de tabela:
                1) Tabelas com os dados originais (mês a mês);
                    * :blue[Exemplo: **pnad_covid_nov_2020**]
                2) Tabelas processadas, contemplando exclusivamente as colunas/features que serão utilizadas durante o projeto (mês a mês);
                    * :blue[Exemplo: **pnad_covid_nov_2020_processado**]
                3) Tabela de união das tabelas processadas mês a mês; 
                    * :blue[Exemplo: **pnad_covid_2020**]
                4) Tabela final de união com as colunas renomeadas para facilitar a o entendimento do schema;
                    * :blue[Exemplo: **pnad_covid_2020_processado**]
                5) Tabelas auxiliares com valores do domínio a respeito da pesquisa PNAD COVID-19 (id de UF, por exemplo).
                    * :blue[Exemplo: **pnad_covid_2020_aux_uf**]
                        
                As tabelas com os dados originais foram geradas a partir de arquivos CSV que foram enviados ao **:blue[Google Cloud Storage]**. O processo é detalhado na seção de :blue[Banco de dados].\n
                Além disso, podemos visualizar melhor o processo de transformação dos dados da PNAD (etapas 1 à 4 mais especificamente), conforme imagem a seguir:
            """
            )

            st.image(
                "assets/img/db-transform.png",
                caption="Etapas de transformação dos dados PNAD COVID-19",
            )

            st.markdown('''
                Por fim, são apresentados algumas imagens das tabelas e suas colunas, dentro da ferramenta do **:blue[BigQuery]**
            ''')

            st.image(
                "assets/img/bigquery-explorer-datasets.png",
                caption="Tabelas no Google BigQuery",
            )

            with st.container():
                col1, col2, _ = st.columns([1, 1, 1])

                with col1:
                    st.image(
                        "assets/img/bigquery-exemplo tabela-não-processada.png",
                        caption="Exemplo de colunas das tabelas originais (não processadas)",
                    )

                with col2:
                    st.image(
                        "assets/img/bigquery-exemplo-tabela-processada.png",
                        caption="Exemplo de colunas das tabelas finais (processadas)",
                    )

            st.image(
                "assets/img/bigquery-exemplo-select-pnad-processado.png",
                caption="Exemplo de dados armazenados na tabela agrupada e processada no Google BigQuery",
            )

            st.divider()

            st.markdown(
                """
                **:blue[Dados de Setembro]**\n\n
                A tabela inicial com os dados de Setembro possui :blue[387.298] registros e ocupa um total de :blue[218,94MB].\n\n
                Já a versão processada, permanece com a mesma quantidade registros mas ocupando um total de :blue[75,86MB].
            """
            )
            with st.container():
                col1, col2, _ = st.columns([1, 1, 1])

                with col1:
                    st.image(
                        "assets/img/bigquery-detalhes-pnad-set-2020.png",
                        caption="Detalhes da tabela de Setembro (não processado)",
                    )

                with col2:
                    st.image(
                        "assets/img/bigquery-detalhes-pnad-set-2020-processado.png",
                        caption="Detalhes da tabela de Setembro (processado)",
                    )

            st.divider()

            st.markdown(
                """
                **:blue[Dados de Outubro]**\n\n
                A tabela inicial com os dados de Outubro possui :blue[380.461] registros e ocupa um total de :blue[215,36MB].\n\n
                Já a versão processada, permanece com a mesma quantidade registros mas ocupando um total de :blue[74,53MB].
            """
            )
            with st.container():
                col1, col2, _ = st.columns([1, 1, 1])

                with col1:
                    st.image(
                        "assets/img/bigquery-detalhes-pnad-out-2020.png",
                        caption="Detalhes da tabela de Outubro (não processado)",
                    )

                with col2:
                    st.image(
                        "assets/img/bigquery-detalhes-pnad-out-2020-processado.png",
                        caption="Detalhes da tabela de Outubro (processado)",
                    )

            st.divider()

            st.markdown(
                """
                **:blue[Dados de Novembro]**\n\n
                A tabela inicial com os dados de Novembro possui :blue[381.438] registros e ocupa um total de :blue[217,39MB].\n\n
                Já a versão processada, permanece com a mesma quantidade registros mas ocupando um total de :blue[74,75MB].
            """
            )
            with st.container():
                col1, col2, _ = st.columns([1, 1, 1])

                with col1:
                    st.image(
                        "assets/img/bigquery-detalhes-pnad-nov-2020.png",
                        caption="Detalhes da tabela de Novembro (não processado)",
                    )

                with col2:
                    st.image(
                        "assets/img/bigquery-detalhes-pnad-nov-2020-processado.png",
                        caption="Detalhes da tabela de Novembro (processado)",
                    )

            st.divider()

            st.markdown(
                """
                **:blue[Dados consolidados]**\n\n
                Ao juntarmos todas as 3 tabelas processadas, temos um total de :blue[1.149.187] registros.
            """
            )

            st.image(
                "assets/img/bigquery-total-registros-processados.png",
                caption="Total de registros geral",
            )
