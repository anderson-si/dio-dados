
import textwrap

msnInicial = """
            ============= BANCO FICTICIO: =============
              Operações disponíveis para nosso cliente  
        """

msnFinal = """
            ============================================
                        FIM DA OPERAÇÃO            
        """

msnMenu = """
            -------------- MENU - Digite --------------- 
            [q] Sair
            [s] Sacar
            [d] Depositar
            [e] Extrato
           [cc] Criar Conta
           [lc] Listar Contas
           [nc] Novo Cliente
    """

def main():

    LIMITE_SAQUES = 3
    NUM_AGENCIA = '0001'
    
    limite = 500
    saldo = 0
    numero_saques = 0
    extrato = ""
    num_conta = 1
    arrayClientes = []
    arrayContas = []
    
    print(msnInicial)
    while True:
        op = menu()
        
        if (op.upper() == 'Q'):
            print(msnFinal)
            break
        
        elif (op.upper() == 'S'):
            valor = float(input("Digite o valor que deseja sacar: "))
             
            saldo, extrato, numero_saques = sacar (
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=LIMITE_SAQUES,
                numero_saques=numero_saques,
                limite_saque=limite
            )
        
        elif (op.upper() == 'D'):
            valor = float(input("Digite o valor que deseja depositar: "))
            saldo, extrato = depositar(saldo, valor, extrato)
            
        elif (op.upper() == 'E'):
            exibir_extrato(saldo, extrato=extrato)
        
        elif (op.upper() == "NC"):
            cadastrar_cliente(arrayClientes)
        
        elif (op.upper() == "CC"):
            conta = criar_conta(NUM_AGENCIA, num_conta, arrayClientes)
            
            if conta:
                arrayContas.append(conta)
                num_conta += 1
            
        elif (op.upper() == "LC"):
            listar_contas(arrayContas)
        
        else:
            print("Opção inválida, tente novamente! \n")   

def menu():
    print(msnMenu)
    op = input("Escolha uma das opções do MENU Acima: " )
    return op

def cadastrar_cliente(arrayClientes):
    cpf = input("Informe o CPF (Somente números): ")
    usuario = filtrar_cliente(cpf, arrayClientes)
    
    if usuario:
        print("\nJá existe usuário com esse CPF! ")
        return
    
    nome = input("Informe o nome completo: ")
    data_nasc = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    
    arrayClientes.append({"nome": nome, "data_nascimento": data_nasc, "cpf": cpf, "endereco": endereco})
    print("Cliente cadastrado com sucesso! ")    
    
    return None
 
def criar_conta(agencia, num_conta, arrayClientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, arrayClientes)
    
    if cliente:
        print("Conta criada com sucesso! ")
        return {"agencia": agencia, "num_conta": num_conta, "cliente": cliente }

    print("Cliente não encontrado, fluxo de criação de conta encerrado! ")
    
def listar_contas(arrayContas):
    if len(arrayContas) == 0:
        print ("Não há contas cadastradas\n")
        return None
    for conta in arrayContas:
        linha = f"""\
                Agência: \t{conta['agencia']}
                C/C:\t\t{conta['num_conta']}
                Titular:\t{conta['cliente']['nome']}
        """
        print("=" * 70)
        print(textwrap.dedent(linha))
    
def filtrar_cliente(cpf, arrayClientes):
    usuarios_filtrados = [cliente for cliente in arrayClientes if cliente["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def depositar(saldo, valor, extrato, /):
    if (valor <= 0):
        print ("Tipo de depósito não permitido para esse valor!\n")
    else:
        saldo += valor
        extrato = f'Deposito: \tR$ {valor:.2f} \n'
        print(f'Deposito no valor de R$ {valor:.2f} realizado com sucesso! ')
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saque):
    excedeu_saldo = valor > saldo
    excedeu_valor_saque = valor > limite_saque
    excedeu_qtd_saque = numero_saques >= limite

    if excedeu_qtd_saque:
        print(f'Excedeu o limite de saque diário \n')
    
    elif excedeu_saldo:
        print(f'Saldo insulficiente!\n')    
    
    elif excedeu_valor_saque:
       print(f'Valor do saque acima do Permitido \n')
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n Saque realizado com sucesso! ")

    else:
        print ("Valor inválido \n")  
    
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("============= BANCO FICTICIO: =============\n")
    print("Não foram realizadas movimentações. " if not extrato else extrato)
    print(f"Saldo:\t\tR$ {saldo:.2f}")
    print("===========================================\n")
    

main()