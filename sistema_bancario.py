# Sistema Bancário Simples
# Regras:
# 1. O usuário pode depositar valores positivos inteiros.
# 2. O extrato deve ser exibido com o histórico de depósitos e saques.
# 3. O sistema deve permitir realizar 3 saques por dia, com limite de R$ 500,00 por saque.
# 4. O saldo não pode ser negativo.

from datetime import datetime
import os

menu = """
# Sistema Bancário Simples v1.0

 ______________
|_____Menu_____|
|              |
|[d] Depositar |
|[s] Sacar     |
|[e] Extrato   |
|[q] Sair      |
|______________|

=> """

# Variáveis constantes
LIMITE_SAQUES = 3
LIMITE_DIARIO = 500

# Funções do sistema bancário
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def depositar(saldo, extrato):
    limpar_tela()
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        registro_data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        extrato.append(f"{registro_data} - Depósito: R$ {valor:.2f}")
    else:
        print("Operação falhou! O valor informado é inválido.")
    input("\nPressione Enter para continuar...")
    limpar_tela()
    return saldo, extrato

def sacar(saldo, extrato, numero_saques):
    limpar_tela()
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > LIMITE_DIARIO
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
    elif excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    else:
        saldo -= valor
        registro_data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        extrato.append(f"{registro_data} - Saque: R$ {valor:.2f}")
        numero_saques += 1
    input("\nPressione Enter para continuar...")
    limpar_tela()
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    limpar_tela()
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for operacao in extrato:
            print(operacao)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    input("\nPressione Enter para continuar...")
    limpar_tela()

# Loop principal
def main():
    saldo = 0
    numero_saques = 0
    extrato = []

    while True:
        opcao = input(menu)

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques)
        elif opcao == "e":
            exibir_extrato(saldo, extrato)
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
            input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()

# Fim do sistema bancário simples