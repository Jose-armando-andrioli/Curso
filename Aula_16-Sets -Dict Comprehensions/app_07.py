from collections import Counter
with open('C:/Users/Armando/Documents/python/Curso/Aula_16-Sets -Dict Comprehensions/arquivo.txt','r') as t:
    text = t.read()
def funcl(text):
     # Chamada da função counter metodo most mostra quais são os mais comuns
    return Counter(text).most_common(4)
 

print(funcl(text))

