Sistema de Avaliação de Técnicas de Prompt Engineering

Descrição

Este projeto implementa um sistema de avaliação
de técnicas de Prompt Engineering utilizando
LLMs locais com Ollama e o modelo phi3.

O sistema compara diferentes técnicas de prompting
em tarefas de análise de sentimentos.

Tecnologias Utilizadas

- Python
- Ollama
- phi3
- Pandas
- Matplotlib
- JSON
- CSV

Estrutura do Projeto

PROMPT-TOOLKIT/
│
├── data/
│   ├── examples.json
│   └── inputs.json
│
├── docs/
│
├── output/
│   └── graficos/
│
├── prompts/
│   ├── system_prompts.json
│   └── templates.json
│
├── src/
│   ├── __init__.py
│   ├── charts.py
│   ├── evaluator.py
│   ├── llm_client.py
│   ├── prompt_builder.py
│   ├── report.py
│   ├── tasks.py
│   └── techniques.py
│
├── venv/
│
├── .env
├── main.py
├── README.md
└── requirements.txt

Componentes do Sistema

llm_client.py
Responsável pela comunicação com o Ollama
e envio de prompts para o modelo phi3.

prompt_builder.py
Responsável pela construção dinâmica
dos prompts utilizados no sistema.

techniques.py
Implementa as técnicas de Prompt Engineering:
Zero Shot
Few Shot
Chain of Thought
Role Prompting

evaluator.py
Executa avaliações automáticas utilizando
o dataset presente em inputs.json.
Também calcula:
acurácia;
tempo de execução;
comparação entre técnicas.

charts.py
Responsável pela geração de gráficos
utilizando matplotlib.

tasks.py
Define as tarefas disponíveis no sistema,
como análise de sentimentos.

report.py
Responsável pela geração de relatórios
e organização de métricas.

Técnicas de Prompt Engineering
O sistema implementa as seguintes técnicas:

Zero Shot
A IA recebe apenas a instrução principal,
sem exemplos prévios.

Few Shot
A IA recebe exemplos antes da tarefa.

Chain of Thought
A IA é incentivada a explicar
o raciocínio passo a passo.

Role Prompting
A IA recebe um papel específico,
como especialista ou analista.

Dataset
Os dados de entrada estão localizados em:

data/inputs.json

O dataset contém exemplos de análise
de sentimentos classificados como:
POSITIVO
NEGATIVO
NEUTRO

Como Executar
1. Ativar ambiente virtual
Windows:
venv\Scripts\activate

2. Instalar dependências
pip install -r requirements.txt

3. Iniciar o Ollama
ollama run phi3

4. Executar avaliação
python src/evaluator.py

5. Gerar gráficos
python src/charts.py

Resultados Gerados

O sistema gera:
métricas de acurácia;
comparação de tempo;
benchmark entre técnicas;
gráficos automáticos.
Arquivos Gerados
CSV de resultados
results.csv

Gráficos
tempo_tecnicas.png
accuracy_tecnicas.png

Objetivo Acadêmico
O objetivo do projeto é demonstrar
na prática o impacto das técnicas
de Prompt Engineering em LLMs locais.

Conclusão
O projeto demonstrou que diferentes
técnicas de Prompt Engineering impactam
diretamente:
qualidade das respostas;
tempo de processamento;
desempenho geral do modelo.
Além disso, o sistema permitiu criar
um benchmark automatizado entre técnicas
utilizando IA local com Ollama.