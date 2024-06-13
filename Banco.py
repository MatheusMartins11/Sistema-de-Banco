menu = """

[d] Depositar
[w] Sacar
[s] Extrato
[q] Sair

=> """

balance = 0
limit = 500
statement = ""
withdrawal_count = 0
WITHDRAWAL_LIMIT = 3

while True:

    option = input(menu)

    if option == "d":
        amount = float(input("Informe o valor do depósito: "))

        if amount > 0:
            balance += amount
            statement += f"Depósito: R$ {amount:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif option == "w":
        amount = float(input("Informe o valor do saque: "))

        exceeded_balance = amount > balance

        exceeded_limit = amount > limit

        exceeded_withdrawals = withdrawal_count >= WITHDRAWAL_LIMIT

        if exceeded_balance:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif exceeded_limit:
            print("Operação falhou! O valor do saque excede o limite.")

        elif exceeded_withdrawals:
            print("Operação falhou! Número máximo de saques excedido.")

        elif amount > 0:
            balance -= amount
            statement += f"Saque: R$ {amount:.2f}\n"
            withdrawal_count += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif option == "s":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not statement else statement)
        print(f"\nSaldo: R$ {balance:.2f}")
        print("==========================================")

    elif option == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")