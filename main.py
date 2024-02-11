import plotly.graph_objs as go
import pandas as pd
import streamlit as st
from util.layout import output_layout

st.set_page_config(page_title="Tech Challenge 3 | FIAP", layout='wide')
output_layout()

st.header('Tech Challenge 3 | Data Science | FIAP')

st.subheader('Explorando os Impactos da Pandemia de COVID-19 no Brasil através da Análise de Dados')
st.markdown('''
A pandemia de COVID-19, declarada pela Organização Mundial da Saúde (OMS) em março de 2020, representou um dos desafios mais significativos enfrentados pela humanidade no século XXI. Além dos impactos diretos na saúde pública, a disseminação do vírus SARS-CoV-2 provocou profundas repercussões socioeconômicas em todo o mundo, incluindo no Brasil. Diante deste contexto, compreender os efeitos da pandemia e suas ramificações em diferentes aspectos da vida da população torna-se uma prioridade crucial para governos, instituições de pesquisa e demais atores sociais.\n\n
Este trabalho tem como objetivo explorar os impactos da pandemia de COVID-19 no Brasil através da análise de dados, utilizando informações coletadas pela Pesquisa Nacional por Amostra de Domicílios Contínua (PNAD) COVID19, conduzida pelo Instituto Brasileiro de Geografia e Estatística (IBGE). A PNAD COVID19 é uma ferramenta fundamental que fornece insights valiosos sobre como a crise sanitária afetou diversos aspectos da vida dos brasileiros, incluindo o mercado de trabalho, acesso a serviços de saúde, educação, entre outros.
Por meio da análise desses dados, buscamos identificar padrões, tendências e desafios enfrentados pela população brasileira durante a pandemia. Ao compreendermos melhor os impactos socioeconômicos da COVID-19, podemos contribuir para o desenvolvimento de estratégias e políticas mais eficazes para enfrentar os desafios atuais e promover a recuperação pós-pandemia.\n\n
Neste trabalho, vamos explorar os dados da PNAD COVID19 para fornecer uma visão abrangente e fundamentada sobre os efeitos da pandemia no Brasil, contribuindo assim para uma compreensão mais completa dessa crise sem precedentes.
''')

st.subheader('PNAD COVID19')
st.markdown('''
A PNAD COVID19, ou Pesquisa Nacional por Amostra de Domicílios sobre os efeitos da pandemia de COVID-19 no Brasil, foi uma iniciativa conduzida pelo Instituto Brasileiro de Geografia e Estatística (IBGE) para compreender os impactos socioeconômicos da crise sanitária no país. Lançada em 04 maio de 2020, a pesquisa teve como objetivo principal coletar dados sobre diversos aspectos da vida da população brasileira durante a pandemia, incluindo o mercado de trabalho, acesso a serviços de saúde, educação e outras áreas afetadas.\n\n
Utilizando entrevistas telefônicas com amostras representativas da população, a PNAD COVID19 buscou captar informações sobre mudanças no emprego e renda, acesso a benefícios governamentais, adaptações no ensino remoto, impactos na saúde mental, entre outros aspectos relevantes. Esses dados foram cruciais para entender como a pandemia afetou diferentes grupos sociais e regiões do país, permitindo a elaboração de políticas e ações mais direcionadas para enfrentar os desafios socioeconômicos gerados pela crise.\n\n
Ao longo de sua realização, a PNAD COVID19 proporcionou insights valiosos para governos, instituições de pesquisa, organizações da sociedade civil e demais interessados, contribuindo para uma compreensão mais completa dos efeitos da pandemia no Brasil e fornecendo subsídios para a tomada de decisões informadas visando mitigar seus impactos e promover a recuperação socioeconômica do país.
''')

st.subheader('Objetivo')
st.markdown('''
O objetivo deste trabalho é analisar os dados da PNAD COVID19 para compreender os impactos da pandemia de COVID-19 no Brasil e contribuir para o desenvolvimento de estratégias eficazes de enfrentamento e recuperação pós-pandemia.
''')

st.subheader('Metodologia')
st.markdown('''
Neste estudo, serão utilizados dados da PNAD COVID19 que foram coletados em seus últimos três meses (Setembro, Outubro e Novembro), organizados em um banco de dados em nuvem. Selecionaremos 20 perguntas relevantes sobre áreas afetadas pela pandemia. Os dados serão limpos e analisados estatisticamente para identificar padrões e relações entre as variáveis. Os resultados fornecerão insights sobre os impactos da COVID-19 no Brasil, orientando estratégias de enfrentamento e recuperação e auxiliando numa possível nova pandemia no futuro.
''')