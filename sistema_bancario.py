menu = """

[d] depositar
[s] sacar
[e] extrato
[0] sair

"""

saldo = 0
limite = 500
extrato = ""
n_saques = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        valor_d = float(input('Insira o valor do depósito: \n'))
       
        if valor_d < 0:
            print('Não é possível realizar a operação. Insira um valor válido!\n')
        else:
            saldo += valor_d
            extrato += f'Depósito: R${valor_d:.2f}\n'       
            print('Depósito realizado com sucesso\n')  
    
    elif opcao == 's':
        valor_s = float(input('Insira o valor que deseja sacar: \n'))
        
        excedeu_limite = valor_s > limite
        excedeu_saque = n_saques >= LIMITE_SAQUE
        excedeu_saldo = valor_s > saldo

        if excedeu_saldo:
            print('Não foi possível completar a transação. Saldo insuficiente na conta!\n')
        elif excedeu_saque:
            print('Não foi possível completar a transação. Número máximo de saques diários atingido!\n')
        elif excedeu_limite:
            print('Não foi possível completar a transação. Limite de valor atingido. Só é permitido saque de até R$500.00\n')
        elif valor_s > 0:
            saldo -= valor_s
            extrato += f'Saque: R${valor_d:.2f}\n'
            print('Saque realizado com sucesso\n')
            n_saques += 1
        else:
            print('Não é possível realizar a operação. Insira um valor válido!\n')
    
    elif opcao == 'e':
        print('\n ========== EXTRATO ==========')
        print('Sem movimentações recentes.' if not extrato else extrato)
        print(f'\n Saldo: R${saldo:.2f}')
        print('=============================')

    elif opcao == 0: break

