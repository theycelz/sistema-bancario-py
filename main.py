from ContaBancaria import ContaBancaria

class Main:
    conta1 = ContaBancaria(1, "Alice", 1000)
    conta2 = ContaBancaria(2, "Bob", 500)

    conta1.depositar(200)
    conta1.sacar(150)
    conta1.transferir(conta2, 300)
    print(conta1.visualizar_saldo())
    print(conta2.visualizar_saldo())