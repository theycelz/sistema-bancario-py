from Transacao import Deposito, Saque
from ContaBancaria import ContaCorrente
import textwrap

CLIENTE_NAO_ENCONTRADO = "Cliente não encontrado."
CPF_PROMPT = "Digite o CPF do titular da conta: "

class Cliente:
    def __init__(self, nome: str, _cpf: str, _endereco: str):
        self.nome = nome
        self._endereco = _endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao: str):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome: str, endereco: str, data_nascimento: str, cpf: str):
        super().__init__(nome, endereco)
        self._cpf = cpf
        self.data_nascimento = data_nascimento

    @staticmethod
    def filtrar_cliente_por_cpf(cpf, clientes):
        clientes_filtrados = [cliente for cliente in clientes if cliente._cpf == cpf]
        return clientes_filtrados[0] if clientes_filtrados else None

    @staticmethod
    def recuperar_conta(cliente):
        if not cliente.contas:
            print("Cliente não possui contas.")
            return

        if len(cliente.contas) > 1:
            print("Escolha a conta:")
            for i, conta in enumerate(cliente.contas):
                print(f"{i + 1}. {conta}")
            escolha = int(input("Digite o número da conta: "))
            if escolha < 1 or escolha > len(cliente.contas):
                print("Escolha inválida.")
                return cliente.contas[0]
            return cliente.contas[escolha - 1]

        return cliente.contas[0]
    


    def depositar(self, clientes):
        _cpf = input(CPF_PROMPT)
        cliente = self.filtrar_cliente_por_cpf(_cpf, clientes)

        if not cliente:
            print(CLIENTE_NAO_ENCONTRADO)
            return

        valor = float(input("Digite o valor do depósito: "))
        transacao = Deposito(valor)
        conta = self.recuperar_conta(cliente)

        if not conta:
            print(CLIENTE_NAO_ENCONTRADO)
            return
        cliente.realizar_transacao(conta, transacao)

    def sacar(self, clientes):
        _cpf = input(CPF_PROMPT)
        cliente = self.filtrar_cliente_por_cpf(_cpf, clientes)

        if not cliente:
            print(CLIENTE_NAO_ENCONTRADO)
            return

        valor = float(input("Digite o valor do saque: "))
        transacao = Saque(valor)
        conta = self.recuperar_conta(cliente)

        if not conta:
            print("Conta não encontrada.")
            return
        cliente.realizar_transacao(conta, transacao)
    

    def exibir_extrato(self, clientes):
        _cpf = input(CPF_PROMPT)
        cliente = self.filtrar_cliente_por_cpf(_cpf, clientes)

        if not cliente:
            print(CLIENTE_NAO_ENCONTRADO)
            return

        conta = self.recuperar_conta(cliente)

        if not conta:
            print("Conta não encontrada.")
            return

        print("\n============= Extrato =============")
        transacoes = conta.historico.transacoes

        extrato = ""
        if not transacoes:
            extrato = "Nenhuma transação realizada."
        else:
            for transacao in transacoes:
                extrato += f"\n{transacao['tipo']} de R${transacao['valor']:.2f} em {transacao['data']}"
        print(extrato)
        print(f"\nSaldo atual: R${conta.saldo:.2f}")
        print("===================================")

    def criar_conta(self, clientes):
        _cpf = input(CPF_PROMPT)
        cliente = self.filtrar_cliente_por_cpf(_cpf, clientes)

        if not cliente:
            print(CLIENTE_NAO_ENCONTRADO)
            return None

        else:
            numero = int(input("Digite o número da conta: "))
            titular = input("Digite o nome do titular: ")
            saldo = float(input("Digite o saldo inicial: "))
            conta = ContaCorrente(numero, titular, saldo)
            cliente.adicionar_conta(conta)
            print("Conta criada com sucesso.")
            return conta
    
    def listar_contas(self,contas):
        for conta in contas: 
            print("="*100)
            print(textwrap.dedent(str(conta)))

    def criar_cliente(self,clientes):
        cpf = input("Digite o CPF do cliente: ")
        cliente = self.filtrar_cliente_por_cpf(cpf,clientes)
        if cliente:
            print("Cliente já cadastrado.")
            return cliente
        
        nome = input("Digite o nome do cliente: ")
        endereco = input("Digite o endereço do cliente: ")
        data_nascimento = input("Digite a data de nascimento do cliente: ")
        cliente = PessoaFisica(nome,endereco,data_nascimento,cpf)
        clientes.append(cliente)
        print("Cliente criado com sucesso.")
        return cliente

    def listar_clientes(self,clientes):
        for cliente in clientes:
            print("="*100)
            print(f"Nome: {cliente.nome}\nCPF: {cliente._cpf}\nEndereço: {cliente._endereco}\nData de Nascimento: {cliente.data_nascimento}")