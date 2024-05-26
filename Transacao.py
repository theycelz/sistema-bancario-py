from abc import ABC, abstractmethod, abstractclassmethod
from ContaBancaria import ContaBancaria
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass
    
    @classmethod
    @abstractclassmethod
    def registrar(cls, conta:ContaBancaria):
        pass

class Deposito:
    def __init__(self, valor:float):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta:ContaBancaria):
        transacao_completa = conta.depositar(self.valor)
        if transacao_completa:
            conta.historico.adicionar_transacao(self)
        else:
            print("Transação não realizada.")

class Saque:
    def __init__(self, valor:float):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta:ContaBancaria):
        transacao_completa = conta.sacar(self.valor)
        if transacao_completa:
            conta.historico.adicionar_transacao(self)
        else:
            print("Transação não realizada.")