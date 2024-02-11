import streamlit as st
from util.layout import output_layout

st.set_page_config(page_title="Tech Challenge 3 | FIAP", layout='wide')
output_layout()

with st.container():
    st.header('Referências')

    st.markdown('''
    - O que é. PNAD COVID19. IBGE. https://www.ibge.gov.br/estatisticas/investigacoes-experimentais/estatisticas-experimentais/27946-divulgacao-semanal-pnadcovid1?t=o-que-e\n\n
    - Microdados. PNAD COVID19. IBGE. https://www.ibge.gov.br/estatisticas/investigacoes-experimentais/estatisticas-experimentais/27946-divulgacao-semanal-pnadcovid1?t=microdados\n\n
    - Informações Técnicas. PNAD COVID19. IBGE. https://www.ibge.gov.br/estatisticas/investigacoes-experimentais/estatisticas-experimentais/27946-divulgacao-semanal-pnadcovid1?t=notas-tecnicas\n\n
    ''')