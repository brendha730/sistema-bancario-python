
def menu_principal():
    return """
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuário
[nc] Nova Conta
[lc] Listar Contas
[q] Sair
=> """

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("✅ Depósito realizado com sucesso!")
    else:
        print("❌ Valor inválido para depósito.")
    return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("❌ Saldo insuficiente.")
    elif valor > limite:
        print("❌ Limite de saque excedido.")
    elif numero_saques >= limite_saques:
        print("❌ Número máximo de saques atingido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("✅ Saque realizado com sucesso!")
    else:
        print("❌ Valor inválido.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n========== EXTRATO ==========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=============================\n")

def criar_usuario(usuarios):
    cpf = input("Digite o CPF (apenas números): ")
    if any(u['cpf'] == cpf for u in usuarios):
        print("❌ CPF já cadastrado.")
        return
    nome = input("Nome completo: ")
    data_nasc = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, nº - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nasc": data_nasc, "cpf": cpf, "endereco": endereco})
    print("✅ Usuário criado com sucesso!")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o CPF do usuário: ")
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)
    if usuario:
        print("✅ Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print("❌ Usuário não encontrado.")
        return None

def listar_contas(contas):
    for conta in contas:
        print(f"""
Agência: {conta['agencia']}
Conta: {conta['numero_conta']}
Titular: {conta['usuario']['nome']}
----------------------""")

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        opcao = input(menu_principal())

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES)

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("👋 Obrigado por usar nosso sistema bancário!")
            break

        else:
            print("❌ Operação inválida, selecione novamente.")

if __name__ == "__main__":
    main()
