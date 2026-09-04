from mod_rh import cadastrar_colaborador, exibir_colaboradores

def exibir_menu():
    print("\n" + "#"*30)
    print(f"{'SISTEMA DE PRÉ-CADASTRO RH':^30}")
    print("#"*30)
    print("1 - Cadastrar Colaborador")
    print("2 - Listar Colaboradores")
    print("0 - Sair")
    print("#"*30)

def executar_sistema():
    colaboradores_em_memoria = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            print("\n--- NOVO CADASTRO ---")
            nome = input("Digite o nome: ").strip()
            cargo = input("Digite o cargo: ").strip()
            
            try:
                salario = float(input("Digite o salário (ex: 2500.50): "))
            except ValueError:
                print("\n[ERRO] Salário inválido!")
                continue

            novo_colaborador = cadastrar_colaborador(nome, cargo, salario)
            colaboradores_em_memoria.append(novo_colaborador)
            print(f"\n[OK] {nome} cadastrado com sucesso!")

        elif opcao == "2":
            exibir_colaboradores(colaboradores_em_memoria)

        elif opcao == "0":
            print("\n[Saindo] Encerrando o sistema.")
            break
            
        else:
            print("\n[!] Opção inválida.")

if __name__ == "__main__":
    executar_sistema()
