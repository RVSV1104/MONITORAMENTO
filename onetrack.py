# -*- coding: utf-8 -*-
"""OneTrack

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cJDxaF3qPhN9CEVCIYq5pi2KrhNjQI73
"""

# Importar pacotes necessários para exibição e banco de dados
import pandas as pd
import ipywidgets as widgets
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Banco de dados em memória para registrar monitorias
data_db = pd.DataFrame(columns=[
    "Consultor", "Turno", "Ciclo de Monitoria", "Tipo de Atendimento", "Data do Contato",
    "Resumo do Contato", "Venda Concluída", "Tempo de Chamada (min)", "Satisfação do Cliente (1 a 5)",
    "Aderência ao Script", "Prontidão", "Apresentação", "Confirmação de Dados", "Personalização",
    "Identificação de Necessidade e Objetivo", "Qualificação do Lead", "Sondagem",
    "Empatia e Comunicação", "Proatividade", "Apresentação de Benefícios", "Oferta de Descontos e Promoções",
    "Argumentação de Vendas", "Contra-Argumentação", "Resumo e Encerramento",
    "Encerramento do Atendimento", "Feedback Gerencial", "Motivos de Não Venda",
    "Solicitação de Compromisso", "Incentivo ao Testemunho", "Primeira Resolução",
    "Pontos Positivos", "Pontos de Melhoria", "Nota Final", "Plano de Desenvolvimento"
])

# Campos de entrada de dados essenciais
consultor_input = widgets.Text(description="Consultor")
turno_input = widgets.Text(description="Turno")
ciclo_monitoria_input = widgets.Text(description="Ciclo")
tipo_atendimento_input = widgets.Text(description="Tipo Atendimento")
data_contato_input = widgets.DatePicker(description="Data Contato")
resumo_contato_input = widgets.Textarea(description="Resumo do Contato")
venda_concluida_input = widgets.Checkbox(description="Venda Concluída")
tempo_chamada_input = widgets.FloatText(description="Tempo de Chamada (min)")
satisfacao_cliente_input = widgets.IntSlider(value=3, min=1, max=5, description="Satisfação (1 a 5)")
aderencia_script_input = widgets.Checkbox(description="Aderência ao Script")

# Perguntas de monitoria com checkboxes
prontidao_input = widgets.Checkbox(description="Prontidão")
apresentacao_input = widgets.Checkbox(description="Apresentação")
confirmacao_dados_input = widgets.Checkbox(description="Confirmação de Dados")
personalizacao_input = widgets.Checkbox(description="Personalização")
necessidade_objetivo_input = widgets.Checkbox(description="Necessidade e Objetivo")
qualificacao_lead_input = widgets.Checkbox(description="Qualificação do Lead")
sondagem_input = widgets.Checkbox(description="Sondagem")
empatia_comunicacao_input = widgets.Checkbox(description="Empatia e Comunicação")
proatividade_input = widgets.Checkbox(description="Proatividade")
apresentacao_beneficios_input = widgets.Checkbox(description="Apresentação de Benefícios")
oferta_descontos_input = widgets.Checkbox(description="Oferta de Descontos e Promoções")
argumentacao_vendas_input = widgets.Checkbox(description="Argumentação de Vendas")
contra_argumentacao_input = widgets.Checkbox(description="Contra-Argumentação")
resumo_encerramento_input = widgets.Checkbox(description="Resumo e Encerramento")
encerramento_atendimento_input = widgets.Checkbox(description="Encerramento do Atendimento")
feedback_gerencial_input = widgets.Checkbox(description="Feedback Gerencial")
motivos_nao_venda_input = widgets.Checkbox(description="Motivos de Não Venda")
solicitacao_compromisso_input = widgets.Checkbox(description="Solicitação de Compromisso")
incentivo_testemunho_input = widgets.Checkbox(description="Incentivo ao Testemunho")
primeira_resolucao_input = widgets.Checkbox(description="Primeira Resolução")

# Novos campos para Pontos de Melhoria e Pontos Positivos
pontos_positivos_input = widgets.Textarea(description="Pontos Positivos")
pontos_melhoria_input = widgets.Textarea(description="Pontos de Melhoria")

# Botão para salvar monitoria
save_button = widgets.Button(description="Salvar Monitoria")

# Função para salvar a monitoria e calcular indicadores
def salvar_monitoria(b):
    # Armazenar dados essenciais
    new_data = {
        "Consultor": consultor_input.value,
        "Turno": turno_input.value,
        "Ciclo de Monitoria": ciclo_monitoria_input.value,
        "Tipo de Atendimento": tipo_atendimento_input.value,
        "Data do Contato": data_contato_input.value,
        "Resumo do Contato": resumo_contato_input.value,
        "Venda Concluída": venda_concluida_input.value,
        "Tempo de Chamada (min)": tempo_chamada_input.value,
        "Satisfação do Cliente (1 a 5)": satisfacao_cliente_input.value,
        "Aderência ao Script": aderencia_script_input.value,
        "Prontidão": prontidao_input.value,
        "Apresentação": apresentacao_input.value,
        "Confirmação de Dados": confirmacao_dados_input.value,
        "Personalização": personalizacao_input.value,
        "Identificação de Necessidade e Objetivo": necessidade_objetivo_input.value,
        "Qualificação do Lead": qualificacao_lead_input.value,
        "Sondagem": sondagem_input.value,
        "Empatia e Comunicação": empatia_comunicacao_input.value,
        "Proatividade": proatividade_input.value,
        "Apresentação de Benefícios": apresentacao_beneficios_input.value,
        "Oferta de Descontos e Promoções": oferta_descontos_input.value,
        "Argumentação de Vendas": argumentacao_vendas_input.value,
        "Contra-Argumentação": contra_argumentacao_input.value,
        "Resumo e Encerramento": resumo_encerramento_input.value,
        "Encerramento do Atendimento": encerramento_atendimento_input.value,
        "Feedback Gerencial": feedback_gerencial_input.value,
        "Motivos de Não Venda": motivos_nao_venda_input.value,
        "Solicitação de Compromisso": solicitacao_compromisso_input.value,
        "Incentivo ao Testemunho": incentivo_testemunho_input.value,
        "Primeira Resolução": primeira_resolucao_input.value,
        "Pontos Positivos": pontos_positivos_input.value,
        "Pontos de Melhoria": pontos_melhoria_input.value
    }

    # Cálculo da Nota Final (exemplo de cálculo, pode ser ajustado)
    new_data["Nota Final"] = (
        satisfacao_cliente_input.value * 20  # Satisfação do Cliente tem peso maior
        + (aderencia_script_input.value + prontidao_input.value + apresentacao_input.value +
           confirmacao_dados_input.value + personalizacao_input.value + necessidade_objetivo_input.value +
           qualificacao_lead_input.value + sondagem_input.value + empatia_comunicacao_input.value +
           proatividade_input.value + apresentacao_beneficios_input.value + oferta_descontos_input.value +
           argumentacao_vendas_input.value + contra_argumentacao_input.value + resumo_encerramento_input.value +
           encerramento_atendimento_input.value + feedback_gerencial_input.value + motivos_nao_venda_input.value +
           solicitacao_compromisso_input.value + incentivo_testemunho_input.value + primeira_resolucao_input.value
        ) * 5  # Cada checkbox conta 5 pontos
    ) / 25  # Dividido para obter uma nota média (ajustar conforme necessário)

    # Definir se há necessidade de plano de desenvolvimento
    new_data["Plano de Desenvolvimento"] = "Sim" if new_data["Nota Final"] < 85 else "Não"

    # Adicionar ao banco de dados usando pd.concat
    global data_db
    data_db = pd.concat([data_db, pd.DataFrame([new_data])], ignore_index=True)

    # Feedback de confirmação
    print("Monitoria salva com sucesso!")

# Associar botão à função de salvar
save_button.on_click(salvar_monitoria)

# Exibir formulário
display(
    consultor_input, turno_input, ciclo_monitoria_input, tipo_atendimento_input,
    data_contato_input, resumo_contato_input, venda_concluida_input, tempo_chamada_input,
    satisfacao_cliente_input, aderencia_script_input,
    prontidao_input, apresentacao_input, confirmacao_dados_input, personalizacao_input,
    necessidade_objetivo_input, qualificacao_lead_input, sondagem_input, empatia_comunicacao_input,
    proatividade_input, apresentacao_beneficios_input, oferta_descontos_input,
    argumentacao_vendas_input, contra_argumentacao_input, resumo_encerramento_input,
    encerramento_atendimento_input, feedback_gerencial_input, motivos_nao_venda_input,
    solicitacao_compromisso_input, incentivo_testemunho_input, primeira_resolucao_input,
    pontos_positivos_input, pontos_melhoria_input, save_button
)

# Importação das bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Função para gerar o relatório detalhado por consultor com pontos positivos e negativos
def gerar_relatorio_por_consultor(data_db):
    # Verificar se o banco de dados contém informações
    if data_db.empty:
        print("Nenhuma monitoria registrada para gerar o relatório.")
        return

    # Lista de consultores
    consultores = data_db["Consultor"].unique()

    # Criar DataFrame para armazenar resultados
    resultados = []

    # Calcular os indicadores para cada consultor
    for consultor in consultores:
        # Filtrar dados do consultor
        consultor_data = data_db[data_db["Consultor"] == consultor]
        total_atendimentos = len(consultor_data)

        # Indicadores de performance
        taxa_conversao = (consultor_data["Venda Concluída"].sum() / total_atendimentos) * 100 if total_atendimentos > 0 else 0
        indice_qualificacao = (consultor_data["Qualificação do Lead"].mean() * 100) if total_atendimentos > 0 else 0
        indice_personalizacao = (consultor_data["Personalização"].mean() * 100) if total_atendimentos > 0 else 0
        indice_apresentacao = (consultor_data["Apresentação de Benefícios"].mean() * 100) if total_atendimentos > 0 else 0
        taxa_ofertas = (consultor_data["Oferta de Descontos e Promoções"].mean() * 100) if total_atendimentos > 0 else 0
        taxa_sucesso = (consultor_data["Venda Concluída"].mean() * 100) if total_atendimentos > 0 else 0
        tempo_medio = consultor_data["Tempo de Chamada (min)"].mean()
        taxa_primeira_resolucao = (consultor_data["Primeira Resolução"].mean() * 100) if total_atendimentos > 0 else 0
        satisfacao_cliente = consultor_data["Satisfação do Cliente (1 a 5)"].mean() * 20  # Convertendo para porcentagem
        aderencia_script = (consultor_data["Aderência ao Script"].mean() * 100) if total_atendimentos > 0 else 0
        taxa_proatividade = (consultor_data["Proatividade"].mean() * 100) if total_atendimentos > 0 else 0
        habilidade_contra_arg = consultor_data["Contra-Argumentação"].mean() * 100
        taxa_doc_nao_venda = (consultor_data["Motivos de Não Venda"].notnull().sum() / total_atendimentos) * 100
        indice_feedback = (consultor_data["Feedback Gerencial"].mean() * 100) if total_atendimentos > 0 else 0
        taxa_fechamento = (consultor_data["Encerramento do Atendimento"].mean() * 100) if total_atendimentos > 0 else 0
        pontuacao_geral = consultor_data[[
            "Prontidão", "Apresentação", "Confirmação de Dados", "Personalização",
            "Identificação de Necessidade e Objetivo", "Qualificação do Lead",
            "Sondagem", "Empatia e Comunicação", "Proatividade",
            "Apresentação de Benefícios", "Argumentação de Vendas",
            "Contra-Argumentação", "Resumo e Encerramento"
        ]].mean().mean() * 100  # Média de todas as habilidades específicas
        total_pontos = consultor_data[[
            "Prontidão", "Apresentação", "Confirmação de Dados", "Personalização",
            "Identificação de Necessidade e Objetivo", "Qualificação do Lead",
            "Sondagem", "Empatia e Comunicação", "Proatividade",
            "Apresentação de Benefícios", "Argumentação de Vendas",
            "Contra-Argumentação", "Resumo e Encerramento"
        ]].sum().sum()  # Soma total das pontuações

        # Identificar pontos positivos e negativos
        pontos_positivos = []
        pontos_negativos = []

        if taxa_conversao > 50:
            pontos_positivos.append("Alta taxa de conversão")
        else:
            pontos_negativos.append("Taxa de conversão abaixo do esperado")

        if satisfacao_cliente >= 80:
            pontos_positivos.append("Alta satisfação do cliente")
        else:
            pontos_negativos.append("Satisfação do cliente abaixo do desejado")

        if tempo_medio <= 5:
            pontos_positivos.append("Tempo médio de atendimento eficiente")
        else:
            pontos_negativos.append("Tempo médio de atendimento acima do ideal")

        if aderencia_script >= 90:
            pontos_positivos.append("Alta aderência ao script")
        else:
            pontos_negativos.append("Baixa aderência ao script")

        # Adicionar os resultados no DataFrame
        resultados.append([
            consultor, taxa_conversao, indice_qualificacao, indice_personalizacao, indice_apresentacao,
            taxa_ofertas, taxa_sucesso, tempo_medio, taxa_primeira_resolucao, satisfacao_cliente,
            aderencia_script, taxa_proatividade, habilidade_contra_arg, taxa_doc_nao_venda,
            indice_feedback, taxa_fechamento, pontuacao_geral, total_pontos, pontos_positivos, pontos_negativos
        ])

    # Criar DataFrame de Resultados
    colunas = [
        "Consultor", "Taxa de Conversão (%)", "Índice de Qualificação de Leads (%)",
        "Índice de Personalização e Aderência (%)", "Índice de Apresentação de Benefícios (%)",
        "Taxa de Ofertas e Descontos (%)", "Taxa de Sucesso de Vendas (%)", "Tempo Médio de Atendimento (min)",
        "Taxa de Primeira Resolução (%)", "Satisfação do Cliente (NPS) (%)",
        "Aderência ao Script (%)", "Taxa de Proatividade (%)", "Habilidade de Contra-Argumentação (%)",
        "Taxa de Documentação de Não Venda (%)", "Índice de Implementação de Feedback (%)",
        "Taxa de Fechamento (%)", "Pontuação Geral (%)", "Total de Pontos", "Pontos Positivos", "Pontos Negativos"
    ]
    resultados_df = pd.DataFrame(resultados, columns=colunas)

    # Exibir o relatório em formato tabular
    print("\nRelatório de Desempenho por Consultor:")
    display(resultados_df)

    # Exibir gráficos de desempenho geral para visualização
    plt.figure(figsize=(16, 8))
    sns.barplot(x="Consultor", y="Taxa de Conversão (%)", data=resultados_df, palette="Blues_d")
    plt.title("Taxa de Conversão por Consultor")
    plt.xticks(rotation=45)
    plt.show()

    plt.figure(figsize=(16, 8))
    sns.barplot(x="Consultor", y="Tempo Médio de Atendimento (min)", data=resultados_df, palette="viridis")
    plt.title("Tempo Médio de Atendimento por Consultor")
    plt.xticks(rotation=45)
    plt.show()

    plt.figure(figsize=(16, 8))
    sns.barplot(x="Consultor", y="Satisfação do Cliente (NPS) (%)", data=resultados_df, palette="magma")
    plt.title("Satisfação do Cliente (NPS) por Consultor")
    plt.xticks(rotation=45)
    plt.show()

    # Salvar o relatório como CSV
    resultados_df.to_csv("relatorio_detalhado_por_consultor.csv", index=False)
    print("\nRelatório salvo como 'relatorio_detalhado_por_consultor.csv'.")

# Gerar o relatório detalhado por consultor
gerar_relatorio_por_consultor(data_db)

pip install streamlit