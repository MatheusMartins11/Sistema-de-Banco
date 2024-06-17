def deposit(balance, statement):
    amount = float(input("Informe o valor do depósito: "))
    if amount > 0:
        balance += amount
        statement += f"Depósito: R$ {amount:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return balance, statement

def withdraw(balance, limit, statement, withdrawal_count, WITHDRAWAL_LIMIT):
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
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return balance, statement, withdrawal_count

def show_statement(balance, statement):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not statement else statement)
    print(f"\nSaldo: R$ {balance:.2f}")
    print("==========================================")

def main_menu():
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
            balance, statement = deposit(balance, statement)
        elif option == "w":
            balance, statement, withdrawal_count = withdraw(balance, limit, statement, withdrawal_count, WITHDRAWAL_LIMIT)
        elif option == "s":
            show_statement(balance, statement)
        elif option == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main_menu()
