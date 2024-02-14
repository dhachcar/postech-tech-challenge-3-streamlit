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
                O Google Cloud Storage é um serviço de armazenamento de objetos na nuvem oferecido pelo Google. Ele permite armazenar e recuperar dados de maneira altamente durável, escalável e segura. O Cloud Storage organiza os dados em "buckets", que são recipientes para armazenar objetos, como arquivos e bases de dados. Esses buckets podem ser configurados com políticas de acesso e retenção para garantir a segurança e conformidade dos dados.\n\n
                Especificamente para este projeto, as bases de dados originais do PNAD COVID19 estão armazenadas num bucket dentro do Google Cloud Storage, integrado ao Google BigQuery para a criação das respectivas tabelas. Desta forma, o BigQuery pode consultar e processar os dados diretamente do Cloud Storage, facilitando o processo de análise e geração de insights.\n\n
                Considerando o contexto do projeto, as bases de dados originais são relativamente grandes para upload manual dentro da plataforma, o que justifica ainda mais a utilização de um armazenamento em nuvem.
            ''')

            st.markdown('**:blue[Bucket]**')
            st.image('assets/img/cloudstorage-bucket.png', caption='Bucket criado dentro do Google Cloud Storage')

            st.markdown('**:blue[Bases de dados CSV dentro do bucket]**')
            st.image('assets/img/cloudstorage-bucket-bases-originais.png', caption='Bases de dados dentro do bucket')
            