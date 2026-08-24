# 🏦 Projeto Banco em Python

Sistema bancário desenvolvido em **Python**, com foco no aprendizado e aplicação prática de programação, banco de dados, SQL, PostgreSQL e desenvolvimento de APIs REST.

O projeto foi construído de forma modular, utilizando funções, separação de responsabilidades e persistência de dados em PostgreSQL.

---

## 📌 Sobre o projeto

O **Projeto Banco** simula um sistema bancário capaz de realizar operações relacionadas a clientes, contas e movimentações financeiras.

O projeto iniciou utilizando SQLite e, durante sua evolução, foi migrado para **PostgreSQL**, permitindo o estudo de um sistema gerenciador de banco de dados mais robusto e utilizado em aplicações reais.

Durante o desenvolvimento foram aplicados conceitos de:

* Python
* PostgreSQL
* SQL
* Psycopg
* CRUD
* Chaves primárias e estrangeiras
* Relacionamentos entre tabelas
* `JOIN`
* Consultas com filtros e ordenações
* Transações
* `COMMIT`
* `ROLLBACK`
* Funções
* Modularização
* APIs REST
* FastAPI
* Pydantic
* Uvicorn
* Tratamento e organização de dados
* Relatórios administrativos
* Validação de acesso

O projeto foi desenvolvido em etapas, buscando evoluir gradualmente sua estrutura, organização e complexidade.

---

# 🎯 Objetivos

O principal objetivo é desenvolver, na prática, um sistema que permita aplicar os conhecimentos adquiridos durante os estudos de Python, Banco de Dados e desenvolvimento de APIs.

Entre os objetivos estão:

* Desenvolver um sistema bancário funcional;
* Trabalhar com persistência de dados utilizando PostgreSQL;
* Praticar operações CRUD;
* Trabalhar com relacionamentos entre tabelas;
* Desenvolver consultas SQL;
* Utilizar `JOIN`, `ORDER BY`, `GROUP BY`, `COUNT`, `CASE` e outros recursos do SQL;
* Trabalhar com transações utilizando `COMMIT` e `ROLLBACK`;
* Integrar Python com PostgreSQL através do Psycopg;
* Criar uma API REST utilizando FastAPI;
* Organizar o projeto em diferentes módulos;
* Desenvolver relatórios administrativos;
* Praticar separação de responsabilidades;
* Evoluir progressivamente a arquitetura da aplicação.

---

# ⚙️ Funcionalidades

## 👤 Clientes

O sistema permite trabalhar com informações dos clientes, incluindo:

* Cadastro de clientes;
* Consulta de clientes;
* Busca por CPF;
* Listagem de clientes;
* Remoção de cadastro;
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

As contas são relacionadas aos clientes através de uma chave estrangeira utilizando o CPF do titular.

---

## 💰 Operações bancárias

O sistema permite realizar operações como:

* Consulta de saldo;
* Depósitos;
* Saques;
* Transferências;
* Encerramento de conta.

As operações utilizam os dados armazenados no PostgreSQL.

Os cálculos de saldo podem ser realizados diretamente através de comandos SQL, como:

```sql
SET saldo = saldo + valor
```

ou:

```sql
SET saldo = saldo - valor
```

As transferências utilizam transações para garantir maior segurança na alteração dos dados.

Caso toda a operação seja concluída corretamente:

```text
COMMIT
```

confirma as alterações.

Caso ocorra algum erro:

```text
ROLLBACK
```

desfaz as alterações realizadas naquela transação.

---

# 📊 Relatórios

O projeto possui um ambiente separado para relatórios administrativos.

O acesso ao ambiente de relatórios é protegido por uma senha específica e possui **limite de 3 tentativas de autenticação**.

## Relatórios de clientes

O sistema possui relatórios como:

* Relatório padrão de clientes;
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

```text
CASE
WHEN
THEN
ELSE
COUNT(*)
GROUP BY
ORDER BY
```

---

## Relatórios de contas

O ambiente de relatórios também possui consultas relacionadas às contas, incluindo:

* Relatório padrão de contas;
* Relatório por maior saldo;
* Relatório por nível de saldo.

O relatório por nível de saldo utiliza `CASE` e `COUNT(*)` para classificar as contas de acordo com seus saldos.

Também são considerados saldos negativos de acordo com as regras estabelecidas no sistema.

---

# 🗄️ Banco de dados

A partir da versão 3.0, o projeto utiliza **PostgreSQL** para persistência dos dados.

A comunicação entre Python e PostgreSQL é realizada através da biblioteca:

```text
psycopg
```

A conexão com o banco fica centralizada no módulo:

```text
database/
└── conexao_postgre.py
```

O projeto utiliza atualmente duas entidades principais:

```text
clientes
contas
```

## Tabela `clientes`

Possui informações como:

```text
id_cliente
nome
idade
cpf
```

O CPF possui restrição `UNIQUE`, impedindo o cadastro de clientes com CPFs duplicados.

## Tabela `contas`

Possui:

```text
id_conta
cpf_titular
saldo
```

O saldo utiliza:

```sql
NUMERIC(12,2)
```

permitindo o armazenamento de valores monetários com duas casas decimais.

A coluna `cpf_titular` possui uma `FOREIGN KEY` apontando para:

```text
clientes.cpf
```

garantindo o relacionamento entre clientes e contas.

---

# 📄 Schema do banco

A estrutura oficial das tabelas é armazenada em:

```text
database/schema.sql
```

O arquivo permite recriar a estrutura do banco PostgreSQL em outro ambiente.

Estrutura principal:

```sql
CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INTEGER NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS contas (
    id_conta INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    cpf_titular VARCHAR(14) NOT NULL,
    saldo NUMERIC(12,2) NOT NULL DEFAULT 0.00,

    CONSTRAINT fk_contas_clientes
        FOREIGN KEY (cpf_titular)
        REFERENCES clientes(cpf)
);
```

---

# 💾 Backup do PostgreSQL

O banco também pode ser exportado através do pgAdmin utilizando o formato de backup do PostgreSQL.

O `schema.sql` é utilizado para armazenar a estrutura do banco, enquanto backups podem ser utilizados para transportar também os dados armazenados.

Arquivos de backup não devem ser enviados ao Git caso contenham dados reais.

---

# 🌐 API REST

O projeto possui uma API REST desenvolvida utilizando **FastAPI**.

A API permite disponibilizar operações do sistema através de endpoints HTTP.

Tecnologias utilizadas nessa camada:

* FastAPI;
* Pydantic;
* Uvicorn;
* Psycopg;
* PostgreSQL.

A camada da API está organizada separadamente:

```text
api/
├── __init__.py
└── app.py
```

Os modelos utilizados para validação dos dados são definidos com `BaseModel` do Pydantic.

---

# 🧠 Conceitos de SQL utilizados

Durante o desenvolvimento foram utilizados diversos recursos do SQL:

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
PRIMARY KEY
FOREIGN KEY
UNIQUE
NOT NULL
DEFAULT
NUMERIC
RETURNING
```

Também foram utilizados conceitos de transações:

```text
COMMIT
ROLLBACK
```

Esses recursos são utilizados tanto nas operações do sistema quanto na geração de relatórios.

---

# 📁 Estrutura do projeto

A estrutura atual do projeto está organizada aproximadamente da seguinte forma:

```text
Projeto_Banco/
│
├── api/
│   ├── __init__.py
│   └── app.py
│
├── database/
│   ├── __init__.py
│   ├── conexao_postgre.py
│   └── schema.sql
│
├── relatorios/
│   ├── __init__.py
│   └── validacao.py
│
├── utils/
│   ├── __init__.py
│   ├── banco_de_dados.py
│   └── menus.py
│
├── banco.py
├── cliente.py
├── conta.py
├── main.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

Os arquivos `__init__.py` identificam os diretórios como pacotes Python e permitem uma organização mais clara dos módulos.

---

# 🔐 Validação de acesso

O ambiente de relatórios possui autenticação própria.

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
| PostgreSQL | Sistema gerenciador de banco de dados |
| Psycopg    | Comunicação entre Python e PostgreSQL |
| SQL        | Consultas e manipulação dos dados     |
| FastAPI    | Desenvolvimento da API REST           |
| Pydantic   | Validação e modelagem de dados        |
| Uvicorn    | Servidor ASGI da API                  |
| Git        | Versionamento do projeto              |

---

# 📦 Dependências

As dependências externas utilizadas pelo projeto estão registradas no arquivo:

```text
requirements.txt
```

Conteúdo atual:

```text
psycopg[binary]
fastapi
uvicorn
pydantic
```

Para instalar todas as dependências:

```bash
pip install -r requirements.txt
```

---

# 🚀 Execução

## Executar o sistema

Na raiz do projeto:

```bash
python main.py
```

---

## Executar a API

Como o arquivo da API está localizado em:

```text
api/app.py
```

a execução com Uvicorn é:

```bash
uvicorn api.app:app --reload
```

---

# 🔄 Configuração do banco em outro computador

Após clonar o projeto:

```bash
git clone <repositorio>
```

instale as dependências:

```bash
pip install -r requirements.txt
```

Instale e configure o PostgreSQL.

Depois crie o banco:

```text
projeto_banco
```

e execute o arquivo:

```text
database/schema.sql
```

para criar as tabelas.

Caso exista um backup do PostgreSQL, ele também pode ser restaurado através do pgAdmin para recuperar os dados armazenados.

---

# 🚫 Arquivos ignorados pelo Git

O projeto possui um `.gitignore` para evitar o versionamento de arquivos locais ou desnecessários, como:

```text
__pycache__/
*.pyc
venv/
.venv/
.env
*.db
*.backup
.vscode/
```

---

# 📚 Objetivo de aprendizado

Este projeto faz parte dos estudos de **Python, Banco de Dados, PostgreSQL e desenvolvimento de APIs**.

A ideia é evoluir o sistema progressivamente, começando por operações básicas e aumentando a complexidade através da aplicação prática de novos conceitos.

O projeto também serve como base para praticar:

* organização de projetos Python;
* desenvolvimento de sistemas;
* modelagem de banco de dados;
* PostgreSQL;
* SQL;
* transações;
* APIs REST;
* integração entre aplicação e banco de dados;
* análise de dados através de relatórios;
* versionamento com Git.

---

# 🔄 Evolução do projeto

## Versão 1.0

Primeira implementação do sistema bancário utilizando Python e operações básicas.

## Versão 2.0

Evolução do sistema com:

* SQLite;
* persistência de dados;
* API REST;
* FastAPI;
* relatórios administrativos;
* consultas SQL mais avançadas.

## Versão 3.0

Migração da camada de persistência de SQLite para PostgreSQL.

Principais alterações:

* PostgreSQL 18;
* integração através do Psycopg;
* remoção da dependência principal do SQLite;
* criação de `schema.sql`;
* utilização de `NUMERIC(12,2)` para valores financeiros;
* chaves estrangeiras no PostgreSQL;
* utilização de `RETURNING`;
* transações com `COMMIT` e `ROLLBACK`;
* reorganização dos módulos;
* criação da pasta `api`;
* criação de `requirements.txt`;
* criação de `.gitignore`;
* suporte a backup e restauração do banco PostgreSQL.

---

# 🔜 Próximos passos

Possíveis evoluções futuras:

* melhorias na autenticação;
* tratamento de erros mais completo;
* validações adicionais;
* melhorias na API REST;
* documentação dos endpoints;
* novos relatórios financeiros;
* filtros avançados;
* utilização de variáveis de ambiente para credenciais;
* evolução da arquitetura do projeto;
* estudo futuro de SQLAlchemy;
* implementação de migrations.

---

## 📌 Status do projeto

**Versão atual: 3.0**

O projeto encontra-se em uma versão funcional utilizando **Python + PostgreSQL**, contendo operações bancárias, persistência de dados, API REST, relacionamentos entre tabelas, transações e ambiente administrativo de relatórios.

**Projeto desenvolvido para fins de estudo e prática de desenvolvimento em Python, Banco de Dados, PostgreSQL e APIs REST.**
