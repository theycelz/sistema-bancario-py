from Transacao import Deposito, Saque
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

    def recuperar_conta(self, cliente):
        if not cliente.contas:
            print("Cliente não possui contas.")
            return 
        
        if len(cliente.contas) > 1:
            print("Escolha a conta:")
            for i, conta in enumerate(cliente.contas):
                print(f"{i+1}. {conta}")
            escolha = int(input("Digite o número da conta: "))
            if escolha < 1 or escolha > len(cliente.contas):
                print("Escolha inválida.")
                return cliente.contas[0]
            return cliente.contas[escolha-1]
        
        return cliente.contas[0]

    def depositar(self, clientes):
        _cpf = input("Digite o CPF do titular da conta: ")
        cliente = cliente.filtrar_cliente_por_cpf(_cpf, clientes)

        if not cliente:
            print("Cliente não encontrado.")
            return
        
        valor = float(input("Digite o valor do depósito: "))
        transacao = Deposito(valor)
        conta = cliente.recuperar_conta(cliente)  

        if not conta:
            print("Conta não encontrada.")
            return
        cliente.realizar_transacao(conta, transacao)

    def sacar(self, clientes):
        _cpf = input("Digite o CPF do titular da conta: ")
        cliente = cliente.filtrar_cliente_por_cpf(_cpf, clientes)

        if not cliente:
            print("Cliente não encontrado.")
            return
        
        valor = float(input("Digite o valor do saque: "))
        transacao = Saque(valor)
        conta = cliente.recuperar_conta(cliente)  

        if not conta:
            print("Conta não encontrada.")
            return
        cliente.realizar_transacao(conta, transacao)