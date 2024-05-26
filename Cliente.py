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

    def filtrar_cliente_por_cpf(self, cpf, clientes):
        clientes_filtrados = [cliente for cliente in clientes if cliente._cpf == cpf]
        return clientes_filtrados[0] if clientes_filtrados else None

    def depositar(self, clientes):
        _cpf = input("Digite o CPF do titular da conta: ")
        cliente = cliente.filtrar_cliente_por_cpf(_cpf, clientes)

        if not cliente:
            print("Cliente não encontrado.")
            return
        
        valor = float(input("Digite o valor do depósito: "))
        transacao = Deposito(valor)

        conta = recuperar_conta(cliente)

        if not conta:
            print("Conta não encontrada.")
            return
        
        cliente.realizar_transacao(conta, transacao)