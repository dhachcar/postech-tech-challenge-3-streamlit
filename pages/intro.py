import streamlit as st
from tabs.intro.apache_spark_tab import IntroApacheSparkTab
from tabs.intro.arquitetura import IntroArquiteturaTab
from tabs.intro.banco_de_dados import IntroBancoDeDadosTab
from tabs.intro.google_bigquery_tab import IntroGoogleBigQueryTab
from tabs.intro.google_cloud_storage_tab import IntroGoogleCloudStorageTab
from tabs.intro.machine_learning_tab import IntroMachineLearningTab
from util.layout import output_layout
from tabs.intro.pnad_tab import IntroPnadTab

st.set_page_config(page_title="Introdução | Tech Challenge 3 | FIAP", layout='wide')
output_layout()

with st.container():
    st.header(':orange[Introdução]')

    tab0, tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(tabs=['PNAD COVID19', 'Arquitetura', 'Banco de dados', 'Apache Spark', 'Google BigQuery', 'Google Cloud Storage', 'Machine Learning'])

    IntroPnadTab(tab0)
    IntroArquiteturaTab(tab1)
    IntroBancoDeDadosTab(tab2)
    IntroApacheSparkTab(tab3)
    IntroGoogleBigQueryTab(tab4)
    IntroGoogleCloudStorageTab(tab5)
    IntroMachineLearningTab(tab6)