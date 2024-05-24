# i = 1
# while i < 10:
#     print(i)
#     i +=1

# criancas=["Bruno","Maria","Paula"]

# for item in criancas:
#     print(item)


# canal = "Refatorando"
# for letra in canal:
#     print(letra)


# for index in range(6,20,2):
#     print(index)

# criancas=["Bruno","Maria","Paula"]
# for index in range(len(criancas)):
#     print(criancas[index],index)

# criancas=["Bruno","Maria","Paula"]
# for index in range(len(criancas)):
#     if index == 0:
#         print(f"Primeira linha {criancas[index]}")
#     else:
#         print(f"Outras linhas {criancas[index]}")

matrix_numero=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
for linha in matrix_numero:
    print(linha)
    for coluna in linha:
        print(coluna)