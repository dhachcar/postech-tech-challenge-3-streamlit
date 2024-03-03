import streamlit as st
from st_pages import show_pages, Page


def output_layout():
    # add_page_title()
    # show_pages_from_config()

# [[pages]]
# path = "main.py"
# name = "Tech Challenge 3"
# icon = ":house:"

# [[pages]]
# path = "pages/intro.py"
# name = "Introdução"
# icon = ":books:"

# [[pages]]
# path = "pages/analise.py"
# name = "Explorações, descobertas e análises"
# icon = ":memo:"

# [[pages]]
# path = "pages/conclusao.py"
# name = "Conclusão"
# icon = ":sparkles:"

# [[pages]]
# path = "pages/refs.py"
# name = "Referências"
# icon = ":globe_with_meridians:"
# is_section = false


    show_pages(
        [
            Page("./main.py", "Tech Challenge 3", ":house:", use_relative_hash=True),
            Page("./pages/intro.py", "Introdução", ":books:", use_relative_hash=True),
            Page("./pages/analise.py", "Explorações, descobertas e análises", ":memo:", use_relative_hash=True),
            Page("./pages/conclusao.py", "Conclusão", ":sparkles:", use_relative_hash=True),
            Page("./pages/refs.py", "Referências", ":globe_with_meridians:", use_relative_hash=True),
        ]
    )

    with st.sidebar:
        st.subheader("Aluno")
        st.text("Danilo Henrique Achcar")
        st.text("RM 351516 | 2DTAT")

        st.divider()

        st.subheader("Instalando as dependências do app")
        st.code(body="pip install -r requirements.txt", language="shell")

        st.divider()

        st.subheader("Executar localmente")
        st.code(body="streamlit run main.py", language="shell")

        st.divider()

        st.subheader("Repositórios do projeto")
        st.link_button(
            "Repositório Streamlit",
            "https://github.com/dhachcar/postech-tech-challenge-3-streamlit",
            help=None,
            type="secondary",
            disabled=False,
            use_container_width=False,
        )
        st.link_button(
            "Repositório Jupyter Notebook",
            "https://github.com/dhachcar/postech-tech-challenge-3",
            help=None,
            type="secondary",
            disabled=False,
            use_container_width=False,
        )

    # with st.spinner('Carregando...'):
    #     time.sleep(1)
    #     st.success("Carregamento concluído!", icon='✅')
