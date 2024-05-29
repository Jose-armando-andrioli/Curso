def a():
    n=0
    while True:
        # Gerador retorno valor da função pelo comando yield
        n += 1
        yield n


for i in a():
    print(i)
    #break

