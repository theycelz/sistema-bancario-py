class ContaBancaria:
    def __init__(self, numero:int, titular:str, saldo:float=0.00):
        self.saldo = saldo
        self.numero = numero
        self.titular = titular

    def sacar(self, valor:float) -> bool:
        if valor <= 0:
            print("O valor de saque deve ser positivo.")
            return False
        if valor > self.saldo:
            print("Saldo insuficiente.")
            return False
        self.saldo -= valor
        return True

    def depositar(self, valor:float):
        self.saldo += valor

    def visualizar_saldo(self):
        return self.saldo

    def extrato(self):
        return f"Titular: {self.titular}\nNúmero da conta: {self.numero}\nSaldo: {self.saldo}"

    def transferir(self, destino, valor:float):
        if self.sacar(valor):
            destino.depositar(valor)
            print(f"Transferência de R${valor:.2f} para a conta {destino.numero} realizada com sucesso.")
        else:
            print("Transferência falhou devido a saldo insuficiente.")
