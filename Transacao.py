from abc import ABC, abstractmethod, abstractclassmethod
from ContaBancaria import ContaBancaria
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass
    
    @classmethod
    @abstractclassmethod
    def registrar(cls, conta):
        pass

class Deposito:
    pass

class Saque:
    pass