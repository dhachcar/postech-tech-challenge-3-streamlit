import streamlit as st
import time
import joblib
import pandas as pd
import numpy as np
from tabs.tab import TabInterface
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


class AnaliseProcessamentoMachineLearningUnsupervisedTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":blue[Modelo KMeans]", divider="blue")
            st.markdown(
                """
                O propósito principal do modelo KMeans aplicado neste projeto, reside na sua capacidade de categorizar os entrevistados em um dos cinco grupos previamente identificados. Esse processo de agrupamento facilita a análise dos dados obtidos nas entrevistas, possibilitando a extração de insights significativos e a identificação de padrões relevantes no comportamento ou nas características dos entrevistados.\n
                Com isso, foram definidos cinco grupos distintos ou centroides numerados de 0 a 4, representando as diferentes regiões de agrupamento dos dados. Para definir a quantidade de grupos, foi utilizado o método Elbow junto de algumas métricas de dispersão, dentre elas:
                * [Silhouete](https://scikit-learn.org/stable/modules/clustering.html#silhouette-coefficient)
                * [Davies Bouldin](https://scikit-learn.org/stable/modules/clustering.html#davies-bouldin-index)
                * [Calinski Harabasz](https://scikit-learn.org/stable/modules/clustering.html#calinski-harabasz-index)
                
                Todos os entrevistados serão inseridos em 1 dos 5 grupos.\n
                Preencha os campos abaixo para especificar em qual grupo o entrevistado será designado.
            """
            )

            # TODO: mostrar um grafico dos grupos (plotly ou img?)

            lista_respostas_sintoma = {1: "Sim", 2: "Não"}
            lista_resultado_exame = {
                1: "Positivo",
                2: "Negativo",
                3: "Inconclusivo",
                4: "Ainda não recebeu o resultado",
                9: "Ignorado",
            }
            lista_respostas_outros_campos = {1: "Sim", 2: "Nâo", 9: "Ignorado"}

            kmeans = joblib.load("assets/modelos/unsupervised/kmeans.pkl")
            scaler = joblib.load("assets/modelos/unsupervised/standard-scaler.pkl")
            pca = joblib.load("assets/modelos/unsupervised/pca.pkl")

            with st.container():
                st.markdown("**:blue[Sintomas leves]**")

                col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(
                    [1, 1, 1, 1, 1, 1, 1, 1]
                )

                with col1:
                    sintoma_dor_garganta = st.selectbox(
                        "Dor de garganta",
                        key="unsupervised_sintoma_dor_garganta",
                        options=list(lista_respostas_sintoma.keys()),
                        format_func=(lambda opt: lista_respostas_sintoma[opt]),
                    )

                with col2:
                    sintoma_dor_cabeca = st.selectbox(
                        "Dor de cabeça",
                        key="unsupervised_sintoma_dor_cabeca",
                        options=list(lista_respostas_sintoma.keys()),
                        format_func=(lambda opt: lista_respostas_sintoma[opt]),
                    )

                with col3:
                    sintoma_nausea = st.selectbox(
                        "Náusea",
                        key="unsupervised_sintoma_nausea",
                        options=list(lista_respostas_sintoma.keys()),
                        format_func=(lambda opt: lista_respostas_sintoma[opt]),
                    )

                with col4:
                    sintoma_nariz_entupido = st.selectbox(
                        "Nariz entupido",
                        key="unsupervised_sintoma_nariz_entupido",
                        options=list(lista_respostas_sintoma.keys()),
                        format_func=(lambda opt: lista_respostas_sintoma[opt]),
                    )

                with col5:
                    sintoma_fadiga = st.selectbox(
                        "Fadiga",
                        key="unsupervised_sintoma_fadiga",
                        options=list(lista_respostas_sintoma.keys()),
                        format_func=(lambda opt: lista_respostas_sintoma[opt]),
                    )

                with col6:
                    sintoma_dor_nos_olhos = st.selectbox(
                        "Dor nos olhos",
                        key="unsupervised_sintoma_dor_olhos",
                        options=list(lista_respostas_sintoma.keys()),
                        format_func=(lambda opt: lista_respostas_sintoma[opt]),
                    )

                with col7:
                    sintoma_perda_olfato = st.selectbox(
                        "Perda de olfato",
                        key="unsupervised_sintoma_perda_olfato",
                        options=list(lista_respostas_sintoma.keys()),
                        format_func=(lambda opt: lista_respostas_sintoma[opt]),
                    )

                with col8:
                    sintoma_diarreia = st.selectbox(
                        "Diarréia",
                        key="unsupervised_sintoma_diarreia",
                        options=list(lista_respostas_sintoma.keys()),
                        format_func=(lambda opt: lista_respostas_sintoma[opt]),
                    )

            with st.container():
                st.markdown("**:blue[Sintomas médios]**")

                col1, col2, col3, _, _, _ = st.columns([1, 1, 1, 1, 1, 1])

                with col1:
                    sintoma_febre = st.selectbox(
                        "Febre",
                        key="unsupervised_sintoma_febre",
                        options=list(lista_respostas_sintoma.keys()),
                        format_func=(lambda opt: lista_respostas_sintoma[opt]),
                    )

                with col2:
                    sintoma_tosse = st.selectbox(
                        "Tosse",
                        key="unsupervised_sintoma_tosse",
                        options=list(lista_respostas_sintoma.keys()),
                        format_func=(lambda opt: lista_respostas_sintoma[opt]),
                    )

                with col3:
                    sintoma_dor_muscular = st.selectbox(
                        "Dor muscular",
                        key="unsupervised_sintoma_dor_muscular",
                        options=list(lista_respostas_sintoma.keys()),
                        format_func=(lambda opt: lista_respostas_sintoma[opt]),
                    )

            with st.container():
                st.markdown("**:blue[Sintomas graves]**")

                col1, col2, _, _, _, _ = st.columns([1, 1, 1, 1, 1, 1])

                with col1:
                    sintoma_dificuldade_respiracao = st.selectbox(
                        "Dificuldade para respirar",
                        key="unsupervised_sintoma_dificuldade_respirar",
                        options=list(lista_respostas_sintoma.keys()),
                        format_func=(lambda opt: lista_respostas_sintoma[opt]),
                    )

                with col2:
                    sintoma_dor_peito = st.selectbox(
                        "Dor no peito",
                        key="unsupervised_sintoma_dor_peito",
                        options=list(lista_respostas_sintoma.keys()),
                        format_func=(lambda opt: lista_respostas_sintoma[opt]),
                    )

            with st.container():
                st.markdown("**:blue[Outros dados]**")

                col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

                with col1:
                    resultado_exame = st.selectbox(
                        "Resultado exame",
                        key="unsupervised_resultado_exame",
                        options=list(lista_resultado_exame.keys()),
                        format_func=(lambda opt: lista_resultado_exame[opt]),
                    )

                with col2:
                    fez_homeoffice = st.selectbox(
                        "Fez homeoffice",
                        key="unsupervised_fez_homeoffice",
                        options=list(lista_respostas_outros_campos.keys()),
                        format_func=(lambda opt: lista_respostas_outros_campos[opt]),
                    )

                with col3:
                    tem_plano = st.selectbox(
                        "Tem plano de saúde",
                        key="unsupervised_plano_saude",
                        options=list(lista_respostas_outros_campos.keys()),
                        format_func=(lambda opt: lista_respostas_outros_campos[opt]),
                    )

                with col4:
                    entubado = st.selectbox(
                        "Foi entubado/sedado",
                        key="unsupervised_entubado",
                        options=list(lista_respostas_outros_campos.keys()),
                        format_func=(lambda opt: lista_respostas_outros_campos[opt]),
                    )

            # função para fazer a predição
            def predict():
                colunas = [
                    "homeoffice",
                    "tem_plano",
                    "entubado",
                    "resultado_exame",
                    "tem_sintomas_leves",
                    "tem_sintomas_medios",
                    "tem_sintomas_graves",
                    "total_sintomas_leves",
                    "total_sintomas_medios",
                    "total_sintomas_graves",
                    "total_sintomas",
                ]

                # junta todos os inputs
                sintomas_leves = np.array(
                    [
                        int(sintoma_dor_garganta),
                        sintoma_dor_cabeca,
                        sintoma_nausea,
                        sintoma_nariz_entupido,
                        sintoma_fadiga,
                        sintoma_dor_nos_olhos,
                        sintoma_perda_olfato,
                        sintoma_diarreia,
                    ]
                )
                sintomas_medios = np.array(
                    [sintoma_febre, sintoma_tosse, sintoma_dor_muscular]
                )
                sintomas_graves = np.array(
                    [sintoma_dificuldade_respiracao, sintoma_dor_peito]
                )
                qtd_sintomas_leves = np.sum(sintomas_leves == 1)
                qtd_sintomas_medios = np.sum(sintomas_medios == 1)
                qtd_sintomas_graves = np.sum(sintomas_graves == 1)
                tem_sintomas_leves = qtd_sintomas_leves > 0
                tem_sintomas_medios = qtd_sintomas_medios > 0
                tem_sintomas_graves = qtd_sintomas_graves > 0

                X = pd.DataFrame(columns=colunas)
                X["homeoffice"] = np.array([fez_homeoffice])
                X["tem_plano"] = np.array([tem_plano])
                X["entubado"] = np.array([entubado])
                X["resultado_exame"] = np.array([resultado_exame])
                X["tem_sintomas_leves"] = np.array([tem_sintomas_leves])
                X["tem_sintomas_medios"] = np.array([tem_sintomas_medios])
                X["tem_sintomas_graves"] = np.array([tem_sintomas_graves])
                X["total_sintomas_leves"] = np.array([qtd_sintomas_leves])
                X["total_sintomas_medios"] = np.array([qtd_sintomas_medios])
                X["total_sintomas_graves"] = np.array([qtd_sintomas_graves])
                X["total_sintomas"] = np.array(
                    [qtd_sintomas_leves + qtd_sintomas_medios + qtd_sintomas_graves]
                )

                # aplica o scaler
                X_scaled = scaler.transform(X)

                # aplica o PCA
                X_pca = pca.transform(X_scaled)

                # faz a previsão
                previsao = kmeans.predict(X_pca)

                st.markdown(
                    """
                    **:blue[Matriz de input para o modelo]**
                """
                )

                st.dataframe(X)

                st.subheader(":blue[Resultados]", divider="blue")

                st.markdown(
                        f"""
                        :orange[Grupo sugerido: <big><b>{previsao[0]}</b></big>]
                    """,
                    unsafe_allow_html=True,
                )

            if st.button("Calcular grupo do entrevistado"):
                with st.spinner("Processando..."):
                    time.sleep(3)
                    predict()
                    st.success("Processamento concluído!")
