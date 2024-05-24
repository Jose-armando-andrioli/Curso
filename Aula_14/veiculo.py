class Carro:
    def __init__(self,marca,modelo,cor,combustivel):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.combustivel = combustivel

        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        if self.ligado:
            print(f"{self.marca} ja esta Ligado, nada acontece")
        else:
            print(f"{self.marca} ligado")
            self.ligado = True

    def desligar(self):
        if self.ligado:
            print(f"{self.marca} desligado")
            self.ligado = False
        else:
            print(f"{self.marca} ja esta desligado, nada acontece")
           
    def acelerar(self):
        if self.ligado:
            self.velocidade += 1
            print(f"{self.marca} a {self.velocidade} km/h")
        else:
            print(f"{self.marca} desligado não é possivel acelerar")

    def frear(self):
        if self.ligado:
            self.velocidade -= 1
            print(f"{self.marca} a {self.velocidade} km/h")
        else:
            print(f"{self.marca} desligado não é possivel frear")