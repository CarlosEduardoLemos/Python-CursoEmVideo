class ContaBancaria:
    """
    Cria uma conta bancária e permite operações básicas como depósito, saque e exibição do saldo.
    """
    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'Conta {self.id} criada para {self.titular} com saldo inicial de R$ {self.saldo:,.2f}.')

    def __str__(self):
        return f'Conta {self.id} - Titular: {self.titular} - Saldo: R$ {self.saldo:,.2f}'
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R$ {valor:,.2f} realizado com sucesso.')
        else:
            print('Valor de depósito inválido.')
        
    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R$ {valor:,.2f} realizado com sucesso.')
        else:
            print('Saldo insuficiente ou valor de saque inválido.')
    

Conta1 = ContaBancaria(1, 'João Silva', 1000)
Conta1.depositar(500)
Conta1.sacar(200)
print(Conta1)