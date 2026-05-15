import json
import csv

from techniques import PromptTechniques

class Evaluator:
    def __init__(self):
        self.tech = PromptTechniques()
    
    def load_inputs(self):
        with open(
        "data/inputs.json",
        "r",
        encoding="utf-8"
    ) as file:
            data = json.load(file)
        return data
    
    def save_result(
        self,
        technique,
        texto,
        esperado,
        resposta,
        tempo,
        tokens
    ):
        with open(
            "results.csv",
            "a",
            newline="",
            encoding="utf-8"
    ) as file:
            writer = csv.writer(file)
            writer.writerow([
                technique,
                texto,
                esperado,
                resposta,
                tempo,
                tokens
            ])
    
    def evaluate(self, technique_name):
        inputs = self.load_inputs()
        technique = getattr(
            self.tech,
            technique_name
        )
        acertos = 0
        print(f"\nTécnica: {technique_name}")
        for item in inputs:
            texto = item["texto"]
            esperado = item["esperado"]
            prompt = technique(texto)
            resultado = self.tech.execute_prompt(prompt)
            resposta = resultado["resposta"]
            tempo = resultado["tempo_ms"]
            tokens = resultado["tokens"]
            resposta = resposta.strip().upper()

            print("Texto:", texto)

            print("Esperado:", esperado)

            print("IA:", resposta)

            print("Tempo:", f"{tempo:.2f} ms")

            print("Tokens:", tokens)

            print("-" * 40)

            self.save_result(
                technique_name,
                texto,
                esperado,
                resposta,
                tempo,
                tokens
            )

            if esperado in resposta:

                acertos += 1

        total = len(inputs)
        accuracy = (acertos / total) * 100

        print(f"Acurácia: {accuracy:.2f}%")

if __name__ == "__main__":

    evaluator = Evaluator()

    tecnicas = [
        "zero_shot",
        "few_shot",
        "chain_of_thought",
        "role_prompting"
    ]

    for tecnica in tecnicas:

        evaluator.evaluate(tecnica)