class Conta:

    def __init__(self, numero, nome, saldo, limite = 1000.0):

        self.__numero = numero
        self.__nome = nome
        self.__saldo = saldo
        self.__limite = limite

#---------Getters e Setters-------------------------------------------
    def get_numero(self):
        return self.__numero
    def get_nome(self):
        return self.__nome
    def get_saldo(self):
        return self.__saldo
    def get_limite(self):
        return self.__limite
    def set_saldo(self,saldo):
        self.__saldo = saldo
    def set_limite(self,limite):
        self.__limite = limite
#----------------------------------------------------------------------

    def extrato(self):
        print(f"Olá {self.get_nome()}! O saldo da sua conta é {self.get_saldo()}")

    def depositar(self, valor):
        self.set_saldo(self.get_saldo() + valor)

    def sacar(self, valor):
        self.set_saldo(self.get_saldo() - valor)

    def transferir(self,valor,destino):
        self.sacar(valor)
        destino.depositar(valor)


#conta1 = Conta(1, "Fulano", 0.0)
#conta2 = Conta(2, "Beltrano", 0.0)
#conta3 = Conta(3, "Sicrano", 0.0, 2000.0)