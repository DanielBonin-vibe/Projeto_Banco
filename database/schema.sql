-- ============================================
-- Projeto Banco
-- Estrutura do banco de dados PostgreSQL
-- ============================================


-- ============================================
-- Tabela de clientes
-- ============================================

CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INTEGER NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL
);


-- ============================================
-- Tabela de contas
-- ============================================

CREATE TABLE IF NOT EXISTS contas (
    id_conta INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    cpf_titular VARCHAR(14) NOT NULL,
    saldo NUMERIC(12,2) NOT NULL DEFAULT 0.00,

    CONSTRAINT fk_contas_clientes
        FOREIGN KEY (cpf_titular)
        REFERENCES clientes(cpf)
);