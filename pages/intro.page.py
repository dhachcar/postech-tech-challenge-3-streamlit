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

    st.page_link("pages/intro.page.py", label="Introdução", icon="🏠")
    st.page_link("pages/index.page.py", label="Índice", icon="1️⃣")
    st.page_link("pages/analise.page.py", label="Análise", icon="2️⃣", disabled=True)
    st.page_link("pages/conclusao.page.py", label="Conclusão", icon="2️⃣", disabled=True)
    st.page_link("pages/refs.page.py", label="Referências", icon="2️⃣", disabled=True)
    st.page_link("http://www.google.com", label="Google", icon="🌎")