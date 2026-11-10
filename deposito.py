"""Depósito de dinheiro."""
from controle_saldo import identificar_usuario, ler_valor, atualizar_saldo, registrar, moeda


def depositar():
    usuario = identificar_usuario()
    if usuario is None:
        return
    valor = ler_valor("Valor do depósito: R$ ")
    if valor is None:
        return
    novo = usuario["saldo"] + valor
    atualizar_saldo(usuario["cpf"], novo)
    registrar("depositos.json", {"cpf": usuario["cpf"], "valor_deposito": valor})
    print(f"✅ Depósito de {moeda(valor)} realizado. Saldo: {moeda(novo)}")
