class PromptBuilder:
    def build_prompt(
    self,
    system_prompt,
    user_input
):
        prompt = f"""
{system_prompt}

Texto:
{user_input}
"""
        return prompt
    
if __name__ == "__main__":
        
    builder = PromptBuilder()
        
    prompt = builder.build_prompt(
        "Você é especialista em sentimentos.",
        "Produto horrível"
    )

    print(prompt)