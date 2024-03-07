import streamlit as st
from util.layout import output_layout

st.set_page_config(page_title="Referências | Tech Challenge 3 | FIAP", layout='wide')
output_layout()

with st.container():
    st.header(':orange[Referências bibliográficas]')

    st.markdown('''
    - O que é. PNAD COVID-19. IBGE. Disponível em: https://www.ibge.gov.br/estatisticas/investigacoes-experimentais/estatisticas-experimentais/27946-divulgacao-semanal-pnadcovid1?t=o-que-e\n\n
    - Microdados. PNAD COVID-19. IBGE. Disponível em: https://www.ibge.gov.br/estatisticas/investigacoes-experimentais/estatisticas-experimentais/27946-divulgacao-semanal-pnadcovid1?t=microdados\n\n
    - Informações Técnicas. PNAD COVID-19. IBGE. Disponível em: https://www.ibge.gov.br/estatisticas/investigacoes-experimentais/estatisticas-experimentais/27946-divulgacao-semanal-pnadcovid1?t=notas-tecnicas\n\n
    - Apache Spark. Apache. Disponível em: https://spark.apache.org/
    - Google Big Query. Google. Disponível em: https://cloud.google.com/bigquery
    - Google Cloud Storage. Google. Disponível em: https://cloud.google.com/storage
    - Google Dataproc Tutorial. Google. https://cloud.google.com/dataproc/docs/tutorials/bigquery-sparkml?hl=pt-br
    - Streamlit Documentation. Streamlit . Disponível em: https://docs.streamlit.io/
    - https://inforiver.com/insights/11-pie-chart-alternatives-and-when-to-use-them/
    - https://dbdiagram.io/d
    - https://dbml.dbdiagram.io/docs/
    - https://app.diagrams.net/
    - https://cloud.google.com/bigquery/docs/kmeans-tutorial?hl=pt-br
    - https://xgboost.readthedocs.io/en/stable/index.html
    - https://python-charts.com/part-whole/waffle-chart-matplotlib/
    - https://scikit-learn.org/stable/modules/clustering.html#silhouette-coefficient
    - https://scikit-learn.org/stable/modules/clustering.html#davies-bouldin-index
    - https://scikit-learn.org/stable/modules/clustering.html#calinski-harabasz-index
    - https://repositorio.ipea.gov.br/bitstream/11058/10472/6/CC_50_mt_trabalho_remoto_e_a_pandemia.pdf
    ''')