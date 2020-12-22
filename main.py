
def criar_conta(numero, nome, saldo, limite):
    conta = {"numero": numero, "nome": nome, "saldo": saldo, "limite": limite}
    return conta

def depositar(conta, valor):
    conta["saldo"] += valor
    return conta
def sacar(conta, valor):
    conta["saldo"] -= valor
    return conta
def extrato(conta):
    print(f"Seu saldo é: {conta['saldo']}")

