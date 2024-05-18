class ContaBancaria:
    def __init__(self, numero, titular, saldo=0):
        self.saldo = saldo
        self.numero = numero
        self.titular = titular

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor

    def visualizar_saldo(self):
        return self.saldo

    def extrato(self):
        return f"Titular: {self.titular}\nNúmero da conta: {self.numero}\nSaldo: {self.saldo}"

    def transferir(self, destino, valor):
        if self.sacar(valor):
            destino.depositar(valor)
            print(f"Transferência de R${valor:.2f} para a conta {destino.numero} realizada com sucesso.")
        else:
            print("Transferência falhou devido a saldo insuficiente.")



