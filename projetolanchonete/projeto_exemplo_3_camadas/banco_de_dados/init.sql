DROP DATABASE IF EXISTS lanchonete;

CREATE DATABASE lanchonete;

USE lanchonete;

-- ==========================
-- TABELA USUÁRIOS
-- ==========================

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    login VARCHAR(50) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL,
    cargo VARCHAR(30) NOT NULL,
    ativo BOOLEAN NOT NULL DEFAULT TRUE
);

-- ==========================
-- TABELA PRODUTOS
-- ==========================

CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10,2) NOT NULL
);

-- ==========================
-- TABELA MESAS
-- ==========================

CREATE TABLE mesas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero INT NOT NULL UNIQUE
);

-- ==========================
-- TABELA PEDIDOS
-- ==========================

CREATE TABLE pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mesa_id INT NOT NULL,
    status VARCHAR(30) NOT NULL,

    CONSTRAINT fk_pedido_mesa
        FOREIGN KEY (mesa_id)
        REFERENCES mesas(id)
);

-- ==========================
-- TABELA ITENS DO PEDIDO
-- ==========================

CREATE TABLE itens_pedido (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pedido_id INT NOT NULL,
    produto_id INT NOT NULL,
    quantidade INT NOT NULL,

    CONSTRAINT fk_item_pedido
        FOREIGN KEY (pedido_id)
        REFERENCES pedidos(id),

    CONSTRAINT fk_item_produto
        FOREIGN KEY (produto_id)
        REFERENCES produtos(id)
);

-- ==========================
-- TABELA PAGAMENTOS
-- ==========================

CREATE TABLE pagamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pedido_id INT NOT NULL,
    valor DECIMAL(10,2) NOT NULL,

    CONSTRAINT fk_pagamento_pedido
        FOREIGN KEY (pedido_id)
        REFERENCES pedidos(id)
);
