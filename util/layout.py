import streamlit as st
from st_pages import show_pages_from_config, add_page_title
import time

def output_layout():
    # add_page_title()
    show_pages_from_config()

    with st.sidebar:
        st.subheader('Instalando as dependências do app')
        st.code(body='pip install -r requirements.txt', language='shell')

        st.divider()

        st.subheader('Repositórios do projeto')
        st.link_button('Repositório Streamlit', 'https://github.com/dhachcar/postech-tech-challenge-3-streamlit', help=None, type="secondary", disabled=False, use_container_width=False)
        st.link_button('Repositório Jupyter Notebook', 'https://github.com/dhachcar/postech-tech-challenge-3', help=None, type="secondary", disabled=False, use_container_width=False)

        st.divider()

        st.subheader('Aluno')
        st.text('Danilo Henrique Achcar')
        st.text('RM 351516 | 2DTAT')

    with st.spinner('Carregando...'):
        time.sleep(1)
        st.success("Carregamento concluído!", icon='✅')