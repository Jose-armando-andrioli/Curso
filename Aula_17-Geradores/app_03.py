def evens(limit=10):
    n=0
    while True:
        # Gerador retorno valor da função pelo comando yield
        n += 2
        if n>limit:
            return

        yield n
def odds(limit=10):
    n=1
    while True:
        if n>limit:
            return
        # Gerador retorno valor da função pelo comando yield
        yield n
        n += 2

# Concatenando 2 geradores 1 maneira de se escrever
# def chain(g1,g2):
#     for i in g1:
#         yield i

#     for i in g2:
#         yield i

# Concatenando 2 geradores 2 maneira de se escrever
def chain(g1,g2):
        # executa enquanto tiver valor em g1 e em g2
        yield from g1
        yield from g2    

# for i in chain(evens(),odds(20)):
#     print(i)
#     #break

#requisitando valores ao gerador
#cria gerador
a=evens()
#pega o primeiro, segundo e terceiro valor
print(next(a))
print(next(a))
print(next(a))
