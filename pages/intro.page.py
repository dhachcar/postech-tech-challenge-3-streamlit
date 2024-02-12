import streamlit as st
from util.layout import output_layout

st.set_page_config(page_title="Introdução | Tech Challenge 3 | FIAP", layout='wide')
output_layout()

# aba com breve texto explicando o desafio
# aba com texto explicando pnda
# aba com texto explicando as perguntas utilizadas
# aba explicando brevemente a covid19 e o cenario na epoca

with st.container():
    st.header('Introdução')

    tab0, tab1, tab2, tab3 = st.tabs(tabs=['PNAD COVID19', 'Apache Spark', 'Google BigQuery', 'Machine Learning'])

    with tab0:
        st.subheader(':blue[PNAD COVID19]', divider='blue')
        st.markdown('''
        A PNAD COVID19, ou Pesquisa Nacional por Amostra de Domicílios sobre os efeitos da pandemia de COVID-19 no Brasil, foi uma iniciativa conduzida pelo Instituto Brasileiro de Geografia e Estatística (IBGE) para compreender os impactos socioeconômicos da crise sanitária no país. Lançada em 04 maio de 2020, a pesquisa teve como objetivo principal coletar dados sobre diversos aspectos da vida da população brasileira durante a pandemia, incluindo o mercado de trabalho, acesso a serviços de saúde, educação e outras áreas afetadas.\n\n
        Utilizando entrevistas telefônicas com amostras representativas da população, a PNAD COVID19 buscou captar informações sobre mudanças no emprego e renda, acesso a benefícios governamentais, adaptações no ensino remoto, impactos na saúde mental, entre outros aspectos relevantes. Esses dados foram cruciais para entender como a pandemia afetou diferentes grupos sociais e regiões do país, permitindo a elaboração de políticas e ações mais direcionadas para enfrentar os desafios socioeconômicos gerados pela crise.\n\n
        Ao longo de sua realização, a PNAD COVID19 proporcionou insights valiosos para governos, instituições de pesquisa, organizações da sociedade civil e demais interessados, contribuindo para uma compreensão mais completa dos efeitos da pandemia no Brasil e fornecendo subsídios para a tomada de decisões informadas visando mitigar seus impactos e promover a recuperação socioeconômica do país.
        ''')

        st.subheader(':blue[Bases de dados utilizadas]', divider='blue')
        st.markdown('''
            Durante este projeto, são utilizadas as bases de dados dos últimos 3 meses da PNAD COVID19 (Setembro, Outubro e Novembro).\n\n
            Para a visualização das bases de dados, utilize o download abaixo:
        ''')
        st.link_button('Download', 'https://www.ibge.gov.br/estatisticas/downloads-estatisticas.html?caminho=Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_PNAD_COVID19/Microdados/Dados', help=None, type="secondary", disabled=False, use_container_width=False)

        st.subheader(':blue[Dicionários das bases de dados]', divider='blue')
        st.markdown('''
            Para interpretarmos os dados das PNAD COVID19, precisamos utilizar os dicionários de dados, que mudam conforme o mês de pesquisa.
            - Os dicionários de Setembro e Outubro são idênticos;
            - Já o dicionário de Novembro tem alguma pequenas modificações, mas que não deve impactar em nossas análises;
                    
            Para a visualização dos dicionários das bases de dados, utilize o download abaixo:
        ''')
        st.link_button('Download', 'https://www.ibge.gov.br/estatisticas/downloads-estatisticas.html?caminho=Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_PNAD_COVID19/Microdados/Documentacao', help=None, type="secondary", disabled=False, use_container_width=False)

        # TODO: melhorar
        st.subheader(':blue[As perguntas escolhidas para realização do projeto]', divider='blue')
        st.markdown('''
            ###### Dados Padrão (Informações Pessoais)

            Estas são as colunas que contêm informações básicas sobre os respondentes. Elas não são contadas como perguntas, mas são essenciais para contextualizar e segmentar as respostas.

            | Código | Descrição |
            | ------ | --------- |
            | UF | Unidade da Federação |
            | CAPITAL | Capital |
            | RM_RIDE | Região Metropolitana e Região Administrativa Integrada de Desenvolvimento |
            | V1012 | Semana no mês |
            | V1013 | Mês da pesquisa |
            | V1022 | Situação do domicílio |
            | V1023 | Tipo de área |
            | A002 | Idade do morador |
            | A003 | Sexo |
            | A004 | Cor ou raça |
            | A005 | Escolaridade |
        ''')

        # TODO: melhorar
        st.markdown('''
            ###### Perguntas Clínicas, Comportamentais e Econômicas

            Estas colunas nos ajudam a entender os sintomas clínicos apresentados pelos respondentes durante a pandemia, bem como seus comportamentos e atitudes.

            | Pergunta | Código | Descrição |
            | -------- | ------ | --------- |
            | 1 | B0011 | Na semana passada teve febre? |
            | 2 | B0012 | Na semana passada teve tosse? |
            | 3 | B0013 | Na semana passada teve dor de garganta? |
            | 4 | B0014 | Na semana passada teve dificuldade para respirar? |
            | 5 | B0015 | Na semana passada teve dor de cabeça? |
            | 6 | B0016 | Na semana passada teve dor no peito? |
            | 7 | B0017 | Na semana passada teve náusea? |
            | 8 | B0018 | Na semana passada teve nariz entupido ou escorrendo? |
            | 9 | B0019 | Na semana passada teve fadiga? |
            | 10 | B00110 | Na semana passada teve dor nos olhos? |
            | 11 | B00111 | Na semana passada teve perda de cheiro ou sabor? |
            | 12 | B00112 | Na semana passada teve dor muscular? |
            | 13 | B00113 | Na semana passada teve diarreia? |
            | 14 | B002 | Por causa disso, foi a algum estabelecimento de saúde? |
            | 15 | B006 | Durante a internação, foi sedado, entubado e colocado em respiração artificial com ventilador |
            | 16 | B007 | Tem algum plano de saúde médico, seja particular, de empresa ou de órgão público |
            | 17 | B009B | Qual o resultado? (SWAB) |
            | 18 | B011 | Na semana passada, devido à pandemia do Coronavírus, em que medida o(a) Sr(a) restringiu o contato com as pessoas? |
            | 19 | C013 | Na semana passada, o(a) Sr(a) estava em trabalho remoto (home office ou teletrabalho)? |
            | 20 | D0051 | Auxílios emergenciais relacionados ao coronavirus |
        ''')
        
