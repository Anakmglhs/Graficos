import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carregar os dados do ficheiro CSV
df = pd.read_csv('graficosCSV/dados_heatmap.csv')

# 2. Reorganizar os dados numa matriz (pivot table)
# Linhas: dia_semana | Colunas: horario | Valores: movimento_clientes
matriz = df.pivot(index="dia_semana", columns="horario", values="movimento_clientes")

dias_ordenados = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
matriz = matriz.reindex([dia for dia in dias_ordenados if dia in matriz.index])

fig, ax = plt.subplots(figsize=(10, 6))

# 4. Gerar o gráfico de Mapa de Calor (Heatmap)
sns.heatmap(
    matriz,
    annot=True,     
    fmt="g",        
    cmap="YlGnBu",   
    linewidths=0.5,  
    cbar_kws={'label': 'Movimento de Clientes'},
    ax=ax
)

ax.set_title("Movimento de Clientes por Dia e Horário", fontsize=14, fontweight="bold")
ax.set_xlabel("Horário", fontsize=11)
ax.set_ylabel("Dia da Semana", fontsize=11)

plt.tight_layout()
plt.savefig('grafico_heatmap.png', dpi=300)
plt.show()