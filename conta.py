class Conta:

    def __init__(self, numero, nome, saldo, limite = 1000.0):

        self.__numero = numero
        self.__nome = nome
        self.__saldo = saldo
        self.__limite = limite

#---------Getters e Setters como propriedades----------------------------
    @property
    def numero(self):
        return self.__numero

    @property
    def nome(self):
        return self.__nome

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @saldo.setter
    def saldo(self,saldo):
        self.__saldo = saldo

    @limite.setter
    def limite(self,limite):
        self.__limite = limite
#----------------------------------------------------------------------

    def extrato(self):
        print(f"Olá {self.nome}! O saldo da sua conta é {self.saldo}")

    def depositar(self, valor):
        self.saldo += valor

    def __verificar_saque(self,valor):
        saque_autorizado = valor <= self.saldo + self.limite
        return saque_autorizado

    def sacar(self, valor):
        if (self.__verificar_saque(valor)):
            self.saldo -= valor
        else:
            print(f"Saque negado! O valor disponivel para saque é de {self.saldo + self.limite}")

    def transferir(self,valor,destino):
        self.sacar(valor)
        destino.depositar(valor)


#conta1 = Conta(1, "Fulano", 0.0)
#conta2 = Conta(2, "Beltrano", 0.0)
#conta3 = Conta(3, "Sicrano", 0.0, 2000.0)