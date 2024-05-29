with open('C:/Users/Armando/Documents/python/Curso/Aula_16-Sets -Dict Comprehensions/arquivo.txt','r') as t:
    text = t.read()

def funcl(text):
    ''' Retornar dict
    
    dict[char] = Quantidade em que char aparecem en text
    '''
    # Criação de set e convert para lista com compehensions
    Chars = list({c for c in text })
     # conta a quantidade de caracteres e cria tupla chave valor
    quantity = [ (c,text.count(c)) for c in Chars ]

    # Convert a tupla em dicionario
    return dict(quantity)

print(funcl(text))

