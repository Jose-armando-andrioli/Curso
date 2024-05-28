lista = []  #[1,2,3,4,5,6,7,8,10]
# Primeiro modo de escrever
# for v in range(1,11):
#     lista.append(v)
#print(lista)

# for v in [1,2,3]:
#     for b in [4,5,6]:
#         lista.append((v,b))
# print(lista)

# for v in [1,2,3]:
#          for b in [4,5,6]:
#             if v % 2 == 0:
#                 lista.append((v,b))
# print(lista)





# lIST COMPREHENSION 
# lista2 = [ v for v in range(10) ]
#print(lista2)

# lista3 = [ v for v in 'asdfrtyuiopgg' ]
#print(lista3)

# lista4 = [ (v,b) for v in [1,2,3] for b in [4,5,6] ]
#print(lista4)

# lista5 = [ (v,b) 
#            for v in [1,2,3] 
#            for b in [4,5,6] 
#         ]
# print(lista5)

# sempre coloca o if apos a função que quer ser testado
# lista6 = [ (v,b) 
#            for v in [1,2,3] 
#            for b in [4,5,6] 
#            if v % 2 == 0
#         ]
# print(lista6)

lista7 = [ [ (v,b) for v in range(4) ] for b in range(3) ]
print(lista7)