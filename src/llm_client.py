import requests
import time
import os
import tiktoken
from dotenv import load_dotenv

load_dotenv()

OLLAMA_HOST = os.getenv("OLLAMA_HOST")
MODEL_NAME = os.getenv("MODEL_NAME")

class LLMClient:

    def __init__(self):

        self.encoding = tiktoken.get_encoding(
            "cl100k_base"
    )

    def chat(self, prompt):

        inicio = time.time()

        url = f"{OLLAMA_HOST}/api/generate"

        payload = {
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False,
            "options": {
                "num_predict": 20
            }
        }
        
        tokens = self.encoding.encode(prompt)

        quantidade_tokens = len(tokens)
        
        response = requests.post(
        url,
        json=payload
        )
        
        data = response.json()

        resposta_modelo = data["response"]

        fim = time.time()
        
        tempo_ms = (fim - inicio) * 1000

        print("Tokens:", quantidade_tokens)

        return {
            "resposta": resposta_modelo,
            "tempo_ms": tempo_ms,
            "tokens": quantidade_tokens
        }
    
if __name__ == "__main__":
        
    client = LLMClient()
        
    resultado = client.chat(
        "Diga apenas: OI"
    )

    print(resultado)