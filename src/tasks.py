class Tasks:
    def sentiment_analysis(self):
        return {
            "nome": "sentiment_analysis",

            "descricao":
            "Classificação de sentimentos",

            "labels": [
                "POSITIVO",
                "NEGATIVO",
                "NEUTRO"
            ]
        }
    
    def summarization(self):
        return {
            "nome": "summarization",

            "descricao":
            "Resumo automático de textos"
        }
    
    def information_extraction(self):
        return {
            "nome": "information_extraction",

            "descricao":
            "Extração de entidades"
        }
    
if __name__ == "__main__":
    tasks = Tasks()

print(
    tasks.sentiment_analysis()
)