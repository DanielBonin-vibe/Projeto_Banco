# 🏦 Projeto Banco em Python

Sistema bancário desenvolvido em **Python**, com foco no aprendizado e aplicação prática de programação, banco de dados, SQL e desenvolvimento de APIs REST.

O projeto foi construído de forma modular, utilizando funções e separação de responsabilidades entre os arquivos.

---

## 📌 Sobre o projeto

O **Projeto Banco** simula um sistema bancário capaz de realizar operações relacionadas a clientes, contas e movimentações financeiras.

Durante o desenvolvimento foram aplicados conceitos de:

* Python
* SQLite
* SQL
* CRUD
* Chaves primárias e estrangeiras
* Relacionamentos entre tabelas
* `JOIN`
* Consultas com filtros e ordenações
* Funções
* Modularização
* APIs REST
* FastAPI
* Pydantic
* Uvicorn
* Tratamento e organização de dados
* Relatórios administrativos
* Validação de acesso

O projeto foi desenvolvido em etapas, buscando evoluir gradualmente a estrutura e a complexidade do sistema.

---

# 🎯 Objetivos

O principal objetivo é desenvolver, na prática, um sistema que permita aplicar os conhecimentos adquiridos durante os estudos de Python e Banco de Dados.

Entre os objetivos estão:

* Desenvolver um sistema bancário funcional;
* Trabalhar com persistência de dados utilizando SQLite;
* Praticar operações CRUD;
* Trabalhar com relacionamentos entre tabelas;
* Desenvolver consultas SQL;
* Utilizar `JOIN`, `ORDER BY`, `GROUP BY`, `COUNT`, `CASE` e outras funcionalidades do SQL;
* Criar uma API REST utilizando FastAPI;
* Organizar o projeto em diferentes módulos;
* Desenvolver relatórios administrativos;
* Praticar a separação de responsabilidades dentro de um projeto Python.

---

# ⚙️ Funcionalidades

## 👤 Clientes

O sistema permite trabalhar com informações dos clientes, incluindo:

* Cadastro de clientes;
* Consulta de clientes;
* Busca por CPF;
* Listagem de clientes;
* Identificação através de CPF;
* Relacionamento entre clientes e contas.

---

## 🏦 Contas

O sistema possui funcionalidades relacionadas às contas bancárias, como:

* Criação de contas;
* Consulta de contas;
* Consulta de saldo;
* Encerramento de conta;
* Relacionamento entre conta e cliente.

Cada cliente cadastrado possui uma conta associada de acordo com a lógica definida no projeto.

---

## 💰 Operações bancárias

O sistema permite realizar operações como:

* Consulta de saldo;
* Depósitos;
* Saques;
* Transferências;
* Encerramento de conta.

As operações são realizadas utilizando os dados armazenados no banco SQLite.

---

# 📊 Relatórios

O projeto possui um ambiente separado para relatórios administrativos.

O acesso ao ambiente de relatórios é protegido por uma senha específica e possui **limite de 3 tentativas de autenticação**.

## Relatórios de clientes

Atualmente o sistema possui relatórios como:

* Relatório padrão de clientes, ordenado por ID;
* Relatório de clientes em ordem alfabética;
* Relatório por CPF;
* Relatório por faixa etária.

### Faixa etária

O relatório por faixa etária utiliza recursos SQL para classificar os clientes em grupos:

* 18 a 25 anos;
* 26 a 35 anos;
* 36 a 50 anos;
* 51 anos ou mais.

Nesse relatório são utilizados conceitos como:

* `CASE`;
* `WHEN`;
* `THEN`;
* `ELSE`;
* `COUNT(*)`;
* `GROUP BY`.

---

## Relatórios de contas

O ambiente de relatórios também possui consultas relacionadas às contas, incluindo:

* Relatório padrão de contas;
* Relatório por maior saldo;
* Relatório por nível de saldo.

O relatório por nível de saldo utiliza `CASE` e `COUNT(*)` para classificar as contas de acordo com seu saldo.

---

# 🗄️ Banco de dados

O projeto utiliza **SQLite3** para persistência dos dados.

O banco é armazenado localmente no projeto:

```text
database/
└── banco.db
```

A comunicação com o banco é realizada utilizando o módulo `sqlite3` do Python.

O projeto trabalha com relacionamentos entre as entidades do sistema, permitindo a utilização de consultas envolvendo diferentes tabelas.

---

# 🌐 API REST

O projeto também possui uma API REST desenvolvida utilizando **FastAPI**.

A API permite disponibilizar as operações do sistema através de endpoints HTTP.

Tecnologias utilizadas nessa camada:

* FastAPI;
* Pydantic;
* Uvicorn;
* SQLite3.

Os `BaseModel` utilizados pela API ficam concentrados na camada responsável pela API, enquanto as operações relacionadas ao banco continuam utilizando funções e `sqlite3`.

---

# 🧠 Conceitos de SQL utilizados

Durante o desenvolvimento foram utilizados diversos recursos do SQL, entre eles:

```text
SELECT
INSERT
UPDATE
DELETE
WHERE
LIKE
ORDER BY
GROUP BY
COUNT
SUM
AVG
MIN
MAX
CASE
WHEN
THEN
ELSE
INNER JOIN
LEFT JOIN
```

Esses recursos foram utilizados tanto nas operações do sistema quanto na criação dos relatórios.

---

# 📁 Estrutura do projeto

A estrutura atual do projeto está organizada aproximadamente da seguinte forma:

```text
Projeto_Banco/
│
├── database/
│   └── banco.db
│
├── relatorios/
│   └── validacao.py
│
├── utils/
│   ├── app.py
│   ├── banco_de_dados.py
│   └── menus.py
│
├── banco.py
├── cliente.py
├── conta.py
├── main.py
└── README.md
```

A organização pode continuar sendo modificada conforme novas versões e funcionalidades forem adicionadas.

---

# 🔐 Validação de acesso

O ambiente de relatórios possui uma autenticação própria.

O funcionamento é:

```text
Usuário
   ↓
Solicitação de acesso aos relatórios
   ↓
Senha
   ↓
Senha correta?
   ├── Sim → Acesso aos relatórios
   └── Não → Nova tentativa
                ↓
             3 tentativas
                ↓
           Acesso negado
```

A validação foi separada da lógica dos relatórios para manter uma melhor organização do projeto.

---

# 🛠️ Tecnologias utilizadas

| Tecnologia | Utilização                            |
| ---------- | ------------------------------------- |
| Python     | Linguagem principal                   |
| SQLite3    | Banco de dados                        |
| SQL        | Consultas e manipulação dos dados     |
| FastAPI    | Desenvolvimento da API REST           |
| Pydantic   | Validação e modelagem de dados da API |
| Uvicorn    | Servidor da API                       |

---

# 🚀 Execução

Para executar o projeto, é necessário possuir o Python instalado.

Instale as dependências utilizadas pela API:

```bash
pip install fastapi uvicorn pydantic
```

Depois, execute o sistema pelo arquivo responsável pela inicialização da aplicação.

Para executar a API utilizando Uvicorn:

```bash
uvicorn app:app --reload
```

A forma de execução pode variar de acordo com a estrutura utilizada no ambiente de desenvolvimento.

---

# 📚 Objetivo de aprendizado

Este projeto faz parte dos estudos de **Python, Banco de Dados e desenvolvimento de APIs**.

A ideia é evoluir o sistema progressivamente, começando por operações básicas e aumentando a complexidade através da aplicação prática de novos conceitos.

O projeto também serve como base para praticar:

* organização de projetos Python;
* desenvolvimento de sistemas;
* modelagem de banco de dados;
* SQL;
* APIs REST;
* integração entre aplicação e banco de dados;
* análise de dados através de relatórios.

---

# 🔄 Próximos passos

Possíveis evoluções futuras do projeto:

* novos relatórios administrativos;
* melhorias na autenticação;
* filtros avançados nos relatórios;
* relatórios financeiros;
* melhorias na API REST;
* tratamento de erros mais completo;
* validações adicionais;
* documentação dos endpoints;
* melhorias na organização dos módulos.

---

## 📌 Status do projeto

**Versão atual: 2.0**

O projeto encontra-se em uma versão funcional, contendo operações bancárias, persistência em SQLite, API REST e um ambiente administrativo de relatórios.

**Projeto desenvolvido para fins de estudo e prática de desenvolvimento em Python.**
