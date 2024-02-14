import streamlit as st
from tabs.tab import TabInterface

class IntroGoogleCloudStorageTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':blue[Google Cloud Storage]', divider='blue')
            st.markdown('''
                TODO: explicar oq é e como estou utilizando... colocar prints dos arquivos + bucket criado
            ''')