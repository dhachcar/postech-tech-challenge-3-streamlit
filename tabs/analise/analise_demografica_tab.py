import streamlit as st
from tabs.tab import TabInterface
import plotly.graph_objs as go
import pandas as pd

class AnaliseDemograficaTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':blue[Análise demográfica]', divider='blue')

            st.markdown('''
                **:blue[Por sexo]**
            ''')

            sexo_cores = ["#983D3D", "#232066"]
            df_pnad_sexo = pd.read_csv('assets/segmentacoes/segmentacao-sexo.csv')

            col1, col2 = st.columns([1, 1])

            with col1:
                fig = go.Figure()
                fig.add_trace(go.Pie(labels=df_pnad_sexo.nome, values=df_pnad_sexo.total, hole=.65, marker=dict(colors=sexo_cores)))
                fig.update_layout(title='Segmentação dos entrevistados por sexo', width=400)
                st.plotly_chart(fig)

            with col2:
                st.image('assets/img/analise-segmentacao-sexo-1.png', caption='Gráfico de waffle')