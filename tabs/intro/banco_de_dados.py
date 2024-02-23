import streamlit as st
from tabs.tab import TabInterface

class IntroBancoDeDadosTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':blue[Banco de dados]', divider='blue')

            st.image('assets/img/db-schema.png', caption='Diagrama de entidade e relacionamento (ER) do projeto')

            st.image('assets/img/db-transform.png', caption='Etapas de transformação dos dados PNAD COVID19')

            st.markdown('''
                O diagrama cima foi criado utilizando DBML, uma linguagem de marcação baseada em domínio que permite descrever e modelar esquemas de banco de dados de uma forma mais intuitiva e legível. Com o DBML, você pode definir tabelas, colunas, chaves primárias, chaves estrangeiras e outros elementos de um banco de dados de uma maneira que se assemelha mais à forma como você os desenharia em um diagrama. Essa abordagem simplifica o processo de design de banco de dados e facilita a comunicação entre equipes técnicas e não técnicas.
            ''')

            st.code('''
// Docs: https://dbml.dbdiagram.io/docs

// tabelas auxiliares
Table pnad_covid_2020_aux_capital {
  id integer [primary key]
  nome varchar(100)
}

Table pnad_covid_2020_aux_escolaridade {
  id integer [primary key]
  nome varchar(100)
}

Table pnad_covid_2020_aux_medida_restricao {
  id integer [primary key]
  nome varchar(100)
}

Table pnad_covid_2020_aux_raca {
  id integer [primary key]
  nome varchar(100)
}

Table pnad_covid_2020_aux_regiao_metropolitana {
  id integer [primary key]
  nome varchar(100)
}

Table pnad_covid_2020_aux_resposta {
  id integer [primary key]
  nome varchar(100)
}

Table pnad_covid_2020_aux_resultado {
  id integer [primary key]
  nome varchar(100)
}

Table pnad_covid_2020_aux_sexo {
  id integer [primary key]
  nome varchar(100)
}

Table pnad_covid_2020_aux_situacao_domicilio {
  id integer [primary key]
  nome varchar(100)
}

Table pnad_covid_2020_aux_tipo_area {
  id integer [primary key]
  nome varchar(100)
}

Table pnad_covid_2020_aux_uf {
  id integer [primary key]
  nome varchar(100)
}

// tabela principal da PNAD
Table pnad_covid_2020_processado {
  uf integer
  capital integer
  regiao_metropolitana integer
  semana_mes_v1012 integer
  mes_v1013 integer
  situacao_domicilio_v1022 integer
  tipo_area_v1023 integer
  morador_idade_a002 integer
  morador_sexo_a003 integer
  morador_raca_a004 integer
  morador_escolaridade_a005 integer
  sintoma_febre_b0011 integer
  sintoma_tosse_b0012 integer
  sintoma_dor_garganta_b0013 integer
  sintoma_dificuldade_respiracao_b0014 integer
  sintoma_dor_cabeca_b0015 integer
  sintoma_dor_peito_b0016 integer
  sintoma_nausea_b0017 integer
  sintoma_nariz_entupido_b0018 integer
  sintoma_fadiga_b0019 integer
  sintoma_dor_olhos_b00110 integer
  sintoma_perda_olfato_b00111 integer
  sintoma_dor_muscular_b00112 integer
  sintoma_diarreia_b00113 integer
  compareceu_estabelecimento_saude_b002 integer
  sedado_entubado_b006 integer	
  tem_plano_saude_b007 integer	
  resultado_exame_b009b integer	
  medida_restricao_contato_b011 integer
  trabalhou_remoto_c013 integer	
  recebeu_auxilio_emergencial_d0051 integer
}

// relacionamentos
Ref: pnad_covid_2020_processado.uf > pnad_covid_2020_aux_uf.id
Ref: pnad_covid_2020_processado.capital > pnad_covid_2020_aux_capital.id
Ref: pnad_covid_2020_processado.regiao_metropolitana > pnad_covid_2020_aux_regiao_metropolitana.id
Ref: pnad_covid_2020_processado.situacao_domicilio_v1022 > pnad_covid_2020_aux_situacao_domicilio.id
Ref: pnad_covid_2020_processado.tipo_area_v1023 > pnad_covid_2020_aux_tipo_area.id
Ref: pnad_covid_2020_processado.morador_sexo_a003 > pnad_covid_2020_aux_sexo.id
Ref: pnad_covid_2020_processado.morador_raca_a004 > pnad_covid_2020_aux_raca.id
Ref: pnad_covid_2020_processado.morador_escolaridade_a005 > pnad_covid_2020_aux_escolaridade.id

Ref: pnad_covid_2020_processado.compareceu_estabelecimento_saude_b002 > pnad_covid_2020_aux_resposta.id
Ref: pnad_covid_2020_processado.sedado_entubado_b006 > pnad_covid_2020_aux_resposta.id
Ref: pnad_covid_2020_processado.tem_plano_saude_b007 > pnad_covid_2020_aux_resposta.id
Ref: pnad_covid_2020_processado.resultado_exame_b009b > pnad_covid_2020_aux_resultado.id
Ref: pnad_covid_2020_processado.medida_restricao_contato_b011 > pnad_covid_2020_aux_medida_restricao.id
Ref: pnad_covid_2020_processado.trabalhou_remoto_c013 > pnad_covid_2020_aux_resposta.id
Ref: pnad_covid_2020_processado.recebeu_auxilio_emergencial_d0051 > pnad_covid_2020_aux_resposta.id

Ref: pnad_covid_2020_processado.sintoma_febre_b0011 > pnad_covid_2020_aux_resposta.id
Ref: pnad_covid_2020_processado.sintoma_tosse_b0012 > pnad_covid_2020_aux_resposta.id
Ref: pnad_covid_2020_processado.sintoma_dor_garganta_b0013 > pnad_covid_2020_aux_resposta.id
Ref: pnad_covid_2020_processado.sintoma_dificuldade_respiracao_b0014 > pnad_covid_2020_aux_resposta.id
Ref: pnad_covid_2020_processado.sintoma_dor_cabeca_b0015 > pnad_covid_2020_aux_resposta.id
Ref: pnad_covid_2020_processado.sintoma_dor_peito_b0016 > pnad_covid_2020_aux_resposta.id
Ref: pnad_covid_2020_processado.sintoma_nausea_b0017 > pnad_covid_2020_aux_resposta.id
Ref: pnad_covid_2020_processado.sintoma_nariz_entupido_b0018 > pnad_covid_2020_aux_resposta.id
Ref: pnad_covid_2020_processado.sintoma_fadiga_b0019 > pnad_covid_2020_aux_resposta.id
Ref: pnad_covid_2020_processado.sintoma_dor_olhos_b00110 > pnad_covid_2020_aux_resposta.id
Ref: pnad_covid_2020_processado.sintoma_perda_olfato_b00111 > pnad_covid_2020_aux_resposta.id
Ref: pnad_covid_2020_processado.sintoma_dor_muscular_b00112 > pnad_covid_2020_aux_resposta.id
Ref: pnad_covid_2020_processado.sintoma_diarreia_b00113 > pnad_covid_2020_aux_resposta.id
            ''')