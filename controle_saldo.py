"""Controle de saldo + funções utilitárias (JSON, entrada e formatação)."""
import json, math, os, tempfile

PASTA = os.path.dirname(os.path.abspath(__file__))
ARQ_CADASTRO = os.path.join(PASTA, "cadastro.json")


# ---------- JSON ----------
def ler_json(caminho):
    """Lê lista do JSON; retorna [] se o arquivo não existir ou estiver vazio/corrompido."""
    if not os.path.exists(caminho):
        return []
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def salvar_json(caminho, dados):
    """Grava de forma atômica (arquivo temporário + troca) para não corromper dados."""
    fd, tmp = tempfile.mkstemp(dir=PASTA, suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
    os.replace(tmp, caminho)


def registrar(nome_arquivo, registro):
    """Acrescenta um registro ao final da lista do arquivo JSON."""
    caminho = os.path.join(PASTA, nome_arquivo)
    dados = ler_json(caminho)
    dados.append(registro)
    salvar_json(caminho, dados)


# ---------- Formatação ----------
def moeda(valor):
    """1234.5 -> 'R$ 1.234,50'."""
    texto = f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {texto}"


def formatar_cpf(cpf):
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


# ---------- Entrada (repete até ser válida; Enter vazio cancela) ----------
def ler_cpf(texto="CPF (11 dígitos): "):
    """Retorna só os dígitos do CPF, ou None se o usuário cancelar."""
    while True:
        bruto = input(texto).strip()
        if not bruto:
            print("Operação cancelada.")
            return None
        cpf = "".join(c for c in bruto if c.isdigit())
        if len(cpf) == 11:
            return cpf
        print("CPF inválido: informe 11 dígitos (Enter para cancelar).")


def ler_valor(texto):
    """Retorna valor float positivo e finito, ou None se cancelar."""
    while True:
        bruto = input(texto).strip()
        if not bruto:
            print("Operação cancelada.")
            return None
        try:
            valor = round(float(bruto.replace(",", ".")), 2)
        except ValueError:
            print("Valor inválido. Digite um número (Enter para cancelar).")
            continue
        if not math.isfinite(valor):
            print("Valor inválido. Digite um número (Enter para cancelar).")
            continue
        if valor <= 0:
            print("O valor deve ser maior que zero.")
            continue
        return valor


# ---------- Saldo ----------
def buscar_usuario(cpf):
    """Retorna o dicionário do usuário ou None."""
    for u in ler_json(ARQ_CADASTRO):
        if u["cpf"] == cpf:
            return u
    return None


def identificar_usuario():
    """Solicita o CPF e retorna o usuário cadastrado (ou None)."""
    cpf = ler_cpf()
    if cpf is None:
        return None
    usuario = buscar_usuario(cpf)
    if usuario is None:
        print("CPF não cadastrado.")
        return None
    print(f"Olá, {usuario['nome']}! Saldo: {moeda(usuario['saldo'])}")
    return usuario


def consultar_saldo(cpf):
    """Retorna o saldo do CPF ou None se não cadastrado."""
    u = buscar_usuario(cpf)
    return None if u is None else u["saldo"]


def atualizar_saldo(cpf, novo_saldo):
    """Atualiza o saldo do usuário. Retorna True se encontrou o CPF."""
    usuarios = ler_json(ARQ_CADASTRO)
    for u in usuarios:
        if u["cpf"] == cpf:
            u["saldo"] = round(novo_saldo, 2)
            salvar_json(ARQ_CADASTRO, usuarios)
            return True
    return False
