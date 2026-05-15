import pandas as pd
import matplotlib.pyplot as plt
import os
os.chdir(r"C:\Users\kffre\OneDrive\Área de Trabalho\faculdade-enzo\aula IA\prompt-toolkit\src")

df = pd.read_csv(
    "results.csv",
    header=None
)

df.columns = [
    "tecnica",
    "texto",
    "esperado",
    "resposta",
    "tempo"
]

media_tempo = df.groupby(
    "tecnica"
)["tempo"].mean()

media_tempo.plot(
    kind="bar"
)

plt.title(
    "Tempo Médio por Técnica"
)

plt.ylabel("Tempo (ms)")

plt.tight_layout()

plt.savefig(
    "tempo_tecnicas.png"
)

plt.show()

df["acerto"] = (
    df["esperado"]
    ==
    df["resposta"]
)

accuracy = df.groupby(
    "tecnica"
)["acerto"].mean() * 100

plt.figure()

accuracy.plot(
    kind="bar"
)

plt.title(
    "Acurácia por Técnica"
)

plt.ylabel("Acurácia (%)")

plt.tight_layout()

plt.savefig(
    "accuracy_tecnicas.png"
)

plt.show()