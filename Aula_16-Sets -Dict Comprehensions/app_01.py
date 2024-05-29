with open('C:/Users/Armando/Documents/python/Curso/Aula_16-Sets -Dict Comprehensions/arquivo.txt','r') as t:
    text = t.read()

def funcl(text):
    ''' Retornar dict
    
    dict[char] = Quantidade em que char aparecem en text
    '''
    Chars = []
    quantity = []
    for c in text:
        # verifica se o caracter não esta em Chars
        if not c in Chars:
            Chars.append(c)
            quantity.append(1)
        else:
            #Localiza a posição do caracter na lista
            index = Chars.index(c)
            quantity[index] += 1
    # Transforma o resultado em dicionario
    dicionario = {}
    for i in range(len(Chars)):
        dicionario[Chars[i]] = quantity[i]
    return dicionario



print(funcl(text))

