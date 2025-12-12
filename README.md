# 🏦 Sistema Bancário em Python - (Com Funções)

Este é um projeto **simples de sistema bancário** desenvolvido em Python. O objetivo é praticar conceitos básicos da linguagem, como variáveis, estruturas de decisão, loops e entrada/saída de dados.

## 🔹 Funcionalidades

O sistema permite ao usuário:

1. **Depositar** valores na conta.
2. **Sacar** valores respeitando saldo, limite diário e número máximo de saques.
3. Consultar o **extrato** das movimentações.
4. **Criar novo usuário** com CPF e nome.
5. **Criar nova conta** vinculada a um usuário existente.
6. **Listar contas** cadastradas.
7. **Sair** do sistema.

## 🔹 Regras Implementadas

- Cada saque respeita um **limite máximo** (R$ 500) e o número máximo de saques por sessão (3 saques).
- Não é permitido depositar ou sacar valores negativos ou inválidos.
- Cada usuário é identificado pelo **CPF**, evitando duplicidade.
- O extrato exibe todas as movimentações realizadas na conta.

## 🔹 Estrutura do Código

O código é organizado em funções simples:

- `menu()`: exibe o menu principal e retorna a opção escolhida.
- `depositar(saldo, extrato)`: permite realizar depósitos válidos.
- `sacar(saldo, extrato, limite, numero_saques, limite_saques)`: realiza saques verificando saldo, limite e quantidade de saques.
- `exibir_extrato(saldo, extrato)`: mostra todas as movimentações e o saldo atual.
- `criar_usuario(usuarios)`: cadastra novos usuários evitando duplicidade de CPF.
- `criar_conta(contas, usuarios, agencia)`: cria novas contas vinculadas a usuários existentes.
- `listar_contas(contas)`: exibe informações de todas as contas cadastradas.
- `main()`: controla o fluxo principal do sistema.

## 🔹 Tecnologias e Conceitos Usados

- **Python 3**
- Variáveis e tipos básicos
- Estruturas condicionais: `if`, `elif`, `else`
- Laços de repetição: `while`, `for`
- Entrada de dados com `input()`
- Saída de dados com `print()`
- Listas e dicionários para armazenar usuários e contas

## 🔹 Como Usar

1. Salve o arquivo do projeto como `sistema_bancario.py`.
2. Execute no terminal ou em um ambiente Python.
3. Escolha as opções do menu para interagir com o sistema.
4. Para sair, selecione a opção `q`.

## 🔹 Aprendizados

Com este projeto foi possível:

- Praticar lógica de programação básica em Python.
- Criar funções simples e reutilizáveis.
- Trabalhar com listas e dicionários para organizar dados.
- Desenvolver um pequeno sistema funcional que pode ser expandido futuramente.

**Vamos codar o futuro! 🚀**
