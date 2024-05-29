linhas = 5
cols = 5
achou = False

# Modo como normalente seria escrito
# for linha in range(linhas):
#     for col in range(cols):
#         if linha==3 and col==3:
#             achou=True
#             break
#     if achou == True:
#         break

# Modo utilizando Geração
for linha,coluna in ( (l,c) for l in range(linhas) for c in range(cols) ):
    if linha == 3 and coluna ==3:
        break

