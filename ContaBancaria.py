from Historico import Historico
from Historico import Saque
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

def depositar(self, valor: float):
    if valor <= 0:
        print("O valor de depósito deve ser positivo.")
        return False
    else:
        self._saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        return True

''''
    def visualizar_saldo(self) -> float:
        return self.saldo


    def transferir(self, destino: 'ContaBancaria', valor:float) -> bool:
        
        if self.sacar(valor):
            destino.depositar(valor)
            print(f"Transferência de R${valor:.2f} para a conta {destino.numero} realizada com sucesso.")
            return True
        else:
            print("Transferência falhou devido a saldo insuficiente.")
            return False '''
class ContaCorrente:
    def __init__(self, _numero:int, _titular:str, _historico:Historico, _limite:float=700, limite_saques:int=3):
        super().__init__(_numero, _titular, _historico)
        self._numero = _numero
        self._limite = _limite
        self._limite_saques = limite_saques

    def sacar(self, valor: float) -> bool:

        numero_saques = len([transacao for transacao in self._historico.transacoes if transacao["tipo"] == Saque.__name__])
        
        excedeu_limite = valor > self._limite 
        excedeu_limite_saques = numero_saques >= self._limite_saques
        
        if excedeu_limite:
            print("Saque não permitido, o valor excedeu limite.")
        elif excedeu_limite_saques:
            print("Saque não permitido, excedeu o limite de saques.")
        else:
            return super().sacar(valor)
        return False
    
    def __str__(self):
        return f"""\
        Agência:\t{self.agencia}
        Número:\t\t{self.numero}
        Titular:\t{self.titular}"""

