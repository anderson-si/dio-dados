

from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self._saldo = saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, Cliente, numero):
        return cls(numero, cliente)
    
    @property    
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo      

        if excedeu_saldo:
            print(f'\n Operação falhou! Você não tem saldo suficiente.')
        
        elif valor > 0: 
            self._saldo -= valor
            print(f'Saque realizado com sucesso! ')
            return True

        else:
            print(f'\n Operação falhou! O valor informado é inválido. ')

    def depositar(self, valor):
        if valor > 0:
            self._saldo += saldo
            print(f'Deposito realizado com sucesso! ')
        else:
            print(f'Operação falhou! O valor! O valor informado é inválido')
            return False

        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saque = 3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saque = limite_saque
    
    def sacar(self, valor):
        numero_saque = len(
            [transacao for transacao in self.
            historico.transacoes if transacao["tipo"] == Saque.__name__]
        )
    
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saque

        if excedeu_limite:
            print("\n Operação falhou! O valor do saque excede o limite. ")
    
        elif excedeu_saques:
            print("\n Operação falhou! Número máxio de saques excedido. ")

        else:
            return super().sacar(valor)
        
        return False

    def __str__(self):
        return f"""\
            Agência: \t {self.agencia}
            C\C: \t\t {self.numero}
            Titular:\t {self.cliente.nome}
        """
    
class Historico:
    def __init__(self):
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.name__,    
                "valor": transacao.valor,    
                "data": datatime.now().strftime("%d-%m-%Y %H:%H:%s")    
            }
        )

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    
    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self.__valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

def menu():
    msnMenu = """
    -------------- MENU - Digite --------------- 
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Criar Conta
    [lc] Listar Contas
    [nc] Novo Cliente
    [q] Sair
    """
    return input(textwrap.dedent(nenu))

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n Cliente não possui conta! ")
        return 
    
    # FIXME: não permite o cliente escolher a conta
    return cliente.contas[0]

def depositar(Clientes):
    cpf = input ("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n Cliente não encontrado! ")
        return 
    
    valor = float(input("Informe o valor do deposito: "))
    Transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return 
    
    cliente.realizar_transacao(conta, Transacao)

def sacar():
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n Cliente não  encontrado! ")
        return 
    valor = float(input("Informe o valor do saque: "))
    Transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return 
    
    cliente.realizar_transacao(conta, Transacao)

def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print(f"\n cliente não encontrado! ")
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return 

    print("\n ============= EXTRATO ============= ")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações. "
    else:
        for transacao in transacoes:
            extrato += f"\n {transacao['tipo']}:\n\t R$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\n Saldo:\n\t R$ {conta.saldo:.2f}")
    print("===================================")

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n Cliente não encontrado, fluxo de criação de conta encerrado! ")

        conta = ContaCorrente.nova_conta(cliente=cliente,
        numero=numero_conta)
        contas.append(conta)
        cliente.contas.append(conta)

        print("\n ==== Conta criada com sucesso! ==== ")
    
def listar_conta(contas):
    for conta in contas:
        print("=" * 40)
        print(textwrap.dedent(str(conta)))
    
def main():
    clientes = []
    contas = []

    while True:
        if opcao == "d":
            depositar(clientes)
        
        elif opcao == "s":
            sacar(clientes)
        
        elif opcao == "e":
            exibir_extrato(clientes)
        
        elif opcao == "nu":
            cirar_cliente(clientes)
        
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        
        elif opcao == "lc":
            listar_contas(contas)
        
        elif opcao == "q":
            break
         
main()