# <Nome do Projeto>

Este é um projeto desenvolvido para a disciplina de **Algoritmos e Programação de Computadores (APC II)** da Univille, que simula um sistema de gerenciamento de informações. O objetivo é aplicar e integrar diversos conceitos fundamentais da programação em Python.

## Funcionalidades

O sistema oferece as seguintes funcionalidades por meio de um menu interativo:

* **Cadastrar**: Permite adicionar novos objetos (ex: veículos, clientes) ao sistema.
* **Listar**: Exibe uma lista de todos os itens cadastrados.
* **Editar**: Permite modificar informações de um item existente.
* **Excluir**: Remove um item do sistema.
* **Consultar**: Busca informações detalhadas de um item específico.
* **Sair**: Encerra o programa.

## Conceitos de Programação Aplicados

O projeto foi desenvolvido para demonstrar a aplicação dos seguintes conceitos:

* **Estruturas de Controle**: Uso de `if`, `for` e `while` para controlar o fluxo do programa.
* **Estruturas de Dados**: Utilização de `listas` para armazenar objetos e `tuplas` para dados fixos.
* **Funções**: Cada funcionalidade foi implementada em uma função específica para organização do código.
* **Tratamento de Exceções**: Uso de blocos `try/except` para lidar com erros, como a consulta de itens que não existem ou a inserção de valores inválidos.
* **Programação Orientada a Objetos (POO)**:
    * Criação de classes com atributos privados.
    * Uso de `@property` e `@setter` para controlar o acesso e a modificação de pelo menos um atributo.
* **Herança**: Implementação de uma classe base e, no mínimo, duas subclasses que herdam dela com atributos adicionais.

## Estrutura do Projeto

O código está organizado em arquivos separados para facilitar a manutenção e a compreensão:

* `_main.py`: Contém o menu interativo e a lógica principal do programa.
* `_classes.py`: Define as classes e subclasses utilizadas no sistema.
* `_funcoes.py`: Armazena as funções que executam as ações do menu.
* `_dados.py`: Contém as listas e tuplas que servem como "banco de dados" temporário.

## Como Executar o Projeto

1.  **Pré-requisitos**: Certifique-se de ter o **Python <versão utilizada>** instalado na sua máquina.
2.  **Clonar o Repositório**:
    ```bash
    git clone [https://github.com/](https://github.com/)<seu-usuario>/<nome-do-repositorio>.git
    ```
3.  **Executar o Programa**:
    Navegue até a pasta do projeto e execute o arquivo principal:
    ```bash
    cd <nome-do-repositorio>
    python _main.py
    ```

## Equipe

* Andrey Rebelatto
* Erick Anderson
* Eduardo Will
