import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("graficosCSV/dados_linhas.csv")
print(df)
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(
    data=df,
    x="data",
    y="vendas",
    hue="loja",
    marker="o",
    color="#2b5c8f",
    linewidth=2,
    ax=ax,
)
ax.set_title("Evolução do Número de vendas", fontsize=14, fontweight="bold")
ax.set_xlabel("Vendas", fontsize=11)
ax.set_ylabel("Lojas", fontsize=11)
plt.tight_layout()
plt.savefig('grafico_linha.png', dpi=300)
plt.show()