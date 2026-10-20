import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carregar os dados do ficheiro CSV
df = pd.read_csv('graficosCSV/dados_regressao.csv')

fig, ax = plt.subplots(figsize=(8, 6))

# 3. Gerar o gráfico de regressão linear
sns.regplot(
    data=df,
    x="renda_mensal",
    y="gasto_mensal",
    color="#2b5c8f",
    line_kws={"color": "red", "linewidth": 2},
    ax=ax
)

ax.set_title("Relação entre Renda Mensal e Gasto Mensal", fontsize=14, fontweight="bold")
ax.set_xlabel("Renda Mensal", fontsize=11)
ax.set_ylabel("Gasto Mensal", fontsize=11)
ax.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig('grafico_regressao.png', dpi=300)
plt.show()