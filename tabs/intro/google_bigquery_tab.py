import streamlit as st
from tabs.tab import TabInterface

class IntroGoogleBigQueryTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':blue[Google BigQuery]', divider='blue')
            st.markdown('''
                O Google BigQuery é um serviço de armazenamento e análise de dados na nuvem oferecido pelo Google. Ele permite que as organizações armazenem, consultem e analisem grandes volumes de dados de maneira rápida e eficiente, usando a linguagem de consulta SQL padrão. O BigQuery é altamente escalável, oferecendo capacidade de processamento sob demanda e integração fácil com outras ferramentas e serviços do ecossistema do Google Cloud Platform (GCP).\n\n
                O BigQuery é o serviço em nuvem escolhido para a realização deste trabalho.
            ''')

            st.subheader(':blue[Tabelas]', divider='blue')
            st.markdown('''
                Dentro do banco de dados no BigQuery, temos 5 tipos de tabela:
                1) Tabelas com os dados originais (mês a mês);
                2) Tabelas processadas, contemplando exclusivamente as colunas/features que serão utilizadas durante o projeto (mês a mês);
                3) Tabela de união das tabelas processadas mês a mês;
                4) Tabela final de união com as colunas renomeadas para facilitar a o entendimento do schema;
                5) Tabelas auxiliares com valores do domínio a respeito da pesquisa PNAD COVID19 (id de UF, por exemplo).
                        
                As tabelas com os dados originais foram geradas a partir de arquivos CSV que foram enviados ao Google Cloud Storage, um serviço de armazenamento em nuvem (muito parecido com o S3 da Amazon).
            ''')

            st.markdown(':rainbow[TODO: atualizar print com as tabelas finais processadas e print com tabelas auxiliares de exemplo]')
            st.image('assets/img/bigquery-explorer-datasets.png', caption='Tabelas no Google BigQuery')

            with st.container():
                col1, col2, _ = st.columns([1, 1, 1])
            
                with col1:
                    st.image('assets/img/bigquery-exemplo tabela-não-processada.png', caption='Exemplo de colunas das tabelas originais (não processadas)')

                with col2:
                    st.image('assets/img/bigquery-exemplo-tabela-processada.png', caption='Exemplo de colunas das tabelas finais (processadas)')

            st.divider()

            st.markdown('''
                **:blue[Dados de Setembro]**\n\n
                A tabela inicial com os dados de Setembro possui :blue[387.298] registros e ocupa um total de :blue[218,94MB].\n\n
                Já a versão processada, permanece com a mesma quantidade registros mas ocupando um total de :blue[75,86MB].
            ''')
            with st.container():
                col1, col2, _ = st.columns([1, 1, 1])
            
                with col1:
                    st.image('assets/img/bigquery-detalhes-pnad-set-2020.png', caption='Detalhes da tabela de Setembro (não processado)')

                with col2:
                    st.image('assets/img/bigquery-detalhes-pnad-set-2020-processado.png', caption='Detalhes da tabela de Setembro (processado)')

            st.divider()

            st.markdown('''
                **:blue[Dados de Outubro]**\n\n
                A tabela inicial com os dados de Outubro possui :blue[380.461] registros e ocupa um total de :blue[215,36MB].\n\n
                Já a versão processada, permanece com a mesma quantidade registros mas ocupando um total de :blue[74,53MB].
            ''')
            with st.container():
                col1, col2, _ = st.columns([1, 1, 1])

                with col1:
                    st.image('assets/img/bigquery-detalhes-pnad-out-2020.png', caption='Detalhes da tabela de Outubro (não processado)')

                with col2:
                    st.image('assets/img/bigquery-detalhes-pnad-out-2020-processado.png', caption='Detalhes da tabela de Outubro (processado)')

            st.divider()

            st.markdown('''
                **:blue[Dados de Novembro]**\n\n
                A tabela inicial com os dados de Novembro possui :blue[381.438] registros e ocupa um total de :blue[217,39MB].\n\n
                Já a versão processada, permanece com a mesma quantidade registros mas ocupando um total de :blue[74,75MB].
            ''')
            with st.container():
                col1, col2, _ = st.columns([1, 1, 1])

                with col1:
                    st.image('assets/img/bigquery-detalhes-pnad-nov-2020.png', caption='Detalhes da tabela de Novembro (não processado)')

                with col2:
                    st.image('assets/img/bigquery-detalhes-pnad-nov-2020-processado.png', caption='Detalhes da tabela de Novembro (processado)')

            st.divider()

            st.markdown('''
                **:blue[Dados consolidados]**\n\n
                Ao juntarmos todas as 3 tabelas processadas, temos um total de :blue[1.149.187] registros.
            ''')

            st.image('assets/img/bigquery-total-registros-processados.png', caption='Total de registros geral')