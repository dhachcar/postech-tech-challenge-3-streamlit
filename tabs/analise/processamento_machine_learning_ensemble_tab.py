import joblib
import pandas as pd
from sklearn.metrics import accuracy_score
import streamlit as st
from tabs.tab import TabInterface
import time

class AnaliseProcessamentoMachineLearningEnsembleTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":blue[Machine Learning]", divider="blue")
            st.markdown(
                """
                **:blue[XGBoost]**\n
                A seguir, é possível preencher os sintomas de um entrevistado e executar a previsão para o resultado de seu exame. Os resultados possíveis são:
                * Positivo
                * Negativo
                * Inconclusivo

                Além disso, a previsão irá rodar em :blue[2 modelos XGB distintos] (cada um criado com parâmetros diferentes).
            """
            )

            x_test = pd.read_csv("assets/modelos/ensemble/xgb_x_test.csv")
            y_test = pd.read_csv("assets/modelos/ensemble/xgb_y_test.csv")
            df_resultado_exame = pd.read_csv("assets/csv/resultado-exame.csv")

            def recarrega_modelo_xgb(file: str):
                xgb_recarregado = joblib.load(file)
                xgb_recarregado_previsoes = xgb_recarregado.predict(x_test)
                xgb_recarregado_acuracia = (
                    accuracy_score(y_true=y_test, y_pred=xgb_recarregado_previsoes)
                    * 100
                )

                return (xgb_recarregado, xgb_recarregado_acuracia)

            # st.markdown(f"{xgb_recarregado_acuracia:.2f}%")

            xgb1, xgb1_acuracia = recarrega_modelo_xgb(
                "assets/modelos/ensemble/xgb-default.pkl"
            )
            xgb2, xgb2_acuracia = recarrega_modelo_xgb(
                "assets/modelos/ensemble/xgb-sugeridos.pkl"
            )

            lista_respostas_sintoma = {1: "Sim", 2: "Nâo", 9: "Ignorado"}

            with st.container():
                _, col1, col2, _ = st.columns([2, 1, 1, 2])

                with col1:
                    st.metric(
                        label="XGB 1 (parâmetros default)",
                        value=f"{xgb1_acuracia:,.2f}%",
                        delta=f"{(xgb1_acuracia - xgb2_acuracia):,.2f}%",
                    )

                with col2:
                    st.metric(
                        label="XGB 2 (parâmetros sugeridos)",
                        value=f"{xgb2_acuracia:,.2f}%",
                        delta=f"{(xgb2_acuracia - xgb1_acuracia):,.2f}%",
                    )

            with st.container():
                col1, col2, col3, col4, col5, col6, col7 = st.columns(
                    [1, 1, 1, 1, 1, 1, 1]
                )

                with col1:
                    sintoma_febre = st.selectbox(
                        "Febre",
                        options=list(lista_respostas_sintoma.keys()),
                        format_func=(lambda opt: lista_respostas_sintoma[opt]),
                    )

                with col2:
                    sintoma_tosse = st.selectbox(
                        "Tosse",
                        options=list(lista_respostas_sintoma.keys()),
                        format_func=(lambda opt: lista_respostas_sintoma[opt]),
                    )

                with col3:
                    sintoma_dor_garganta = st.selectbox(
                        "Dor de garganta",
                        options=list(lista_respostas_sintoma.keys()),
                        format_func=(lambda opt: lista_respostas_sintoma[opt]),
                    )

                with col4:
                    sintoma_dificuldade_respiracao = st.selectbox(
                        "Dificuldade para respirar",
                        options=list(lista_respostas_sintoma.keys()),
                        format_func=(lambda opt: lista_respostas_sintoma[opt]),
                    )

                with col5:
                    sintoma_dor_cabeca = st.selectbox(
                        "Dor de cabeça",
                        options=list(lista_respostas_sintoma.keys()),
                        format_func=(lambda opt: lista_respostas_sintoma[opt]),
                    )

                with col6:
                    sintoma_dor_peito = st.selectbox(
                        "Dor no peito",
                        options=list(lista_respostas_sintoma.keys()),
                        format_func=(lambda opt: lista_respostas_sintoma[opt]),
                    )

                with col7:
                    sintoma_diarreia = st.selectbox(
                        "Diarréia",
                        options=list(lista_respostas_sintoma.keys()),
                        format_func=(lambda opt: lista_respostas_sintoma[opt]),
                    )

            with st.container():
                col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 1, 1, 1, 1])

                with col1:
                    sintoma_nausea = st.selectbox(
                        "Náusea",
                        options=list(lista_respostas_sintoma.keys()),
                        format_func=(lambda opt: lista_respostas_sintoma[opt]),
                    )

                with col2:
                    sintoma_nariz_entupido = st.selectbox(
                        "Nariz entupido",
                        options=list(lista_respostas_sintoma.keys()),
                        format_func=(lambda opt: lista_respostas_sintoma[opt]),
                    )

                with col3:
                    sintoma_fadiga = st.selectbox(
                        "Fadiga",
                        options=list(lista_respostas_sintoma.keys()),
                        format_func=(lambda opt: lista_respostas_sintoma[opt]),
                    )

                with col4:
                    sintoma_dor_nos_olhos = st.selectbox(
                        "Dor nos olhos",
                        options=list(lista_respostas_sintoma.keys()),
                        format_func=(lambda opt: lista_respostas_sintoma[opt]),
                    )

                with col5:
                    sintoma_perda_olfato = st.selectbox(
                        "Perda de olfato",
                        options=list(lista_respostas_sintoma.keys()),
                        format_func=(lambda opt: lista_respostas_sintoma[opt]),
                    )

                with col6:
                    sintoma_dor_muscular = st.selectbox(
                        "Dor muscular",
                        options=list(lista_respostas_sintoma.keys()),
                        format_func=(lambda opt: lista_respostas_sintoma[opt]),
                    )

            def predict():
                df_query = pd.DataFrame(
                    columns=[
                        "sintoma_febre_b0011",
                        "sintoma_tosse_b0012",
                        "sintoma_dor_garganta_b0013",
                        "sintoma_dificuldade_respiracao_b0014",
                        "sintoma_dor_cabeca_b0015",
                        "sintoma_dor_peito_b0016",
                        "sintoma_nausea_b0017",
                        "sintoma_nariz_entupido_b0018",
                        "sintoma_fadiga_b0019",
                        "sintoma_dor_olhos_b00110",
                        "sintoma_perda_olfato_b00111",
                        "sintoma_dor_muscular_b00112",
                        "sintoma_diarreia_b00113",
                    ]
                )

                df_query.loc[len(df_query)] = {
                    "sintoma_febre_b0011": sintoma_febre,
                    "sintoma_tosse_b0012": sintoma_tosse,
                    "sintoma_dor_garganta_b0013": sintoma_dor_garganta,
                    "sintoma_dificuldade_respiracao_b0014": sintoma_dificuldade_respiracao,
                    "sintoma_dor_cabeca_b0015": sintoma_dor_cabeca,
                    "sintoma_dor_peito_b0016": sintoma_dor_peito,
                    "sintoma_nausea_b0017": sintoma_nausea,
                    "sintoma_nariz_entupido_b0018": sintoma_nariz_entupido,
                    "sintoma_fadiga_b0019": sintoma_fadiga,
                    "sintoma_dor_olhos_b00110": sintoma_dor_nos_olhos,
                    "sintoma_perda_olfato_b00111": sintoma_perda_olfato,
                    "sintoma_dor_muscular_b00112": sintoma_dor_muscular,
                    "sintoma_diarreia_b00113": sintoma_diarreia,
                }

                st.markdown(
                    """
                    **:blue[Matriz de input para o modelo]**
                """
                )
                st.dataframe(df_query)

                xgb1_previsao = xgb1.predict(df_query)
                xgb2_previsao = xgb2.predict(df_query)

                def obtem_resultado_final(previsao):
                    df_resultado_categoria = df_resultado_exame[
                        df_resultado_exame["id"] == previsao[0]
                    ]

                    # qualquer ID > 3, define como 'Inconclusivo' por padrão
                    if df_resultado_categoria.head(1).id.values[0] > 3:
                        return "Inconclusivo"
                    else:
                        return df_resultado_categoria.nome.values[0]

                xgb1_resultado = obtem_resultado_final(xgb1_previsao)
                xgb2_resultado = obtem_resultado_final(xgb2_previsao)

                st.subheader(":blue[Resultados]", divider="blue")

                with st.container():
                    _, col1, col2, _ = st.columns([2, 1, 1, 2])

                    with col1:
                        st.metric(
                            label="XGB 1 (parâmetros default)", value=xgb1_resultado
                        )

                    with col2:
                        st.metric(
                            label="XGB 2 (parâmetros sugeridos)", value=xgb2_resultado
                        )

            if st.button("Entrevistado com COVID19?"):
                with st.spinner('Processando...'):
                    time.sleep(3)
                    predict()
                    st.success("Processamento concluído!")

            # st.write(f"You selected option {option} called {lista_respostas_sintoma[option]}")

            # TODO: explicar sobre os 2 modelos
            # TODO: explicar que a acurácia deles se mantém apos a exportação/importação
            # TODO: colocar inputs para teste dos modelos de forma a dizer se o registro tem covid ou nao
