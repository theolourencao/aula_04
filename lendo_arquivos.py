import csv
#caminho para o arquivo csv
caminho_arquivo = 'exemplo.csv'

#inicializau ma lista vazia para armazenar os dados
dados: list=[]

with open(file=caminho_arquivo, mode="r", encoding='utf-8') as arquivo:
    leitor_csv = csv.DictReader(arquivo)

    for linha in leitor_csv:
        dados.append(linha)

print(dados)