# Nodos
# r - Read
# a - Append
# w - Write
# x - Criar Arquivo
# r+ - Read e Write

arq="C:/Users/Armando/Documents/python/Curso/Aula_12/Test.txt"

arquivo = open(arq,"r+")
try:
    # if not(arquivo.readable()):   # verifica se o arquivo pode ser lido
    #     print("Arquivo Nao pode ser lido")
    # else:
        # print(arquivo.readline())
        # print(arquivo.readline())
        # print(arquivo.readline())
        # print(arquivo.readline())
        # print(arquivo.readline())
        linhas = arquivo.readlines()
        print(linhas)

        arquivo.write("\nSql")
except:
    print("Erro inesperado")

finally:
    arquivo.close

# Remover arquivos atravez de uma biblioteca do Sistema operacional
# import os

# if os.path.exists(arq):
#     os.remove(arq)
# else:
#     print("Arquivo não existe")