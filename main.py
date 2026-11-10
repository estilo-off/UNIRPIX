"""Roleta UNIRPIX - menu principal."""
import cadastro, deposito, aposta, resgata
from controle_saldo import ler_cpf, buscar_usuario, moeda, formatar_cpf


def consultar():
    cpf = ler_cpf()
    if cpf is None:
        return
    usuario = buscar_usuario(cpf)
    if usuario is None:
        print("CPF não cadastrado.")
    else:
        print(f"👤 {usuario['nome']} ({formatar_cpf(cpf)})")
        print(f"💰 Saldo: {moeda(usuario['saldo'])}")


def menu():
    acoes = {
        "1": cadastro.cadastrar_usuario,
        "2": deposito.depositar,
        "3": aposta.apostar,
        "4": resgata.resgatar,
        "5": consultar,
    }
    while True:
        print("\n=== 🎰 ROLETA UNIRPIX 🎰 ===")
        print("1. Cadastrar usuário\n2. Depositar dinheiro\n3. Realizar aposta")
        print("4. Resgatar saldo\n5. Consultar saldo\n6. Sair")
        op = input("Opção: ").strip()
        if op == "6":
            print("Até logo!")
            break
        acoes.get(op, lambda: print("Opção inválida."))()


if __name__ == "__main__":
    try:
        menu()
    except (KeyboardInterrupt, EOFError):
        print("\nEncerrado. Até logo!")
