import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carregar os dados do ficheiro CSV
df = pd.read_csv('graficosCSV/dados_dispersao.csv')

fig, ax = plt.subplots(figsize=(8, 6))

sns.scatterplot(
    data=df,
    x="altura_cm",
    y="peso_kg",
    hue="sexo",
    palette="Set1",
    s=70,  # Tamanho dos pontos
    ax=ax
)


ax.set_title("Relação entre Altura e Peso por Sexo", fontsize=14, fontweight="bold")
ax.set_xlabel("Altura (cm)", fontsize=11)
ax.set_ylabel("Peso (kg)", fontsize=11)
ax.legend(title="Sexo", frameon=True)
ax.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig('grafico_dispersao.png', dpi=300)
plt.show()