import pandas as pd

import matplotlib.pyplot as plt


class ReportGenerator:

    def __init__(self):

        self.df = pd.read_csv(
            "results.csv",
            header=None
        )

        self.df.columns = [
            "tecnica",
            "texto",
            "esperado",
            "resposta",
            "tempo",
            "tokens"
        ]

        self.df["acerto"] = (
            self.df["esperado"]
            ==
            self.df["resposta"]
        )

    def gerar_tabela(self):

        tabela = self.df.groupby(
            "tecnica"
        ).agg({
            "tempo": "mean",
            "tokens": "mean",
            "acerto": "mean"
        })

        tabela["acerto"] = (
            tabela["acerto"] * 100
        )

        tabela.to_csv(
            "summary.csv"
        )

        print("\nTabela gerada!")

        print(tabela)

    def grafico_acuracia(self):

        accuracy = self.df.groupby(
            "tecnica"
        )["acerto"].mean() * 100

        plt.figure()

        accuracy.plot(
            kind="bar"
        )

        plt.title(
            "Acurácia por Técnica"
        )

        plt.ylabel(
            "Acurácia (%)"
        )

        plt.tight_layout()

        plt.savefig(
            "accuracy_tecnicas.png"
        )

        plt.show()

    def grafico_custo(self):

        custo = self.df.groupby(
            "tecnica"
        )["tokens"].mean()

        plt.figure()

        custo.plot(
            kind="bar"
        )

        plt.title(
            "Tokens Médios por Técnica"
        )

        plt.ylabel(
            "Tokens"
        )

        plt.tight_layout()

        plt.savefig(
            "tokens_tecnicas.png"
        )

        plt.show()

    def grafico_temperatura(self):

        consistencia = self.df.groupby(
            "tecnica"
        )["acerto"].std()

        plt.figure()

        consistencia.plot(
            kind="bar"
        )

        plt.title(
            "Consistência por Técnica"
        )

        plt.ylabel(
            "Desvio Padrão"
        )

        plt.tight_layout()

        plt.savefig(
            "consistencia_tecnicas.png"
        )

        plt.show()

    def recomendar(self):

        ranking = self.df.groupby(
            "tecnica"
        )["acerto"].mean()

        melhor = ranking.idxmax()

        print("\nMelhor técnica:")

        print(melhor)

        print(
            "\nJustificativa:"
        )

        print(
            "Maior taxa média de acerto."
        )


if __name__ == "__main__":

    report = ReportGenerator()

    report.gerar_tabela()

    report.grafico_acuracia()

    report.grafico_custo()

    report.grafico_temperatura()

    report.recomendar()