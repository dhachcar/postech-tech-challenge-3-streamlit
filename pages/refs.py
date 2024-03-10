import streamlit as st
from util.layout import output_layout

st.set_page_config(page_title="Referências | Tech Challenge 3 | FIAP", layout='wide')
output_layout()

with st.container():
    st.header(':orange[Referências bibliográficas]')

    st.markdown('''
    1) ALGHOFAILI, Y. Interpretable K-Means: Clusters Feature Importances. 2021. Disponível em: https://towardsdatascience.com/interpretable-k-means-clusters-feature-importances-7e516eeb8d3c. Acesso em 08/03/2024.
    2) Apache. Apache Spark. Disponível em: https://spark.apache.org/. Acesso em 21/01/2024.
    3) DBDiagram. Ferramenta para criação de diagrams DER. Disponível em: https://dbdiagram.io/d. Acesso em 23/01/2024.
    4) DBDiagram. DBML - Full Syntax Docs. Disponível em: https://dbml.dbdiagram.io/docs/. Acesso em 02/02/2024.
    5) FERNANDES, L. Perform an Exploratory Data Analysis. 2020. Disponível em: https://openclassrooms.com/en/courses/5869986-perform-an-exploratory-data-analysis/6177861-analyze-the-results-of-a-k-means-clustering. Acesso em: 09/03/2024.
    6) DMLC. XGBoost. 2022. Disponível em: https://xgboost.readthedocs.io/en/stable/index.html. Acesso em 26/02/2024.
    7) Draw.io. Ferramenta para criação de diagramas genéricos. Disponível em: https://app.diagrams.net/. Acesso em 24/02/2024.
    8) GÓES, G. S., MARTINS, F. S., NASCIMENTO, J. A. S. O trabalho remoto e a pandemia: o que a pnad covid- 19 nos mostrou. 2021. Disponível em: https://repositorio.ipea.gov.br/bitstream/11058/10472/6/CC_50_mt_trabalho_remoto_e_a_pandemia.pdf. Acesso em 17/02/2024.
    9) Google. Criar um modelo k-means para agrupar o conjunto de dados de locações de bicicletas de Londres. Disponível em: https://cloud.google.com/bigquery/docs/kmeans-tutorial?hl=pt-br. Acesso em 07/03/2024.
    10) Google. Google Big Query. 2024. Disponível em: https://cloud.google.com/bigquery. Acesso em 08/02/2024.
    11) Google. Google Cloud Storage. 2024. Disponível em: https://cloud.google.com/storage. Acesso em 08/02/2024.
    12) Google. Google Dataproc Tutorial. 2024. https://cloud.google.com/dataproc/docs/tutorials/bigquery-sparkml?hl=pt-br. Acesso em 09/02/2024.
    13) GUANGYANG, L. Waffle charts (square pie) in matplotlib with pywaffle. 2023. Disponível em: https://python-charts.com/part-whole/waffle-chart-matplotlib/. Acesso em 13/02/2024.
    14) HUBERT, L., ARABIE, P. scikit-Learn. 2024. Disponível em: https://scikit-learn.org/stable/modules/clustering.html#silhouette-coefficient. Acesso em 25/02/2024.
    15) HUBERT, L., ARABIE, P. scikit-Learn. 2024. Disponível em: https://scikit-learn.org/stable/modules/clustering.html#davies-bouldin-index. Acesso em 25/02/2024.
    16) HUBERT, L., ARABIE, P. scikit-Learn. 2024. Disponível em: https://scikit-learn.org/stable/modules/clustering.html#calinski-harabasz-index. Acesso em 25/02/2024.
    17) IBGE. PNAD COVID-19 - O que é. 2020. Disponível em: https://www.ibge.gov.br/estatisticas/investigacoes-experimentais/estatisticas-experimentais/27946-divulgacao-semanal-pnadcovid1?t=o-que-e. Acesso em 27/01/2024.
    18) IBGE. PNAD COVID-19 - Microdados. 2020. Disponível em: https://www.ibge.gov.br/estatisticas/investigacoes-experimentais/estatisticas-experimentais/27946-divulgacao-semanal-pnadcovid1?t=microdados. Acesso em 27/01/2024.
    19) IBGE. PNAD COVID-19 - Informações Técnicas. 2020. Disponível em: https://www.ibge.gov.br/estatisticas/investigacoes-experimentais/estatisticas-experimentais/27946-divulgacao-semanal-pnadcovid1?t=notas-tecnicas. Acesso em 28/01/2024.
    20) JAIN, A. Practical Approach to KMeans Clustering — Python and Why Scaling is Important. 2019. Disponível em: https://medium.com/analytics-vidhya/practical-approach-to-kmeans-clustering-python-and-why-scaling-is-important-44ac0b0fea47. Acesso em 09/03/2024.
    21) Streamlit. Streamlit Documentation. Disponível em: https://docs.streamlit.io/. Acesso em 18/02/2024.
    22) SUKUMAR, H. Inforiver. 11 Pie chart alternatives and when to use them. Disponível em: https://inforiver.com/insights/11-pie-chart-alternatives-and-when-to-use-them/. Acesso em 15/02/2024.
    ''')
