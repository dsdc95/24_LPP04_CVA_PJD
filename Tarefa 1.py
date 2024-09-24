import pandas as pd
#comentário 1
#comentário 2
#comentário 3
#comentário 4
#comentário 5
pessoas = {
    'Nome': ['Ana', 'Rui', 'Pedro', 'Sara'],
    'Idade': [20, 30, 26, 40],
    'Cidade': ['Lisboa', 'Porto', 'Coimbra', 'Faro']
}

df = pd.DataFrame(pessoas)

def mostrar_dataframe(df):
    print("Data Frame com nome, idade e cidade: ")
    print(df)
    print()

def adicionar_profissao(df):
    df['Profissão'] = ['Contabilista', 'Formador', 'Médico', 'Advogada']
    print("Data Frame com profissão adicionada: ")
    print(df)
    print()

def filtrar_por_cidade(df):
    cidade = input("Digite o nome da cidade para filtrar: ")
    filtro_cidade = df[df['Cidade'].str.contains(cidade, case=False)]
    print(f"Lista de pessoas registadas no Data Frame que moram em {cidade}:")
    print(filtro_cidade)
    print()

def remover_coluna_cidade(df):
    df = df.drop(columns=['Cidade'])
    print("Data Frame sem a coluna Cidade: ")
    print(df)
    print()
    return df

def ordenar_idades(df, ascending):
    df_ordenado = df.sort_values(by='Idade', ascending=ascending)
    if ascending:
        print("Data Frame ordenado por idades (ascendente):")
    else:
        print("Data Frame ordenado por idades (descendente):")
    print(df_ordenado)
    print()
    return df_ordenado

def listar_idade_20_30(df):
    filtro_idade_20_30 = df[(df['Idade'] >= 20) & (df['Idade'] <= 30)]
    print("Listagem das pessoas com idades entre os 20 e os 30 anos: ")
    print(filtro_idade_20_30)
    print()

def resumo_estatistico_idades(df):
    resumo_idades = df['Idade'].describe()
    print("Resumo estatístico das Idades: ")
    print(resumo_idades)
    print()

def renomear_profissao_para_cargo(df):
    df.rename(columns={'Profissão': 'Cargo'}, inplace=True)
    print("Data Frame com o nome do array/coluna alterado: ")
    print(df)
    print()

def media_idade_por_cargo(df):
    media_idade_por_cargo = df.groupby('Cargo')['Idade'].mean()
    print("Média de idades por cargo: ")
    print(media_idade_por_cargo)
    print()

def menu():
    print("Selecione uma opção:")
    print("1. Mostrar Data Frame")
    print("2. Adicionar Profissão")
    print("3. Filtrar por Cidade")
    print("4. Remover coluna Cidade")
    print("5. Ordenar por Idade Ascendente")
    print("6. Ordenar por Idade Descendente")
    print("7. Listar pessoas com idades entre 20 e 30 anos")
    print("8. Resumo estatístico das idades")
    print("9. Renomear coluna Profissão para Cargo")
    print("10. Média de idade por cargo")
    print("11. Sair")

while True:
    menu()
    escolha = input("Digite o número da opção desejada: ")

    if escolha == '1':
        mostrar_dataframe(df)
    elif escolha == '2':
        adicionar_profissao(df)
    elif escolha == '3':
        filtrar_por_cidade(df)
    elif escolha == '4':
        df = remover_coluna_cidade(df)
    elif escolha == '5':
        df = ordenar_idades(df, ascending=True)
    elif escolha == '6':
        df = ordenar_idades(df, ascending=False)
    elif escolha == '7':
        listar_idade_20_30(df)
    elif escolha == '8':
        resumo_estatistico_idades(df)
    elif escolha == '9':
        renomear_profissao_para_cargo(df)
    elif escolha == '10':
        media_idade_por_cargo(df)
    elif escolha == '11':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
