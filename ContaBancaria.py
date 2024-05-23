from Historico import Historico
class ContaBancaria:
    def __init__(self, _numero:int, _agencia:int, _titular:str, _saldo:float, _historico:Historico):
        self._numero = _numero
        self._agencia = "0001"
        self._titular = _titular
        self._saldo = 0.00
        self._historico = Historico()
    
    @classmethod
    def nova_conta(cls, numero:int, cliente:str, saldo:float=0.00):
        return cls(numero, cliente, saldo)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def titular(self):
        return self._titular
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def historico(self):
        return self._historico
    
def sacar(self, valor: float) -> bool:
    if valor <= 0:
        print("O valor de saque deve ser positivo.")
        return False
    
    elif valor > self._saldo:
        print("Saldo insuficiente.")
        return False
    
    else:
        self._saldo -= valor
        print(f"Saque de R${valor:.2f} realizado com sucesso.")
        return True

    

'''
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
        if valor <= 0:
            print("O valor de depósito deve ser positivo.")
            return
        self.saldo += valor

    def visualizar_saldo(self) -> float:
        return self.saldo

    def extrato(self)->str:
        return f"Titular: {self.titular}\nNúmero da conta: {self.numero}\nSaldo: {self.saldo}"

    def transferir(self, destino: 'ContaBancaria', valor:float) -> bool:
        
        if self.sacar(valor):
            destino.depositar(valor)
            print(f"Transferência de R${valor:.2f} para a conta {destino.numero} realizada com sucesso.")
            return True
        else:
            print("Transferência falhou devido a saldo insuficiente.")
            return False '''
class ContaCorrente:
    pass 