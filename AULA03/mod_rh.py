def cadastrar_colaborador(nome: str, cargo: str, salario: float) -> dict:
    return {
        "nome": nome,
        "cargo": cargo,
        "salario": salario
    }

def exibir_colaboradores(lista_colaboradores: list) -> None:
    if not lista_colaboradores:
        print("\n[!] Nenhum colaborador cadastrado.")
        return

    print("\n" + "="*40)
    print(f"{'LISTA DE COLABORADORES':^40}")
    print("="*40)
    
    for i, colab in enumerate(lista_colaboradores, start=1):
        print(f"Colaborador #{i}")
        print(f"  Nome:    {colab['nome']}")
        print(f"  Cargo:   {colab['cargo']}")
        print(f"  Salário: R$ {colab['salario']:.2f}")
        print("-" * 40)
