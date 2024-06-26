menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
  opcao =input(menu)
  if opcao == 'd':
    valor = float(input("Informe o valor do deposito: "))
    if valor > 0:
      saldo+=valor

    else:
      print("A operação falhou, valor inválido.")


  elif opcao == 's':
    valor = float(input("Informe o valor do saque: "))
    
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = valor >= limite_saques

    if excedeu_saldo:
      print("Operação falhou, saldo insuficiente.")

    if excedeu_limite:
      print("Operação falhou! O valor do saque excede o limite.")

    if excedeu_saques:
      print("Operação falhou! O número de saques diários excede o limite.")

    elif valor > 0:
      saldo -= valor
      extrato += f"Saque: R$ {valor:.2f}\n"
      numero_saques += 1

    else:
      print("Operação falhou! O valor informado é inválido.")


  elif opcao == 'e':
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

  elif opcao == 'q':
    break
  else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")
