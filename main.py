import plotly.graph_objs as go
import pandas as pd
import streamlit as st
from util.layout import output_layout
import warnings
import locale


warnings.filterwarnings("ignore")
locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
st.set_page_config(page_title="Tech Challenge 3 | FIAP", layout="wide")
output_layout()

st.header(":orange[Tech Challenge 3 | Data Science | FIAP]")

st.subheader(
    ":blue[Explorando os Impactos da Pandemia de COVID-19 no Brasil através da Análise de Dados]",
    divider="blue",
)
st.markdown(
    """
    A pandemia de COVID-19, declarada pela Organização Mundial da Saúde (OMS) em março de 2020, representou um dos desafios mais significativos enfrentados pela humanidade no século XXI. Além dos impactos diretos na saúde pública, a disseminação do vírus SARS-CoV-2 provocou profundas repercussões socioeconômicas em todo o mundo, incluindo no Brasil. Diante deste contexto, compreender os efeitos da pandemia e suas ramificações em diferentes aspectos da vida da população torna-se uma prioridade crucial para governos, instituições de pesquisa e demais atores sociais.\n\n
    Este trabalho tem como objetivo explorar os impactos da pandemia de COVID-19 no Brasil através da análise de dados, utilizando informações coletadas pela Pesquisa Nacional por Amostra de Domicílios Contínua (PNAD) COVID-19, conduzida pelo Instituto Brasileiro de Geografia e Estatística (IBGE). A PNAD COVID-19 é uma ferramenta fundamental que fornece insights valiosos sobre como a crise sanitária afetou diversos aspectos da vida dos brasileiros, incluindo o mercado de trabalho, acesso a serviços de saúde, educação, entre outros.
    Por meio da análise desses dados, buscamos identificar padrões, tendências e desafios enfrentados pela população brasileira durante a pandemia. Ao compreendermos melhor os impactos socioeconômicos da COVID-19, podemos contribuir para o desenvolvimento de estratégias e políticas mais eficazes para enfrentar os desafios atuais e promover a recuperação pós-pandemia.\n\n
    Neste trabalho, vamos explorar os dados da PNAD COVID-19 para fornecer uma visão abrangente e fundamentada sobre os efeitos da pandemia no Brasil, contribuindo assim para uma compreensão mais completa dessa crise sem precedentes.
"""
)

st.subheader(":blue[Objetivo]", divider="blue")
st.markdown(
    """
    O objetivo deste trabalho é analisar os dados da PNAD COVID-19 para compreender os impactos da pandemia no Brasil e contribuir para o desenvolvimento de estratégias eficazes de enfrentamento e recuperação pós-pandemia.
"""
)

st.subheader(":blue[Metodologia]", divider="blue")
st.markdown(
    """
    Neste estudo, serão utilizados dados da PNAD COVID-19 que foram coletados em seus :blue[últimos três meses (Setembro, Outubro e Novembro)], organizados em um banco de dados em nuvem. Selecionaremos 20 perguntas relevantes sobre áreas afetadas pela pandemia. Os dados serão limpos e analisados estatisticamente para identificar padrões e relações entre as variáveis.\n\n
    Os resultados fornecerão insights sobre os impactos da COVID-19 no Brasil, orientando estratégias de enfrentamento e recuperação, além de auxiliar numa possível nova pandemia no futuro.
"""
)
