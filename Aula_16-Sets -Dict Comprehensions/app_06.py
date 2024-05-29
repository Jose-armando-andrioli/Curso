with open('C:/Users/Armando/Documents/python/Curso/Aula_16-Sets -Dict Comprehensions/arquivo.txt','r') as t:
    text = t.read()
print(text)
def funcl(text):
    '''Retornar dict\n
   dict[char] = Quantidade em que char aparecem en text
    '''
    # Criação do Dict comprehension com chave : valor
    return { c : text.count(c) for c in set(text) }
 

print(funcl(text))

