with open('C:/Users/Armando/Documents/python/Curso/Aula_18-Interações/arquivo.txt','r') as arquivo:
    
    # a Função enumerate enumera a linha e com a opção de iniciar na linha 1
    for n,i in enumerate(arquivo,start=1):
        #imprime com 4 zeros a esquerda e retirando \n do final do arquivo
        print(f"{n:04} - " + i.strip())

