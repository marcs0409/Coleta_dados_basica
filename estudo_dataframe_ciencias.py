import pandas as pd

# Lista: coleção ordenada de elementos que podem ser de qualquer tipo
lista_nomes = ['Alice', 'Bob', 'Charlie']
print('Lista de nomes: \n', lista_nomes)
print('Primeiro nome: \n', lista_nomes[0])

# Dicionário: coleção não ordenada de pares chave-valor
dicionario_pessoa = {
    'nome': 'Alice',
    'idade': 25,
    'cidade': 'São Paulo'
}
print('Dicionário de pessoa: \n', dicionario_pessoa)
print('Nome da pessoa: \n', dicionario_pessoa.get('nome'))

# Lista de dicionários: estrutura de dados que combina listas e dicionários
dados = [
    {'nome': 'Alice', 'idade': 25, 'cidade': 'São Paulo'},
    {'nome': 'Bob', 'idade': 30, 'cidade': 'Rio de Janeiro'},
    {'nome': 'Charlie', 'idade': 28, 'cidade': 'Belo Horizonte'}
]

# Dataframe: estrutura de dados tabular com linhas e colunas
df = pd.DataFrame(dados)
print('Dataframe de pessoas: \n', df)

# Selecionar coluna
print(df['nome'])

# Selecionar várias colunas
print(df[['nome', 'idade']])

# Selecionar linha pelo índice
print('Primeira linha: \n', df.iloc[0])

# Adicionar nova coluna
df['salario'] = [5000, 6000, 5500]

# Adicionar um novo registro
df.loc[len(df)] = {
    'nome': 'Daniel',
    'idade': 30,
    'cidade': 'São Paulo',
    'salario': 7000
}

print('dataframe atualizado: \n', df, '\n')

# Remover coluna
df.drop('salario', axis=1, inplace=True)

# Filtrando pessoas com mais de 28 anos
filtro_idade = df[df['idade'] >= 28]
print('Pessoas com 28 anos ou mais: \n', filtro_idade)

# Salvando o dataframe em um arquivo CSV
df.to_csv('dados.csv', index=False)

# Lendo um arquivo CSV em um dataframe
df_lido = pd.read_csv('dados.csv')
print('Dados lidos do arquivo CSV: \n', df_lido)
