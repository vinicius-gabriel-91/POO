class Conta:

    def __init__(self, numero, nome, saldo, limite = 1000.0):

        self.numero = numero
        self.nome = nome
        self.saldo = saldo
        self.limite = limite

#conta1 = Conta(1, "Fulano", 0.0)
#conta2 = Conta(2, "Beltrano", 0.0)
#conta3 = Conta(3, "Sicrano", 0.0, 2000.0)

    def extrato(self):
        print(f"Olá {self.nome}! O saldo da sua conta é {self.saldo}")

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor