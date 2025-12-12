def menu():
    print("\n=============== MENU ================")
    print("[d] Depositar")
    print("[s] Sacar")
    print("[e] Extrato")
    print("[nu] Novo usuário")
    print("[nc] Nova conta")
    print("[lc] Listar contas")
    print("[q] Sair")
    return input("Escolha uma opção: ")


def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += "Depósito: R$ " + str(valor) + "\n"
        print("Depósito realizado!")
    else:
        print("Valor inválido!")
    return saldo, extrato


def sacar(saldo, extrato, limite, numero_saques, limite_saques):
    valor = float(input("Informe o valor do saque: "))
    if valor <= 0:
        print("Valor inválido!")
    elif valor > saldo:
        print("Saldo insuficiente!")
    elif valor > limite:
        print("Valor acima do limite!")
    elif numero_saques >= limite_saques:
        print("Limite de saques atingido!")
    else:
        saldo -= valor
        extrato += "Saque: R$ " + str(valor) + "\n"
        numero_saques += 1
        print("Saque realizado!")
    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato):
    print("\n============== EXTRATO ==============")
    if extrato == "":
        print("Nenhuma movimentação.")
    else:
        print(extrato)
    print("Saldo: R$ " + str(saldo))
    print("====================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF: ")
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Usuário já existe!")
            return
    nome = input("Informe o nome: ")
    usuarios.append({"nome": nome, "cpf": cpf})
    print("Usuário criado!")


def criar_conta(contas, usuarios, agencia):
    cpf = input("Informe o CPF do usuário: ")
    usuario = None
    for u in usuarios:
        if u["cpf"] == cpf:
            usuario = u
            break
    if usuario:
        numero_conta = len(contas) + 1
        conta = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
        contas.append(conta)
        print("Conta criada!")
    else:
        print("Usuário não encontrado!")


def listar_contas(contas):
    for conta in contas:
        print("Agência:", conta["agencia"])
        print("C/C:", conta["numero_conta"])
        print("Titular:", conta["usuario"]["nome"])
        print("=" * 30)


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_saques = 3
    agencia = "0001"
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(
                saldo, extrato, limite, numero_saques, limite_saques
            )
        elif opcao == "e":
            exibir_extrato(saldo, extrato)
        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "nc":
            criar_conta(contas, usuarios, agencia)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")


main()
