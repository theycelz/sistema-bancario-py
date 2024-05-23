class Cliente:
    def __init__(self, nome:str, _cpf:str, _endereco:str):
        self.nome = nome
        self._endereco = _endereco
        self.contas = []
    
    def realizar_transacao(self, conta, transacao:str):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)
                           

class PessoaFisica(Cliente):
    def __init__(self, nome:str, endereco:str, data_nascimento:str,cpf:str):
        super().__init__(nome, endereco)
        self._cpf = cpf
        self.data_nascimento = data_nascimento