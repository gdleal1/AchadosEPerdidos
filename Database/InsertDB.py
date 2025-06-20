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
    
INSERT INTO denouncesImages (path, codd) VALUES
    ('images/denounce_spam.jpg', 1),
    ('images/denounce_offense.jpg', 2),
    ('images/denounce_inappropriate_content.jpg', 3),
    ('images/denounce_abuse.jpg', 4),
    ('images/denounce_fake_profile.jpg', 5),
    ('images/denounce_evidence1.png', 1),
    ('images/denounce_evidence2.png', 2),
    ('images/denounce_chatlog.jpg', 2),
    ('images/denounce_screenshot.png', 3);


INSERT INTO categories (codc, name) VALUES
    (1, 'Vestuário'),
    (2, 'Eletrônicos'),
    (3, 'Documentos'),
    (4, 'Acessórios'),
    (5, 'Materiais escolares'),
    (6, 'Chaves');

INSERT INTO foundItems (codu, date, codc, description, local, status, owner, endDate) VALUES
    (1, 20240301, 1, 'Jaqueta preta encontrada', 'Praça Central', 'ativo', 2, NULL),
    (2, 20240302, 2, 'Celular Samsung no mercado', 'Rua das Flores', 'ativo', 1, NULL),
    (3, 20240303, 3, 'Carteira com documentos', 'Terminal Rodoviário', 'ativo', 4, NULL),
    (4, 20240304, 4, 'Relógio dourado', 'Shopping Center', 'finalizado', 5, 20240320),
    (5, 20240305, 5, 'Estojo com canetas', 'Biblioteca Municipal', 'ativo', 6, NULL),
    (1, 20240306, 1, 'Blusa vermelha', 'Academia Central', 'ativo', 7, NULL),
    (2, 20240307, 2, 'Notebook Dell', 'Café do Ponto', 'ativo', 8, NULL),
    (3, 20240308, 3, 'RG em nome de Ana', 'Praia Grande', 'ativo', 9, NULL),
    (4, 20240309, 4, 'Bolsa feminina', 'Estação Norte', 'ativo', 10, NULL),
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

INSERT INTO foundItemsImages (path, code) VALUES
    ('imagens/jaqueta.jpg', 1),
    ('imagens/celular.jpg', 2),
    ('imagens/carteira.jpg', 3),
    ('imagens/relogio.jpg', 4),
    ('imagens/estojo.jpg', 5),
    ('imagens/blusa.jpg', 6),
    ('imagens/notebook.jpg', 7),
    ('imagens/rg.jpg', 8),
    ('imagens/bolsa.jpg', 9),
    ('imagens/chave.jpg', 10);

INSERT INTO wantedItems (codu, date, codc, description, local, financialReward, status, symbolicReward, finder, endDate) VALUES
    (2, 20240201, 1, 'Perdi jaqueta preta', 'Praça Central', 50, 'ativo', NULL, 1, NULL),
    (1, 20240202, 2, 'Procuro celular Samsung', 'Rua das Flores', 100, 'ativo', 'Agradecimento', 2, NULL),
    (3, 20240203, 3, 'Carteira com documentos', 'Rodoviária', 0, 'ativo', 'Gratidão', 4, NULL),
    (4, 20240204, 4, 'Relógio de ouro', 'Shopping Center', 200, 'finalizado', NULL, 5, 20240330),
    (5, 20240205, 5, 'Estojo escolar', 'Biblioteca', 20, 'ativo', NULL, 6, NULL),
    (6, 20240206, 1, 'Blusa vermelha perdida', 'Academia Central', 30, 'ativo', 'Mimo', 7, NULL),
    (7, 20240207, 2, 'Notebook Dell Inspiron', 'Café do Ponto', 500, 'ativo', NULL, 8, NULL),
    (8, 20240208, 3, 'Documentos RG Ana', 'Praia Grande', 0, 'ativo', 'Agradecimento público', 9, NULL),
    (9, 20240209, 4, 'Bolsa feminina azul', 'Estação Norte', 150, 'ativo', NULL, 10, NULL),
    (10, 20240210, 6, 'Chave de carro HB20', 'Estacionamento A', 70, 'finalizado', NULL, 1, 20240405);

INSERT INTO wantedItemsKeywords (searchTerm, codp) VALUES
    ('jaqueta', 1),
    ('celular', 2),
    ('carteira', 3),
    ('relógio', 4),
    ('estojo', 5),
    ('blusa', 6),
    ('notebook', 7),
    ('documentos', 8),
    ('bolsa', 9),
    ('chave', 10);

INSERT INTO wantedItemsImages (path, codp) VALUES
    ('imagens/procura_jaqueta.jpg', 1),
    ('imagens/procura_celular.jpg', 2),
    ('imagens/procura_carteira.jpg', 3),
    ('imagens/procura_relogio.jpg', 4),
    ('imagens/procura_estojo.jpg', 5),
    ('imagens/procura_blusa.jpg', 6),
    ('imagens/procura_notebook.jpg', 7),
    ('imagens/procura_rg.jpg', 8),
    ('imagens/procura_bolsa.jpg', 9),
    ('imagens/procura_chave.jpg', 10);
""")

conn.commit()
conn.close()