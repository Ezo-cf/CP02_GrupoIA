from prompt_builder import PromptBuilder
from llm_client import LLMClient
class PromptTechniques:
    def __init__(self):

        self.builder = PromptBuilder()

        self.client = LLMClient()
    
    def zero_shot(self, user_input):
        system_prompt = """
            Você é um especialista em análise de sentimentos.

            Classifique o texto como:
            POSITIVO, NEGATIVO ou NEUTRO.

            Responda apenas com a classificação.`

            Responda em português do Brasil.
            """
        return self.builder.build_prompt(
            system_prompt,
            user_input
    )

    def few_shot(self, user_input):
        system_prompt = """
            Você é um especialista em análise de sentimentos.

            Exemplos:

            Texto: Produto excelente
            Resposta: POSITIVO

            Texto: Produto horrível
            Resposta: NEGATIVO

            Texto: Produto normal
            Resposta: NEUTRO

            Agora classifique o próximo texto.

            Responda em português do Brasil.
            """
        return self.builder.build_prompt(
            system_prompt,
            user_input
        )
    
    def chain_of_thought(self, user_input):
        system_prompt = """
        Você é especialista em sentimentos.

        Analise o texto passo a passo.

        Explique seu raciocínio antes da resposta final.

        Responda em português do Brasil.
        """
        return self.builder.build_prompt(
            system_prompt,
            user_input
    )

    def role_prompting(self, user_input):
        system_prompt = """
        Você é um analista sênior de experiência do cliente
        com 20 anos de experiência.
        """
        return self.builder.build_prompt(
            system_prompt,
            user_input
    )

    def execute_prompt(self, prompt):
        
        return self.client.chat(prompt)

if __name__ == "__main__":
    tech = PromptTechniques()

    prompt = tech.few_shot(
        "Produto veio quebrado"
    )

    print(prompt)
    