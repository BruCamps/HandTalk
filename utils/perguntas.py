perguntas_por_trilha = {
    "Introdução à Lógica": [
        {
            "enunciado": "Todo programa começa com qual estrutura?",
            "alternativas": ["funcao inicio()", "se", "variável", "escreva"],
            "correta": 0,
            "explicacao": "Todo programa em Portugol começa com a função inicio()."
        },
    ],
    "Variáveis": [
        {
            "enunciado": "Qual tipo é usado para números com ponto?",
            "alternativas": ["inteiro", "cadeia", "real", "logico"],
            "correta": 2,
            "explicacao": "O tipo 'real' é usado para representar números decimais."
        },
    ],
    "Condicionais": [
        {
            "enunciado": "Qual comando é usado para decisões?",
            "alternativas": ["enquanto", "se", "para", "caso"],
            "correta": 1,
            "explicacao": "'se' é o comando condicional usado para tomar decisões."
        },
    ],
    "Laços de Repetição": [
        {
            "enunciado": "Qual laço repete enquanto uma condição for verdadeira?",
            "alternativas": ["para", "enquanto", "caso", "faça"],
            "correta": 1,
            "explicacao": "O laço 'enquanto' continua executando enquanto a condição for verdadeira."
        },
    ]
}

# Para facilitar, exporta só a lista de trilhas (chaves do dicionário)
trilhas_disponiveis = list(perguntas_por_trilha.keys())
# Para facilitar, exporta a lista de perguntas de uma trilha (valores do dicionário)
perguntas_disponiveis = list(perguntas_por_trilha.values())