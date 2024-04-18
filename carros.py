class Veiculo:
    def __init__(self,marca,modelo) -> None:
        self.marca = marca
        self.modelo = modelo
        
    def acelerar(self):
        print(f'Você acelerou seu {self.marca}')
        
    def freiar(self):
        print(f'Você freiou seu {self.marca}')
        
class Carro(Veiculo):
    def __init__(self, marca, modelo) -> None:
        super().__init__(marca, modelo)
        
    def abrir_porta(self):
        print(f'Você abriu a porta do seu {self.marca}')
        
class Moto(Veiculo):
    def __init__(self, marca, modelo) -> None:
        super().__init__(marca, modelo)
        
    def empinar(self):
        print(f'Você empinou sua {self.marca}')
        
if __name__ == '__main__':
    carro1 = Carro('Fiat','Uno')
    moto1 = Moto('Honda','XRE360')

    carro1.abrir_porta()
    carro1.acelerar()
    carro1.freiar()
    print()
    moto1.acelerar()
    moto1.empinar()
    moto1.freiar()