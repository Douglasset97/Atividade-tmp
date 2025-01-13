import pandas as pd 

# Dados de exemplo
dados = {
    'Pergunta': [
        'O Que é Inteligência Artificial?',
        'Quando surgiu?',
        'Qual foi o criador?'
    ],
    'Resposta': [
        'Inteligência artificial, ou IA, é uma tecnologia que permite que computadores e máquinas simulem a capacidade de resolução de problemas e a inteligência humana.',
        'A Inteligência Artificial foi cunhada por John McCarthy durante a conferência de Dartmouth em 1956, marcando o início oficial das pesquisas em IA.',
        'John McCarthy.'
    ]
}

# Criação do DataFrame
df = pd.DataFrame(dados)

# Exibindo as perguntas numeradas
print("Escolha uma pergunta pelo número:")
for index, pergunta in enumerate(df['Pergunta']):
    print(f"{index + 1} - {pergunta}")

# Seleção da pergunta
while True:
    try:
        numero = int(input("\nDigite o número da pergunta: "))
        if 1 <= numero <= len(df):
            resposta = df.loc[numero - 1, 'Resposta']
            print(f"\nResposta: {resposta}")
            break
        else:
            print("Por favor, escolha um número válido.")
    except ValueError:
        print("Entrada inválida! Digite um número.")
