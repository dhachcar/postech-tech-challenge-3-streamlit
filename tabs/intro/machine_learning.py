import streamlit as st
from tabs.tab import TabInterface

class IntroMachineLearningTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':blue[Machine Learning]', divider='blue')
            st.markdown('''
                TODO: explicar q será utilizado Algoritmos Não Supervisionados (KMEANS, DBSCAN, etc) via XTREMEBOOST, SPARK ML e BIG QUERY ML, co\n\n
                colocar prints
            ''')