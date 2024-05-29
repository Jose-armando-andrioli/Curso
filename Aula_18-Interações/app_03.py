nomes=['Will','Maria','Aline','Cesar']
idade=[10,20,40,20]

# Maneira mais comum de se escrever
# for i in range(len(nomes)):
#     print(f'{nomes[i]} tem {idade[i]} anos')

# Outra maneira de se escrever
for nome, idade in zip(nomes,idade):
    print(f'{nome} tem {idade} anos')
