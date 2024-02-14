import streamlit as st
from util.layout import output_layout

st.set_page_config(page_title="Referências | Tech Challenge 3 | FIAP", layout='wide')
output_layout()

with st.container():
    st.header('Referências')

    st.markdown('''
    - O que é. PNAD COVID19. IBGE. Disponível em: https://www.ibge.gov.br/estatisticas/investigacoes-experimentais/estatisticas-experimentais/27946-divulgacao-semanal-pnadcovid1?t=o-que-e\n\n
    - Microdados. PNAD COVID19. IBGE. Disponível em: https://www.ibge.gov.br/estatisticas/investigacoes-experimentais/estatisticas-experimentais/27946-divulgacao-semanal-pnadcovid1?t=microdados\n\n
    - Informações Técnicas. PNAD COVID19. IBGE. Disponível em: https://www.ibge.gov.br/estatisticas/investigacoes-experimentais/estatisticas-experimentais/27946-divulgacao-semanal-pnadcovid1?t=notas-tecnicas\n\n
    - Apache Spark. Apache. Disponível em: https://spark.apache.org/
    - Google Big Query. Google. Disponível em: https://cloud.google.com/bigquery
    - Google Cloud Storage. Google. Disponível em: https://cloud.google.com/storage
    ''')