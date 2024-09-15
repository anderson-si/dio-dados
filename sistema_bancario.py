
SALDO_DA_CONTA = 0
arrayQtdDeposito = []
arrayQtdSaque = []

def depositar(valorDeposito):
    global SALDO_DA_CONTA
    if (valorDeposito <= 0):
        print ("Tipo de depósito não permitido para esse valor!\n")
    else:
        arrayQtdDeposito.append(valorDeposito)
        SALDO_DA_CONTA += valorDeposito 
        print (f'Deposito no valor de R$ {valorDeposito:.2f} realizado com sucesso! ')
      
def sacar(valorSaque):
    global SALDO_DA_CONTA
    if ((valorSaque > SALDO_DA_CONTA) or (SALDO_DA_CONTA - valorSaque) < 0):
        print ("Saldo insulficiente! \n")
    elif (len(arrayQtdSaque) >= 3):
        print ("Atingiu limite de saque diário \n")
    elif (valorSaque > 500):
        print ("Valor Acima do Permitido \n")
    else:
        SALDO_DA_CONTA -= valorSaque
        arrayQtdSaque.append(valorSaque)
        print ("Saque realizado com sucesso! ")  
    
def extrato():
    print("\n")
    print("----------------------")
    print("       EXTRATO        ")
    print("      depositos       ")
    if (len(arrayQtdDeposito) > 0):
        for i in arrayQtdDeposito:
            print (f'R$ {i:.2f}')
    else:
        print("Nenhum deposito registrado!")
    print("        Saque         ")
    if (len(arrayQtdSaque) > 0):
        for i in arrayQtdSaque:
            print (f'R$ {i:.2f}')
    else: 
        print("Nenhum saque registrado!")
    print("        Saldo         ")
    print(f'R$ {SALDO_DA_CONTA:.2f}')
    print("----------------------")

msnInicial =  """
            ============= BANCO FICTICIO: =============
              Operações disponíveis para nosso cliente

            ------------------ MENU ------------------- 
            [q] para 'sair'
            [s] para 'sacar'
            [d] para 'depositar'
            [e] para 'consultar o extrato'
            
        """

msnFinal = """
            ============================================
                        FIM DA OPERAÇÃO            
        """
print ( msnInicial )
while True:
    op = input("Escolha uma das opções do MENU Acima: " )
    if (op.upper() == 'Q'):
        print(msnFinal)
        break
    elif (op.upper() == 'S'):
        sacar(float(input("Digite o valor que deseja sacar: ")))
    elif (op.upper() == 'D'):
        depositar(float(input("Digite o valor que deseja depositar: ")))
    elif (op.upper() == 'E'):
        extrato()
    else:
        print("Opção inválida, tente novamente! \n")    