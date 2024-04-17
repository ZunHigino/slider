import datetime
from os import system
from time import sleep
import keyboard as kb

class Conta:
    def __init__(self, nome, sobrenome, saldo, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.saldo = saldo
        self.idade = idade
        self.ano = datetime.datetime.now()
        self.ano = int(self.ano.strftime('%Y'))
        
    def __str__(self) -> str:
        return f'''Nome do usuário: {self.nome} {self.sobrenome}
Idade: {self.idade}
Data de nascimento: {self.ano - self.idade}
Saldo da conta: {self.saldo}
'''

    def menu():
        print('''======Menu======
1 - Sacar
2 - Depositar
3 - Ver conta
0 - Sair''')
        
    def conta(self,res):
        print(f'''Nome do usuário: {self.nome} {self.sobrenome}
Idade: {self.idade}
Data de nascimento: {self.ano - self.idade}
Saldo da conta: {self.saldo}

4 - Sair
    ''')   
        rodar = True
        
        while rodar: 
            res = kb.read_key()
            if res == '4':
                rodar = False

    def loading():
        n = 3
        for i in range(2):
            for i in range(1, n+1):
                system('cls')
                print('Carregando transação' + i * '.')
                sleep(0.4)
        system('cls')

    def sacar(self, x):
        self.saldo -= x
        Conta.loading()
        print('Transação completa')
        sleep(1.2)

    def depositar(self, x):
        self.saldo += x
        Conta.loading()
        print('Transação completa')
        sleep(1.2)
    
    def sair():
        n = 3
        for i in range(2):
            for i in range(1, n+1):
                system('cls')
                print('Saindo' + i * '.')
                sleep(0.3)
        system('cls')

if __name__ == '__main__':
    conta1 = Conta('Heitor','Higino',2000,17)
    
    rodando = True
    
    while rodando:
        system('cls')
        Conta.menu()

        sensor = kb.read_key()
        
        if sensor == '1':
            kb.press_and_release('backspace')
            system('cls')
            qnt = int(input('Insira a quantidade de dinheiro que deseja sacar: '))
            conta1.sacar(qnt)
        elif sensor == '2':
            kb.press_and_release('backspace')
            system('cls')
            qnt = int(input('Insira a quantidade de dinheiro que deseja depositar: '))
            conta1.depositar(qnt)
        elif sensor == '3':
            kb.press_and_release('backspace')
            system('cls')
            conta1.conta(sensor)
        elif sensor == '0':
            kb.press_and_release('backspace')
            Conta.sair()
            rodando = False
        else:
            kb.press_and_release('backspace')
    
    system('cls')
    print('Obrigado pela visita!')