try:
    numero = int(input("Entre com um valor : " ))
    print(numero)


except ValueError:
    print("Numero invalido")
except:
    print("Erro : ")
finally:
    print("Finalizando o programa")