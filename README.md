# 🏦 Sistema Bancário em Python  - (Com Funções)

Um sistema bancário simplificado desenvolvido em Python para demonstração de conceitos fundamentais de programação.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![License](https://img.shields.io/github/license/tertudev/sistema-bancario-com-funcoes?color=green)

## 🧐 Sobre o Projeto

Este repositório apresenta um sistema bancário básico implementado em Python, focado na prática e demonstração de conceitos fundamentais da linguagem. O projeto foi concebido para solidificar conhecimentos em estruturas de controle de fluxo, manipulação de dados com listas e dicionários, e organização de código através de funções.

A abordagem é procedural, com o fluxo principal gerenciado por uma função `main()` que interage com funções auxiliares para cada operação bancária, como depósito, saque e extrato, além de funcionalidades de gestão de usuários e contas. O sistema opera em memória, sem persistência de dados, sendo ideal para estudos e prototipagem rápida.

## ✨ Funcionalidades

O sistema oferece as seguintes operações e características:

*   **Depósito:** Permite adicionar valores à conta, validando que o montante seja positivo.
*   **Saque:** Realiza retiradas de valores, aplicando as seguintes regras:
    *   Limite máximo de R$ 500 por saque.
    *   Limite de 3 saques por sessão.
    *   Verificação de saldo disponível.
*   **Extrato:** Exibe um histórico detalhado de todas as transações (depósitos e saques) realizadas na conta, juntamente com o saldo atual.
*   **Criação de Usuário:** Cadastra novos usuários no sistema, utilizando o CPF como identificador único para evitar duplicidade.
*   **Criação de Conta:** Permite a criação de novas contas bancárias, que são vinculadas a um usuário existente.
*   **Listagem de Contas:** Apresenta uma visão geral de todas as contas cadastradas no sistema.
*   **Sair:** Encerra a execução do sistema.

## 🛠️ Tecnologias

As seguintes tecnologias e conceitos foram empregados no desenvolvimento deste projeto:

*   **Python 3.x:** Linguagem de programação principal.
*   **Variáveis e Tipos Básicos:** Utilização de inteiros, floats e strings.
*   **Estruturas Condicionais:** `if`, `elif`, `else` para controle de fluxo e validações.
*   **Laços de Repetição:** `while` para o menu principal e `for` para iteração sobre dados.
*   **Funções:** Organização do código em blocos reutilizáveis para cada funcionalidade.
*   **Entrada e Saída de Dados:** `input()` para interação com o usuário e `print()` para exibição de informações.
*   **Estruturas de Dados:**
    *   **Listas:** Para armazenar coleções de usuários e contas.
    *   **Dicionários:** Para representar objetos complexos como usuários e contas, com pares chave-valor.

## 🚀 Como Começar

Siga as instruções abaixo para configurar e executar o projeto em sua máquina local.

### Pré-requisitos

Certifique-se de ter o Python 3.x instalado em seu ambiente. Você pode verificar a versão instalada com o comando:

```bash
python --version
```
ou
```bash
python3 --version
```

### Instalação

1.  Clone o repositório para sua máquina local:

    ```bash
    git clone https://github.com/tertudev/sistema-bancario-com-funcoes.git
    ```

2.  Navegue até o diretório do projeto:

    ```bash
    cd sistema-bancario-com-funcoes
    ```

### Execução

Para iniciar o sistema bancário, execute o script principal Python:

```bash
python labproject.py
```

Após a execução, um menu interativo será exibido no terminal, permitindo que você utilize as funcionalidades do sistema.

## 📂 Estrutura

O repositório é composto por um único arquivo Python principal:

*   `labproject.py`: Contém toda a lógica do sistema bancário, organizada em funções para cada operação.

## 🤝 Contribuição

Contribuições são bem-vindas! Se você tiver sugestões de melhoria, novas funcionalidades ou encontrar algum bug, sinta-se à vontade para abrir uma [issue](https://github.com/tertudev/sistema-bancario-com-funcoes/issues) ou enviar um [pull request](https://github.com/tertudev/sistema-bancario-com-funcoes/pulls).

## 📜 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

Vamos codar o futuro! 🚀
