"""Resgate (saque) de saldo."""
from controle_saldo import identificar_usuario, ler_valor, atualizar_saldo, registrar, moeda


def resgatar():
    usuario = identificar_usuario()
    if usuario is None:
        return
    valor = ler_valor("Valor do resgate: R$ ")
    if valor is None:
        return
    if valor > usuario["saldo"]:
        print(f"❌ Saldo insuficiente. Saldo: {moeda(usuario['saldo'])}")
        return
    novo = usuario["saldo"] - valor
    atualizar_saldo(usuario["cpf"], novo)
    registrar("saques.json", {"cpf": usuario["cpf"], "valor_saque": valor})
    print(f"✅ Resgate de {moeda(valor)} realizado. Saldo: {moeda(novo)}")
