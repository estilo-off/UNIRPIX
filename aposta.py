"""Aposta em número da sorte (0 a 10)."""
import random
from controle_saldo import identificar_usuario, ler_valor, atualizar_saldo, registrar, moeda

MULTIPLICADOR = 10  # acertou: recebe 10x o valor apostado


def ler_numero():
    """Pede um inteiro de 0 a 10 (repete se inválido; Enter cancela)."""
    while True:
        bruto = input("Escolha um número (0 a 10): ").strip()
        if not bruto:
            print("Operação cancelada.")
            return None
        if bruto.isdigit() and 0 <= int(bruto) <= 10:
            return int(bruto)
        print("Número inválido: digite um inteiro entre 0 e 10.")


def apostar():
    usuario = identificar_usuario()
    if usuario is None:
        return
    saldo = usuario["saldo"]
    valor = ler_valor("Valor da aposta: R$ ")
    if valor is None:
        return
    if valor > saldo:
        print(f"❌ Saldo insuficiente. Saldo: {moeda(saldo)}")
        return
    escolhido = ler_numero()
    if escolhido is None:
        return

    sorteado = random.randint(0, 10)
    if escolhido == sorteado:
        obtido = round(valor * MULTIPLICADOR, 2)
        novo_saldo, resultado = saldo + obtido, "ganhou"
        print(f"🎉 Sorteado: {sorteado}. Você GANHOU {moeda(obtido)}!")
    else:
        obtido = 0.0
        novo_saldo, resultado = saldo - valor, "perdeu"
        print(f"😕 Sorteado: {sorteado}. Você perdeu {moeda(valor)}.")
    atualizar_saldo(usuario["cpf"], novo_saldo)
    registrar("apostas.json", {
        "cpf": usuario["cpf"], "valor_apostado": valor, "numero_apostado": escolhido,
        "numero_sorteado": sorteado, "resultado": resultado, "valor_obtido": obtido,
    })
    print(f"Saldo atual: {moeda(novo_saldo)}")
