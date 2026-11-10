# 🎰 Roleta UNIRPIX

Simulador de apostas em **Python**, feito para a disciplina de Programação 2. Permite cadastrar usuários, depositar, apostar em um número da sorte, resgatar saldo e consultar o saldo. Os dados ficam salvos em arquivos **JSON**.

## ▶️ Como executar

Requisito: Python 3.10 ou superior.

```
python main.py
```

Os arquivos `.json` são criados automaticamente na primeira execução.

## 📋 Menu

1. Cadastrar usuário
2. Depositar dinheiro
3. Realizar aposta
4. Resgatar saldo
5. Consultar saldo
6. Sair

## 🎲 Regras da aposta

1. O usuário informa o CPF e o valor da aposta.
2. Escolhe um número de 0 a 10.
3. O programa sorteia um número de 0 a 10.
4. **Acertou:** recebe 10x o valor apostado. **Errou:** perde o valor apostado.

## 🖥️ Exemplo de uso

```
=== 🎰 ROLETA UNIRPIX 🎰 ===
1. Cadastrar usuário
2. Depositar dinheiro
3. Realizar aposta
4. Resgatar saldo
5. Consultar saldo
6. Sair
Opção: 2
CPF (11 dígitos): 12345678900
Olá, Maria! Saldo: R$ 0,00
Valor do depósito: R$ 100
✅ Depósito de R$ 100,00 realizado. Saldo: R$ 100,00
```

## 🗂️ Estrutura do projeto

| Arquivo | Função |
|---|---|
| `main.py` | Menu principal e integração dos módulos |
| `cadastro.py` | Cadastro de usuários (nome e CPF), sem CPF repetido |
| `controle_saldo.py` | Consulta e atualização de saldo, leitura e gravação de JSON |
| `deposito.py` | Depósitos |
| `resgata.py` | Resgates (saques), com verificação de saldo |
| `aposta.py` | Lógica da aposta em número da sorte |

## 💾 Arquivos gerados

**cadastro.json**
```json
[{"nome": "Maria", "cpf": "12345678900", "saldo": 100.0}]
```

**depositos.json**
```json
[{"cpf": "12345678900", "valor_deposito": 100.0}]
```

**saques.json**
```json
[{"cpf": "12345678900", "valor_saque": 20.0}]
```

**apostas.json**
```json
[{"cpf": "12345678900", "valor_apostado": 10.0, "numero_apostado": 5,
  "numero_sorteado": 3, "resultado": "perdeu", "valor_obtido": 0.0}]
```

## ✅ Validações implementadas

- Operações identificadas pelo CPF (11 dígitos, aceita pontos e traço)
- CPF único no cadastro
- Rejeita depósito, aposta ou resgate com valor menor ou igual a zero
- Impede resgatar ou apostar acima do saldo
- Novos registros são adicionados ao final dos arquivos, sem apagar os anteriores
- Funciona mesmo que os arquivos JSON ainda não existam
- Entradas inválidas são tratadas sem fechar o programa
