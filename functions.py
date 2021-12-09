def Saque(valorConta, valorSaque):
    x = valorConta
    x -= valorSaque
    print("\n[OPERAÇÃO DE SAQUE]: Saldo anterior à operação: R${}.\nSaldo após à operação: R${}.\n".format(
        valorConta, x))
    return x


def Deposito(valorConta, valorDeposito):
    x = valorConta
    x += valorDeposito
    print("\n[OPERAÇÃO DE DEPÓSITO]: Saldo anterior à operação: R${}.\nSaldo após à operação: R${}.\n".format(
        valorConta, x))
    return x
