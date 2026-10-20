import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carregar os dados do arquivo CSV
df = pd.read_csv('graficosCSV/dados_barras.csv')

# 2. Configurar a figura
fig, ax = plt.subplots(figsize=(10, 6))

# 3. Gerar o gráfico de barras com as colunas do arquivo
sns.barplot(
    data=df,
    x="categoria",
    y="vendas_medias",
    hue="regiao",
    palette="Set2",
    errorbar=None,
    ax=ax
)

# 4. Ajustar títulos e rótulos
ax.set_title("Média de Vendas por Categoria e Região", fontsize=14, fontweight="bold")
ax.set_xlabel("Categoria", fontsize=11)
ax.set_ylabel("Vendas Médias", fontsize=11)
ax.legend(title="Região", frameon=True)

plt.tight_layout()
plt.savefig('grafico_barras.png', dpi=300)
plt.show()
