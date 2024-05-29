with open('C:/Users/Armando/Documents/python/Curso/Aula_16-Sets -Dict Comprehensions/arquivo.txt','r') as t:
    text = t.read()

def funcl(text):
    '''Retornar dict\n
   dict[char] = Quantidade em que char aparecem en text
    '''
    # conta a quantidade de caracteres e cria tupla chave valor
    return dict([ (c,text.count(c)) for c in set(text) ])
 

print(funcl(text))

