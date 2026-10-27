
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import os

# Configuração da página
st.set_page_config(
    page_title="Dashboard - Atividade 07",
    page_icon="📊",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.title("Informações do Aluno")
    st.write("**Nome:** Ana Karolina Magalhães")
    st.write("**Número da chamada:** 22403086")
    st.write("**Turma:** 3E2")

# Título
st.title("Dashboard - Atividade 07")
st.write("Visualização dos gráficos da Atividade 06")

# Lista de gráficos e análises
graficos = [
    (
        "Gráfico de Barras",
        "grafico_barras.png",
        "O gráfico de barras permite comparar valores entre diferentes categorias."
    ),
    (
        "Gráfico Boxplot",
        "grafico_boxplot.png",
        "O boxplot apresenta a mediana, a dispersão e possíveis valores atípicos."
    ),
    (
        "Gráfico de Dispersão",
        "grafico_dispersao.png",
        "O gráfico de dispersão ajuda a observar relações entre duas variáveis."
    ),
    (
        "Gráfico de Distribuição",
        "grafico_distribuicao.png",
        "O gráfico mostra como os valores estão distribuídos e onde se concentram."
    ),
    (
        "Gráfico de Frequência",
        "grafico_frequencia.png",
        "O gráfico permite identificar as categorias ou valores mais frequentes."
    ),
    (
        "Gráfico Heatmap",
        "grafico_heatmap.png",
        "O mapa de calor utiliza cores para destacar diferenças e padrões nos dados."
    ),
    (
        "Gráfico de Linha",
        "grafico_linha.png",
        "O gráfico de linha ajuda a observar variações e tendências entre os pontos."
    ),
    (
        "Gráfico de Pizza",
        "grafico_pizza.png",
        "O gráfico de pizza mostra a participação proporcional de cada categoria."
    ),
    (
        "Gráfico de Regressão",
        "grafico_regressao.png",
        "O gráfico de regressão permite observar a tendência e a relação entre variáveis."
    )
]

# Exibir três gráficos por linha
for inicio in range(0, len(graficos), 3):
    grupo = graficos[inicio:inicio + 3]
    colunas = st.columns(3)

    for coluna, (titulo, arquivo, analise) in zip(colunas, grupo):
        with coluna:
            st.subheader(titulo)

            if os.path.exists(arquivo):
                st.image(arquivo, use_container_width=True)
            else:
                
                st.warning(f"Arquivo não encontrado: {arquivo}")

            st.caption(analise)

    st.divider()
