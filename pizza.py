import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carregar os dados do ficheiro CSV
df = pd.read_csv('graficosCSV/dados_pizza.csv')

# 2. Configurar a figura
fig, ax = plt.subplots(figsize=(8, 8))


cores = sns.color_palette('Set2', len(df))


ax.pie(
    df['faturamento'],
    labels=df['canal_venda'],
    autopct='%1.1f%%',   # Exibe a percentagem com 1 casa decimal
    startangle=140,      # Rotação inicial para melhor disposição
    colors=cores,
    wedgeprops={'edgecolor': 'white', 'linewidth': 1.5}
)


ax.set_title("Distribuição do Faturamento por Canal de Venda", fontsize=14, fontweight="bold")

plt.tight_layout()
plt.savefig('grafico_pizza.png', dpi=300)
plt.show()