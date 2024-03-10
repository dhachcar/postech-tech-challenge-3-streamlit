import streamlit as st
from util.layout import output_layout

st.set_page_config(page_title="Conclusão | Tech Challenge 3 | FIAP", layout="wide")
output_layout()

with st.container():
    st.header(":orange[Conclusão]")

    st.subheader(":blue[A respeito dos dados demográficos e clínicos]", divider="blue")
    st.markdown(
        """
        Conforme observado nos dados da PNAD 2020, uma tendência preocupante se destaca: indivíduos com menor grau de escolaridade tendem a apresentar maiores índices de infecção por COVID-19. Esta correlação pode ser atribuída, em parte, ao fato de que trabalhos que exigem menor escolaridade geralmente envolvem tarefas mais manuais e uma maior interação social, aumentando assim o risco de exposição ao vírus.\n
        Além disso, muitas das pessoas entrevistadas pela PNAD 2020 não possuem um plano de saúde adequado que possa auxiliá-las em momentos de necessidade. Esta falta de acesso a cuidados médicos adequados pode amplificar os desafios enfrentados por aqueles em situações socioeconômicas desfavorecidas, tornando-os mais vulneráveis ​​a complicações de saúde, especialmente durante uma pandemia como a COVID-19.\n
        Essas descobertas destacam a importância de abordagens equitativas na educação em saúde e no acesso aos serviços de saúde. Investir em programas educacionais que promovam a conscientização sobre medidas preventivas e garantir o acesso universal a cuidados médicos de qualidade são passos essenciais para proteger as comunidades mais vulneráveis e promover a saúde pública como um todo.
    """
    )

    st.subheader(":blue[A respeito do modelo XGBoost]", divider="blue")
    st.markdown(
        """
        Além disso, é importante destacar que o modelo XGBoost (ou suas variantes, conforme aplicável) desenvolvido durante esta análise poderia desempenhar um papel crucial em futuras pandemias de COVID-19. Ao permitir a identificação mais rápida e automatizada de casos positivos da doença, o modelo poderia agilizar significativamente o processo de triagem e diagnóstico.\n
        Com uma detecção precoce e eficiente, os pacientes infectados poderiam receber atendimento e cuidados mais rápidos, reduzindo assim a propagação do vírus e potencialmente salvando vidas. Além disso, essa abordagem também poderia ajudar os sistemas de saúde a gerenciar melhor seus recursos, direcionando-os para onde são mais necessários e priorizando o tratamento daqueles em maior risco.\n
        Portanto, o desenvolvimento e a implementação de modelos de aprendizado de máquina, como o XGBoost, representam uma ferramenta promissora para fortalecer a capacidade de resposta a pandemias futuras, fornecendo uma abordagem mais ágil e eficaz na identificação e gestão de casos de doenças infecciosas emergentes.
    """
    )

    st.subheader(
        ":blue[A respeito dos modelos KMeans (scikit-learn & BigQuery)]", divider="blue"
    )

    st.markdown(
            """
            <br/><br/><br/><br/><br/><br/>
            <small>*O processo de criação e evolução deste projeto foi, sem dúvida, desafiador em vários sentidos, mas ao mesmo tempo foi uma experiência divertida e altamente educativa. Devido ao foco principal do TechChallenge da fase 2 estar em séries temporais, tive menos oportunidades para explorar algoritmos de Machine Learning de outras categorias, como ensemble e unsupervised (utilizados neste projeto). No entanto, consegui assimilar diversos conceitos que foram abordados pelos professores, confirmando a importância da prática para uma compreensão mais profunda das coisas. No final das contas, o projeto se mostrou uma jornada muito gratificante!<br/><b>:blue[&ndash; Danilo H. Achcar &ndash;]</b>*</small>
        """,
        unsafe_allow_html=True
    )
