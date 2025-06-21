import sqlite3

conn = sqlite3.connect("Database/AchadosEPerdidos.db")
cursor = conn.cursor()

cursor.executescript("""
INSERT INTO users (name, email, cellphone, password, average_rating, rating_count, role) VALUES
    ('Ana Silva', 'ana@email.com', 111111111, 'senha123', 5, 10, 'comum'),
    ('Bruno Costa', 'bruno@email.com', 222222222, 'senha456', 4, 8, 'comum'),
    ('Carlos Lima', 'carlos@email.com', 333333333, 'senha789', 3, 6, 'moderador'),
    ('Daniela Rocha', 'daniela@email.com', 444444444, 'senha1010', 5, 12, 'comum'),
    ('Eduardo Fonseca', 'eduardo@email.com', 555555555, 'senha1111', 4, 7, 'comum'),
    ('Fernanda Alves', 'fernanda@email.com', 666666666, 'senha1212', 5, 9, 'comum'),
    ('Gustavo Mello', 'gustavo@email.com', 777777777, 'senha1313', 2, 3, 'comum'),
    ('Helena Dias', 'helena@email.com', 888888888, 'senha1414', 4, 6, 'moderador'),
    ('Igor Martins', 'igor@email.com', 999999999, 'senha1515', 3, 5, 'comum'),
    ('Julia Teixeira', 'julia@email.com', 1010101010, 'senha1616', 5, 10, 'comum');

INSERT INTO denounces (title, description, denouncer, denounced) VALUES
    ('Spam frequente', 'Spam frequente', 1, 3),
    ('Ofensa nas mensagens', 'Ofensa nas mensagens', 2, 4),
    ('Conteúdo inapropriado', 'Conteúdo inapropriado', 5, 6),
    ('Abuso de sistema', 'Abuso de sistema', 7, 8),
    ('Perfil falso', 'Perfil falso', 9, 10);

INSERT INTO categories (codc, name) VALUES
    (1, 'Vestuário'),
    (2, 'Eletrônicos'),
    (3, 'Documentos'),
    (4, 'Acessórios'),
    (5, 'Materiais escolares'),
    (6, 'Chaves');

INSERT INTO foundItems (codu, date, codc, description, local, status, owner, endDate) VALUES
    (1, 20240301, 1, 'Jaqueta preta encontrada', 'Praça Central', 'ativo', NULL, NULL),
    (2, 20240302, 2, 'Celular Samsung no mercado', 'Rua das Flores', 'ativo', NULL, NULL),
    (3, 20240303, 3, 'Carteira com documentos', 'Terminal Rodoviário', 'ativo', NULL, NULL),
    (4, 20240304, 4, 'Relógio dourado', 'Shopping Center', 'finalizado', 5, 20240320),
    (5, 20240305, 5, 'Estojo com canetas', 'Biblioteca Municipal', 'ativo', NULL, NULL),
    (1, 20240306, 1, 'Blusa vermelha', 'Academia Central', 'ativo', NULL, NULL),
    (2, 20240307, 2, 'Notebook Dell', 'Café do Ponto', 'ativo', NULL, NULL),
    (3, 20240308, 3, 'RG em nome de Ana', 'Praia Grande', 'ativo', NULL, NULL),
    (4, 20240309, 4, 'Bolsa feminina', 'Estação Norte', 'ativo', NULL, NULL),
    (6, 20240310, 6, 'Chave de carro', 'Estacionamento A', 'finalizado', 1, 20240401);


INSERT INTO foundItemsKeywords (searchTerm, code) VALUES
    ('jaqueta', 1), ('preta', 1),
    ('celular', 2), ('samsung', 2),
    ('carteira', 3),
    ('relógio', 4),
    ('estojo', 5),
    ('blusa', 6),
    ('notebook', 7),
    ('chave', 10);
""")

conn.commit()
conn.close()