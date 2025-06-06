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

INSERT INTO foundItems (codu, date, codc, description, local) VALUES
    (1, 20240301, 1, 'Jaqueta preta encontrada', 'Praça Central'),
    (2, 20240302, 2, 'Celular Samsung no mercado', 'Rua das Flores'),
    (3, 20240303, 3, 'Carteira com documentos', 'Terminal Rodoviário'),
    (4, 20240304, 4, 'Relógio dourado', 'Shopping Center'),
    (5, 20240305, 5, 'Estojo com canetas', 'Biblioteca Municipal'),
    (1, 20240306, 1, 'Blusa vermelha', 'Academia Central'),
    (2, 20240307, 2, 'Notebook Dell', 'Café do Ponto'),
    (3, 20240308, 3, 'RG em nome de Ana', 'Praia Grande'),
    (4, 20240309, 4, 'Bolsa feminina', 'Estação Norte'),
    (6, 20240310, 6, 'Chave de carro', 'Estacionamento A');

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

INSERT INTO wantedItems (codu, date, codc, description, local, financialReward, symbolicReward) VALUES
    (2, 20240201, 1, 'Perdi jaqueta preta', 'Praça Central', 50, NULL),
    (1, 20240202, 2, 'Procuro celular Samsung', 'Rua das Flores', 100, 'Agradecimento'),
    (3, 20240203, 3, 'Carteira com documentos', 'Rodoviária', 0, 'Gratidão'),
    (4, 20240204, 4, 'Relógio de ouro', 'Shopping Center', 200, NULL),
    (5, 20240205, 5, 'Estojo escolar', 'Biblioteca', 20, NULL),
    (6, 20240206, 1, 'Blusa vermelha perdida', 'Academia Central', 30, 'Mimo'),
    (7, 20240207, 2, 'Notebook Dell Inspiron', 'Café do Ponto', 500, NULL),
    (8, 20240208, 3, 'Documentos RG Ana', 'Praia Grande', 0, 'Agradecimento público'),
    (9, 20240209, 4, 'Bolsa feminina azul', 'Estação Norte', 150, NULL),
    (10, 20240210, 6, 'Chave de carro HB20', 'Estacionamento A', 70, NULL);

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

INSERT INTO announcements (startDate, status, code, finder, owner, endDate) VALUES
    (20240311, 'ativo', 1, 1, 2, NULL),
    (20240312, 'ativo', 2, 2, 1, NULL),
    (20240313, 'ativo', 3, 3, 4, NULL),
    (20240314, 'finalizado', 4, 4, 5, 20240320),
    (20240315, 'ativo', 5, 5, 6, NULL),
    (20240316, 'ativo', 6, 6, 7, NULL),
    (20240317, 'ativo', 7, 7, 8, NULL),
    (20240318, 'ativo', 8, 8, 9, NULL),
    (20240319, 'ativo', 9, 9, 10, NULL),
    (20240320, 'finalizado', 10, 10, 1, 20240401);

INSERT INTO requests (startDate, status, codp, owner, finder, endDate) VALUES
    (20240321, 'ativo', 1, 2, 1, NULL),
    (20240322, 'ativo', 2, 1, 2, NULL),
    (20240323, 'ativo', 3, 3, 4, NULL),
    (20240324, 'finalizado', 4, 4, 5, 20240330),
    (20240325, 'ativo', 5, 5, 6, NULL),
    (20240326, 'ativo', 6, 6, 7, NULL),
    (20240327, 'ativo', 7, 7, 8, NULL),
    (20240328, 'ativo', 8, 8, 9, NULL),
    (20240329, 'ativo', 9, 9, 10, NULL),
    (20240330, 'finalizado', 10, 10, 1, 20240405);
""")

conn.commit()
conn.close()