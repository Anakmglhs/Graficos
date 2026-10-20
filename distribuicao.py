import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carregar os dados do arquivo CSV
df = pd.read_csv('graficosCSV/dados_distribuicao.csv')

# 2. Configurar a figura
fig, ax = plt.subplots(figsize=(8, 5))

# 3. Gerar o gráfico de distribuição
sns.histplot(
    data=df,
    x="idade",
    kde=True,
    bins=15,
    color="#4c72b0",
    ax=ax
)

# 4. Configurar títulos e rótulos das eixos
ax.set_title("Distribuição da Idade dos Clientes", fontsize=14, fontweight="bold")
ax.set_xlabel("Idade", fontsize=11)
ax.set_ylabel("Frequência", fontsize=11)

plt.tight_layout()
plt.savefig('grafico_distribuicao.png', dpi=300)
plt.show()