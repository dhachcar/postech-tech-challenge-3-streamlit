import joblib
import pandas as pd
from sklearn.metrics import accuracy_score
import streamlit as st
from tabs.tab import TabInterface

class AnaliseProcessamentoMachineLearningEnsembleTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':blue[Machine Learning]', divider='blue')
            st.markdown('''
                **:blue[XGBoost]**
            ''')

            x_test = pd.read_csv('assets/modelos/ensemble/xgb_x_test.csv')
            y_test = pd.read_csv('assets/modelos/ensemble/xgb_y_test.csv')

            st.dataframe(x_test)
            st.dataframe(y_test)

            def recarrega_modelo_xgb(file: str):
                xgb_recarregado = joblib.load(file)
                xgb_recarregado_previsoes = xgb_recarregado.predict(x_test)
                xgb_recarregado_acuracia = accuracy_score(y_true = y_test, y_pred = xgb_recarregado_previsoes) * 100
                
                st.markdown(f'{xgb_recarregado_acuracia:.2f}%')

                return xgb_recarregado

            xgb1 = recarrega_modelo_xgb('assets/modelos/ensemble/xgb-default.pkl')
            xgb2 = recarrega_modelo_xgb('assets/modelos/ensemble/xgb-sugeridos.pkl')

            # TODO: explicar sobre os 2 modelos
            # TODO: explicar que a acurácia deles se mantém apos a exportação/importação
            # TODO: colocar inputs para teste dos modelos de forma a dizer se o registro tem covid ou nao
            