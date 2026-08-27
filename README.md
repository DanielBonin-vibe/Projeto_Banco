# 🏦 Projeto Banco em Python

Sistema bancário desenvolvido em **Python**, utilizando **PostgreSQL** para persistência de dados, organização em camadas, separação de regras de negócio e uma API REST desenvolvida com **FastAPI**.

O projeto foi criado com fins de estudo e vem sendo evoluído através de diferentes versões, acompanhando o aprendizado de Python, Banco de Dados, SQL, arquitetura de software e desenvolvimento de APIs.

---

## 📌 Sobre o projeto

O **Projeto Banco** simula um sistema bancário capaz de gerenciar clientes, contas, operações financeiras e relatórios administrativos.

A versão **4.0** representa uma grande refatoração da estrutura interna do projeto.

Entre as principais mudanças estão:

* Migração definitiva do SQLite para PostgreSQL;
* Criação da camada de `repositories`;
* Criação da camada de `services`;
* Separação entre acesso aos dados e regras de negócio;
* Refatoração dos menus;
* Refatoração do `main.py`;
* Reorganização das operações bancárias;
* Uso de variáveis de ambiente;
* Remoção das credenciais do código-fonte;
* Criação do `.gitignore`;
* Organização das dependências através do `requirements.txt`;
* Melhor separação de responsabilidades entre os módulos.

---

# 🎯 Objetivo

O principal objetivo do projeto é desenvolver, na prática, um sistema capaz de aplicar conceitos estudados durante o aprendizado de desenvolvimento de software.

Entre os conceitos praticados estão:

* Python;
* PostgreSQL;
* SQL;
* CRUD;
* Chaves primárias e estrangeiras;
* Relacionamentos entre tabelas;
* Transações;
* Consultas com filtros;
* `JOIN`;
* `GROUP BY`;
* `ORDER BY`;
* Funções;
* Modularização;
* Separação de responsabilidades;
* Repository Pattern;
* Camada de Service;
* Tratamento de exceções;
* Variáveis de ambiente;
* APIs REST;
* FastAPI;
* Pydantic;
* Uvicorn.

---

# ⚙️ Funcionalidades

## 👤 Clientes

O sistema possui funcionalidades relacionadas ao gerenciamento de clientes:

* Cadastro de clientes;
* Listagem de clientes;
* Atualização de dados;
* Remoção de clientes;
* Identificação através do CPF;
* Relacionamento entre clientes e contas.

As regras de negócio relacionadas aos clientes são tratadas pelos `services`, enquanto as operações diretamente relacionadas ao banco são realizadas pelos `repositories`.

---

## 🏦 Contas

O sistema permite realizar operações relacionadas às contas bancárias:

* Criar conta;
* Buscar conta;
* Listar contas;
* Consultar saldo;
* Encerrar conta;
* Relacionar a conta ao CPF do titular.

O fluxo utilizado é:

```text
main.py
   ↓
service
   ↓
repository
   ↓
PostgreSQL
```

---

## 💰 Operações bancárias

As movimentações financeiras foram separadas das funcionalidades de gerenciamento das contas.

Atualmente estão disponíveis:

* Depósitos;
* Saques;
* Transferências.

### Depósitos

O sistema impede depósitos com valores menores ou iguais a zero.

### Saques

Antes da realização de um saque são verificadas condições como:

* Existência da conta;
* Valor solicitado;
* Saldo disponível.

Não é permitido realizar um saque superior ao saldo existente.

### Transferências

As transferências trabalham com duas contas dentro de uma mesma transação.

Entre as validações realizadas estão:

* O valor deve ser maior que zero;
* O transferidor deve possuir saldo suficiente;
* Não é possível realizar transferência para a própria conta;
* As duas contas devem participar corretamente da operação.

O `commit` somente é realizado após a conclusão das duas etapas da transferência.

Caso alguma parte da operação falhe, é utilizado `rollback`.

```text
Conta transferidora
       ↓
    débito
       ↓
Conta recebedora
       ↓
    crédito
       ↓
     commit
```

Em caso de erro:

```text
erro
 ↓
rollback
```

---

# 📊 Relatórios administrativos

O projeto possui um ambiente separado para relatórios administrativos.

O acesso ao ambiente passa por uma validação de senha com limite de tentativas.

```text
Menu Principal
      ↓
Relatórios
      ↓
Validação
      ↓
Senha correta?
   ├── Sim → Menu de relatórios
   └── Não → Acesso negado
```

A própria função responsável pela validação controla o número de tentativas.

Como os relatórios atuais são compostos principalmente por consultas SQL, eles acessam diretamente o `relatorios_repository`, sem necessidade de uma camada de `service` exclusiva.

---

## 👤 Relatórios de clientes

Entre os relatórios disponíveis estão:

* Relatório geral de clientes;
* Clientes em ordem alfabética;
* Relatório por CPF;
* Relatório por faixa etária.

Os relatórios utilizam diferentes recursos SQL para organizar, filtrar e agrupar os dados.

---

## 🏦 Relatórios de contas

Também estão disponíveis relatórios relacionados às contas:

* Relatório geral de contas;
* Relatório por saldo;
* Relatório por nível de saldo.

---

# 🗄️ Banco de Dados

O projeto utiliza **PostgreSQL** para persistência dos dados.

A comunicação entre Python e PostgreSQL é realizada através do:

```text
psycopg
```

A estrutura inicial das tabelas está definida em:

```text
database/schema.sql
```

A conexão com o PostgreSQL fica centralizada em:

```text
database/conexao_postgre.py
```

---

# 🔐 Variáveis de ambiente

As credenciais e configurações sensíveis não ficam armazenadas diretamente no código.

Elas são definidas através de um arquivo:

```text
.env
```

Exemplo:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=projeto_banco
DB_USER=postgres
DB_PASSWORD=sua_senha

RELATORIOS_PASSWORD=sua_senha
```

As variáveis são carregadas utilizando:

```python
from dotenv import load_dotenv
```

e acessadas através de:

```python
os.getenv()
```

O arquivo `.env` é ignorado pelo Git e não deve ser enviado ao repositório.

---

# 🧱 Arquitetura

A versão 4.0 trouxe uma divisão mais clara das responsabilidades da aplicação.

## Database

A camada `database` contém os recursos relacionados à configuração do PostgreSQL.

```text
database/
├── __init__.py
├── conexao_postgre.py
└── schema.sql
```

---

## Repositories

Os repositories são responsáveis pela comunicação direta com o banco.

```text
repositories/
├── __init__.py
├── cliente_repository.py
├── conta_repository.py
└── relatorios_repository.py
```

Entre suas responsabilidades estão:

* `SELECT`;
* `INSERT`;
* `UPDATE`;
* `DELETE`;
* Consultas SQL;
* Controle de `commit`;
* Controle de `rollback`;
* Retorno dos dados obtidos do PostgreSQL.

As regras de negócio não devem ficar concentradas nessa camada.

---

## Services

A camada de `services` fica entre a interface da aplicação e os repositories.

```text
services/
├── __init__.py
├── cliente_service.py
└── conta_service.py
```

Ela é responsável por:

* Validações;
* Regras de negócio;
* Verificação de condições;
* Tratamento dos resultados dos repositories;
* Impedir operações inválidas.

Exemplo:

```text
Usuário
   ↓
main.py
   ↓
service
   ↓
repository
   ↓
PostgreSQL
```

---

## Utils

A pasta `utils` contém recursos auxiliares utilizados pela aplicação.

Atualmente:

```text
utils/
├── __init__.py
└── menus.py
```

O arquivo `menus.py` é responsável pela apresentação das opções disponíveis ao usuário.

---

## Relatórios

A pasta responsável pela parte administrativa contém a validação necessária para liberar o acesso aos relatórios.

```text
relatorios/
├── __init__.py
└── validacao.py
```

O fluxo dos relatórios é:

```text
main.py
   ↓
validacao.py
   ↓
menus
   ↓
relatorios_repository
   ↓
PostgreSQL
```

---

## API

O projeto também possui uma camada separada para a API REST:

```text
api/
├── __init__.py
└── app.py
```

A API foi desenvolvida com **FastAPI** nas versões anteriores.

A sua refatoração para utilizar integralmente a nova arquitetura de `services` e `repositories` está planejada para a versão **5.0**.

---

# 📁 Estrutura atual

A estrutura da versão 4.0 está organizada da seguinte forma:

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
├── repositories/
│   ├── __init__.py
│   ├── cliente_repository.py
│   ├── conta_repository.py
│   └── relatorios_repository.py
│
├── services/
│   ├── __init__.py
│   ├── cliente_service.py
│   └── conta_service.py
│
├── utils/
│   ├── __init__.py
│   └── menus.py
│
├── .env
├── .gitignore
├── cliente.py
├── conta.py
├── main.py
├── README.md
└── requirements.txt
```

---

# 🧭 Organização dos menus

A aplicação possui um menu principal dividido em diferentes áreas:

```text
MENU PRINCIPAL
│
├── Clientes
├── Contas
├── Operações Bancárias
├── Relatórios
└── Sair
```

Cada área possui seu próprio submenu.

O `main.py` é responsável pelo controle do fluxo entre os menus.

O arquivo:

```text
utils/menus.py
```

fica responsável apenas pela apresentação e leitura das opções.

---

# 🧠 Conceitos de SQL utilizados

Durante o desenvolvimento foram utilizados recursos como:

```sql
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

Também são trabalhados conceitos como:

* Chaves primárias;
* Chaves estrangeiras;
* Integridade referencial;
* Relacionamentos;
* Consultas;
* Atualizações;
* Transações;
* `COMMIT`;
* `ROLLBACK`.

---

# 🔐 Segurança

A versão 4.0 trouxe melhorias relacionadas à proteção de informações sensíveis.

Entre elas:

* Remoção das credenciais PostgreSQL do código;
* Uso de `.env`;
* Uso de `python-dotenv`;
* Proteção do `.env` através do `.gitignore`;
* Validação de acesso aos relatórios;
* Limite de tentativas para autenticação.

---

# 🌐 API REST

O Projeto Banco possui uma API REST criada com:

* FastAPI;
* Pydantic;
* Uvicorn.

A API continua presente na versão 4.0, porém não fez parte da grande refatoração arquitetural desta versão.

A atualização da API para utilizar a nova estrutura será realizada na:

```text
Versão 5.0
```

Entre as mudanças previstas estão:

* Integração dos endpoints com os services;
* Melhor tratamento das respostas HTTP;
* Organização dos endpoints;
* Atualização dos modelos Pydantic;
* Tratamento de exceções;
* Documentação da API;
* Remoção de dependências da arquitetura antiga.

---

# 🛠️ Tecnologias utilizadas

| Tecnologia    | Utilização                        |
| ------------- | --------------------------------- |
| Python        | Linguagem principal               |
| PostgreSQL    | Banco de dados                    |
| SQL           | Consultas e manipulação dos dados |
| Psycopg       | Comunicação com PostgreSQL        |
| python-dotenv | Variáveis de ambiente             |
| FastAPI       | Desenvolvimento da API REST       |
| Pydantic      | Modelagem e validação de dados    |
| Uvicorn       | Servidor ASGI                     |
| Git           | Controle de versão                |
| GitHub        | Hospedagem do repositório         |

---

# 📦 Dependências

As dependências utilizadas pelo projeto estão registradas no arquivo:

```text
requirements.txt
```

Entre as principais estão:

```text
fastapi
uvicorn
pydantic
psycopg
python-dotenv
```

Para instalar as dependências:

```bash
pip install -r requirements.txt
```

---

# 🚀 Como executar

## 1. Clone o projeto

```bash
git clone <URL_DO_REPOSITORIO>
```

Entre no diretório:

```bash
cd Projeto_Banco
```

---

## 2. Crie um ambiente virtual

### Windows

```bash
python -m venv .venv
```

Ative:

```bash
.venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 4. Configure o PostgreSQL

Crie o banco utilizado pelo projeto.

Depois execute:

```text
database/schema.sql
```

para criar as tabelas necessárias.

---

## 5. Configure o `.env`

Crie um arquivo `.env` na raiz do projeto:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=projeto_banco
DB_USER=postgres
DB_PASSWORD=sua_senha

RELATORIOS_PASSWORD=sua_senha
```

---

## 6. Execute a aplicação

```bash
python main.py
```

---

# 📚 Evolução do projeto

O Projeto Banco vem sendo desenvolvido através de diferentes versões, com cada etapa representando novos conceitos e melhorias.

## Versões iniciais

As primeiras versões tiveram como foco:

* Fundamentos de Python;
* Operações bancárias;
* Persistência;
* SQLite;
* SQL;
* Relatórios;
* API REST.

---

## Versão 3.0

A versão 3.0 marcou a migração do banco:

```text
SQLite
   ↓
PostgreSQL
```

Essa mudança permitiu trabalhar com um sistema de banco de dados mais próximo dos utilizados em aplicações reais.

---

## Versão 4.0

A versão 4.0 foi focada principalmente em **arquitetura, organização e segurança**.

A aplicação passou de uma estrutura mais centralizada para:

```text
main.py
   ↓
services
   ↓
repositories
   ↓
PostgreSQL
```

Entre as mudanças realizadas estão:

* Criação dos repositories;
* Criação dos services;
* Refatoração do `main.py`;
* Refatoração dos menus;
* Reorganização das operações bancárias;
* Uso de transações;
* Uso de `commit` e `rollback`;
* Variáveis de ambiente;
* `.gitignore`;
* `requirements.txt`;
* Melhor separação de responsabilidades.

---

# 🔄 Próximos passos — Versão 5.0

A próxima etapa do projeto será focada na **API REST**.

A versão 5.0 deverá trazer:

* Refatoração da FastAPI;
* Integração da API com os services;
* Melhor organização dos endpoints;
* Tratamento de erros HTTP;
* Melhorias nos modelos Pydantic;
* Documentação dos endpoints;
* Adaptação completa da API à arquitetura atual.

---

# 📌 Status do projeto

**Versão atual: 4.0**

A versão 4.0 possui:

* PostgreSQL;
* Repositories;
* Services;
* Gerenciamento de clientes;
* Gerenciamento de contas;
* Depósitos;
* Saques;
* Transferências;
* Transações com `commit` e `rollback`;
* Relatórios administrativos;
* Validação de acesso;
* Menus reorganizados;
* `main.py` refatorado;
* Variáveis de ambiente;
* `.gitignore`;
* `requirements.txt`;
* API REST criada em versões anteriores.

---

# 📖 Finalidade

Este projeto foi desenvolvido para fins de **estudo e prática de desenvolvimento de software**.

A proposta é acompanhar a evolução de uma aplicação Python desde estruturas mais simples até uma organização com banco de dados relacional, separação de responsabilidades, segurança de configurações, arquitetura em camadas e desenvolvimento de APIs REST.
