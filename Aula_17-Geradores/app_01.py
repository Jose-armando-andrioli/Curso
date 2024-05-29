# coloca tudo em memoria
#a=[i for i in range(50_000_000)]

# O genertion comprehensius é entre parentesis
a=( i for i in range(300_000_000) )


for i in a:
    print(i)
    break

