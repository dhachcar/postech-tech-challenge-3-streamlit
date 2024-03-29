import streamlit as st
from tabs.tab import TabInterface

class IntroPnadTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':blue[PNAD COVID-19]', divider='blue')
            st.markdown('''
            A PNAD COVID-19, ou Pesquisa Nacional por Amostra de Domicílios sobre os efeitos da pandemia de COVID-19 no Brasil, foi uma iniciativa conduzida pelo Instituto Brasileiro de Geografia e Estatística (IBGE) para compreender os impactos socioeconômicos da crise sanitária no país. Lançada em 04 maio de 2020, a pesquisa teve como objetivo principal coletar dados sobre diversos aspectos da vida da população brasileira durante a pandemia, incluindo o mercado de trabalho, acesso a serviços de saúde, educação e outras áreas afetadas.\n\n
            Utilizando entrevistas telefônicas com amostras representativas da população, a PNAD COVID-19 buscou captar informações sobre mudanças no emprego e renda, acesso a benefícios governamentais, adaptações no ensino remoto, impactos na saúde mental, entre outros aspectos relevantes. Esses dados foram cruciais para entender como a pandemia afetou diferentes grupos sociais e regiões do país, permitindo a elaboração de políticas e ações mais direcionadas para enfrentar os desafios socioeconômicos gerados pela crise.\n\n
            Ao longo de sua realização, a PNAD COVID-19 proporcionou insights valiosos para governos, instituições de pesquisa, organizações da sociedade civil e demais interessados, contribuindo para uma compreensão mais completa dos efeitos da pandemia no Brasil e fornecendo subsídios para a tomada de decisões informadas visando mitigar seus impactos e promover a recuperação socioeconômica do país.
            ''')

            st.subheader(':blue[Bases de dados utilizadas]', divider='blue')
            st.markdown('''
                Durante este projeto, são utilizadas as bases de dados dos últimos 3 meses da PNAD COVID-19 (Setembro, Outubro e Novembro).\n\n
                Vale notar que segundo o IBGE, a amostra da pesquisa é fixa, ou seja, os domicílios entrevistados no primeiro mês de coleta de dados permanecerão na amostra nos meses subsequentes, até o fim da pesquisa e assim subsequentemente.\n\n
                Para a visualização das bases de dados, utilize o link abaixo:
            ''')
            st.link_button('Download', 'https://www.ibge.gov.br/estatisticas/downloads-estatisticas.html?caminho=Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_PNAD_COVID19/Microdados/Dados', help=None, type="secondary", disabled=False, use_container_width=False)

            st.subheader(':blue[Dicionários das bases de dados]', divider='blue')
            st.markdown('''
                Para interpretarmos os dados das PNAD COVID-19, precisamos utilizar os dicionários de dados, que mudam conforme o mês de pesquisa.
                - Os dicionários de Setembro e Outubro são idênticos;
                - Já o dicionário de Novembro tem alguma pequenas modificações, mas que não deve impactar em nossas análises;
                        
                Além disso, as perguntas estão organizadas em 6 grupos principais, cada um com um objetivo distinto de coleta, onde:
                - A: Características dos moradores
                - B: COVID-19
                - C: Características de trabalho das pessoas de 14 anos ou mais de idade
                - D: Rendimentos de outras fontes de todos os moradores do domicílio
                - E: Empréstimos
                - F: Domicílio, propriedade e valor do aluguel
                        
                Para a visualização dos dicionários das bases de dados, utilize o link abaixo:
            ''')
            st.link_button('Download', 'https://www.ibge.gov.br/estatisticas/downloads-estatisticas.html?caminho=Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_PNAD_COVID19/Microdados/Documentacao', help=None, type="secondary", disabled=False, use_container_width=False)

            st.subheader(':blue[Instrumentos de coleta]', divider='blue')
            st.markdown('''
                A Pesquisa Nacional por Amostra de Domicílios (PNAD) COVID-19, conduzida pelo IBGE, coletou dados sobre os impactos da pandemia através de três versões de questionários, aplicados por entrevistas telefônicas. As versões evoluíram ao longo do tempo, abordando aspectos como saúde, trabalho, educação, renda, trabalho remoto, acesso a benefícios sociais, prevenção do vírus, retorno às aulas, saúde mental e segurança alimentar, refletindo a dinâmica da pandemia e fornecendo insights cruciais para políticas públicas e estratégias de enfrentamento.
                - 1ª versão (Maio e Junho)
                - 2ª versão (Julho, Agosto, Setembro e Outubro)
                - 3ª versão (Novembro)
                        
                Neste trabalho, serão utilizadas como base as versões 2 e 3 dos instrumentos de coleta, já que as perguntas que mudam entre elas são as do módulo A, que dizem respeito à identificação do respondente/domicílio e não impactam as respostas de caráter clínico.
                Para a visualização dos instrumentos de coleta, utilize os links abaixo:
            ''')
            st.link_button('2ª versão', 'https://biblioteca.ibge.gov.br/visualizacao/instrumentos_de_coleta/doc5592.pdf', help=None, type="secondary", disabled=False, use_container_width=False)
            st.link_button('3ª versão', 'https://biblioteca.ibge.gov.br/visualizacao/instrumentos_de_coleta/doc5601.pdf', help=None, type="secondary", disabled=False, use_container_width=False)

            st.subheader(':blue[As perguntas escolhidas para realização do projeto]', divider='blue')
            st.markdown('''
                **:blue[Perguntas para identificação]**\n\n
                As perguntas à seguir são reservadas para dados básicos dos entrevistados. Elas servem para contextualizar e segmentar as respostas coletadas de todos os entrevistados.
                | Identificador | Descrição da pergunta |
                | - | - |
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
  
                &nbsp;
            ''')

            st.markdown('''
                **:blue[Perguntas de saúde, economia e comportamento durante a pandemia]**\n\n
                As perguntas à seguir auxiliam na compreensão dos sintomas clínicos informados pelos entrevistados. Também ajudam a entender os seus hábitos durante a pandemia.\n\n
                Vale notar que foram utilizadas **:blue[20 perguntas]** do total de disponíveis da PNAD.
                | Identificador | Descrição da pergunta |
                | - | - |
                | B0011 | Na semana passada teve febre? |
                | B0012 | Na semana passada teve tosse? |
                | B0013 | Na semana passada teve dor de garganta? |
                | B0014 | Na semana passada teve dificuldade para respirar? |
                | B0015 | Na semana passada teve dor de cabeça? |
                | B0016 | Na semana passada teve dor no peito? |
                | B0017 | Na semana passada teve náusea? |
                | B0018 | Na semana passada teve nariz entupido ou escorrendo? |
                | B0019 | Na semana passada teve fadiga? |
                | B00110 | Na semana passada teve dor nos olhos? |
                | B00111 | Na semana passada teve perda de cheiro ou sabor? |
                | B00112 | Na semana passada teve dor muscular? |
                | B00113 | Na semana passada teve diarreia? |
                | B002 | Por causa disso, foi a algum estabelecimento de saúde? |
                | B006 | Durante a internação, foi sedado, entubado e colocado em respiração artificial com ventilador |
                | B007 | Tem algum plano de saúde médico, seja particular, de empresa ou de órgão público |
                | B009B | Qual o resultado? |
                | B011 | Na semana passada, devido à pandemia do Coronavírus, em que medida o(a) Sr(a) restringiu o contato com as pessoas? |
                | C013 | Na semana passada, o(a) Sr(a) estava em trabalho remoto (home office ou teletrabalho)? |
                | D0051 | Auxílios emergenciais relacionados ao coronavirus |
            ''')