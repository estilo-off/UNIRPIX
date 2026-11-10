"""Cadastro de usuários em cadastro.json."""
from controle_saldo import ARQ_CADASTRO, ler_json, salvar_json, ler_cpf, buscar_usuario


def cadastrar_usuario():
    nome = input("Nome: ").strip()
    if not nome:
        print("Nome é obrigatório.")
        return
    cpf = ler_cpf()
    if cpf is None:
        return
    if buscar_usuario(cpf):
        print("CPF já cadastrado.")
        return
    usuarios = ler_json(ARQ_CADASTRO)
    usuarios.append({"nome": nome, "cpf": cpf, "saldo": 0.0})
    salvar_json(ARQ_CADASTRO, usuarios)
    print(f"✅ {nome} cadastrado(a) com sucesso! Saldo inicial: R$ 0,00")
