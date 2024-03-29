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
        Além disso, muitas das pessoas entrevistadas pela PNAD 2020 não possuem um plano de saúde adequado que possa auxiliá-las em momentos de necessidade. Esta falta de acesso a cuidados médicos adequados pode aumentar os desafios enfrentados por aqueles em situações socioeconômicas desfavorecidas, tornando-os mais vulneráveis ​​a complicações de saúde, especialmente durante uma pandemia como a COVID-19.\n
        Essas descobertas destacam a importância de abordagens eficientes na questão da educação e principalmente no acesso à serviços de saúde. Garantir o acesso universal a cuidados médicos de qualidade são passos essenciais para proteger as comunidades mais vulneráveis e promover a saúde pública como um todo.
    """
    )

    st.subheader(":blue[A respeito do modelo XGBoost]", divider="blue")
    st.markdown(
        """
        É importante destacar que o modelo :blue[XGBoost] (ou suas variantes, conforme aplicável) desenvolvido durante esta análise poderia desempenhar um papel crucial em futuras pandemias de COVID-19. Ao permitir a identificação mais rápida e automatizada de casos positivos da doença, o processo de triagem e diagnóstico se torna mais ágil.\n
        Com uma detecção precoce e eficiente, os pacientes infectados poderiam receber atendimento e cuidados mais rápidos, reduzindo assim a propagação do vírus e até mesmo podendo salvar vidas. Além disso, essa abordagem também poderia ajudar os sistemas de saúde a gerenciar melhor seus recursos, direcionando-os para onde são mais necessários e priorizando o tratamento daqueles em maior risco. Modelos de machine learning, como o :blue[XGBoost], representam uma oportunidade de melhoria no combate a pandemias futuras.
    """
    )

    st.subheader(
        ":blue[A respeito dos modelos KMeans (scikit-learn & BigQuery)]", divider="blue"
    )
    st.markdown(
        """
        Para compreender melhor as características dos dados da PNAD, foi empregado o algoritmo :blue[KMeans] na análise. Este algoritmo foi escolhido por sua capacidade de agrupar os dados em clusters ou grupos distintos com base em suas similaridades.\n
        Ao aplicar tal algoritmo, os entrevistados da PNAD foram designados em 5 grupos distintos, conforme o objetivo da análise. Essa abordagem permite identificar padrões nos dados da PNAD, revelando insights valiosos sobre diferentes perfis de entrevistados. Por exemplo, podemos observar grupos distintos com base em características demográficas, socioeconômicas ou de saúde, e tais grupos também fornecem uma visão mais mais apurada da população entrevistada.  
    """
    )

    st.subheader(
        ":blue[Sugestões de enfrentamento para uma nova pandemia]", divider="blue"
    )
    st.markdown(
       """
       Considerando todo o material analisado e modelos criados, as sugestões finais deste projeto são as seguintes:
       1) Utilizar um modelo de classificação para agilizar o processo de identificação de pessoas com COVID-19;
       2) Utilizar um modelo de clusterização para segmentar as pessoas em grupos bem distintos que permitam a criação de estratégias e políticas específicas para cada um;
       3) Criar políticas de saúde pública voltadas ao enfretamento de novas pandemias e auxilio àquelas pessoas que não possuem o benefício do homeoffice;
       4) Estabelecer parcerias entre governo e operadoras de planos de saúde em épocas de pandemia, as quais permitam que a população menos favorecida tenha acesso facilitado à diagnósticos e tratamentos de qualidade.
    """
    )

    st.markdown(
        """
            <br/><br/><br/>
            <small>*:orange[Nota final:] O processo de criação e evolução deste projeto foi, sem dúvida, desafiador em vários sentidos, mas ao mesmo tempo foi uma experiência divertida e altamente educativa. Tentei aplicar modelos de machine learning variados (ensemble e unsupervised) neste TechChallenge da fase 3, devido ao foco principal do TechChallenge da fase 2 estar em séries temporais. Consegui assimilar diversos conceitos que foram abordados pelos professores, mas que não havia praticado muito ainda, o que só confirma a importância da prática para uma compreensão mais profunda das coisas. No final das contas, o projeto se mostrou uma jornada muito gratificante! :orange[Obrigado pela oportunidade].<br/><b>:blue[&ndash; Danilo H. Achcar &ndash;]</b>*</small>
        """,
        unsafe_allow_html=True,
    )
