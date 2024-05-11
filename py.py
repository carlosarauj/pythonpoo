class Carro:
    def __init__(self, marca, modelo, cor, combustivel):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.combustivel = combustivel

        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        if self.ligado:
            print("Carro já está ligado")
        else:
            print("O carro foi ligado")

            self.ligado = True

    def desligar(self):
        if self.ligado:
            print("Carro desligado")
        else:
            print("O carro já foi desligado")

            self.ligado = False
    
    def acelerar(self):
        if self.ligado:
            self.velocidade +=10
            print(f"{self.velocidade}km/h")
        else:
            print("Não é possível acelerar, carro desligado")
    
    def frear(self):
        if self.ligado:
            self.velocidade -=10
            print(f"{self.velocidade}km/h")
        else:
            print("Não é possível frear, carro desligado")
        
        

    

#usa o terminal com: python nomedoarquivo.py