import sqlite3

conn = sqlite3.connect("AchadosEPerdidos/AchadosEPerdidos.db")
cursor = conn.cursor()

# Create a sample table
cursor.executescript("""
CREATE TABLE usuarios (
    codu INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    telefone INTEGER UNIQUE NOT NULL, 
    senha TEXT NOT NULL,
    nota_media INTEGER NOT NULL,
    quantidade_notas INTEGER NOT NULL,
    cargo TEXT NOT NULL
);
               
CREATE TABLE mensagens (
    codm INTEGER PRIMARY KEY AUTOINCREMENT,
    conteudo TEXT NOT NULL,
    remetente INTEGER NOT NULL,
    destinatario INTEGER NOT NULL,
    data INTEGER NOT NULL,
    FOREIGN KEY (remetente) REFERENCES usuarios(codu),
    FOREIGN KEY (destinatario) REFERENCES usuarios(codu)
);
               
CREATE TABLE denuncias (
    codd INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL,
    denunciador INTEGER NOT NULL,
    denunciado INTEGER NOT NULL,
    FOREIGN KEY (denunciador) REFERENCES usuarios(codu),
    FOREIGN KEY (denunciado) REFERENCES usuarios(codu)
);
               
CREATE TABLE categorias (
    codc INTEGER PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE
);

CREATE TABLE itensEncontrados (
    code INTEGER PRIMARY KEY AUTOINCREMENT,
    codu INTEGER NOT NULL,
    data INTEGER NOT NULL,
    codc INTEGER NOT NULL,
    descricao TEXT NOT NULL,
    local TEXT NOT NULL,
    FOREIGN KEY (codu) REFERENCES usuarios(codu),
    FOREIGN KEY (codc) REFERENCES categorias(codc)
);  
               
CREATE TABLE palavrasChaveItensEncontrados(
    codpce INTEGER PRIMARY KEY AUTOINCREMENT,
    termo TEXT NOT NULL,
    code INTEGER NOT NULL,
    FOREIGN KEY (code) REFERENCES itensEncontrados(code)
);
               
CREATE TABLE imagensItensEncontrados(
    codie INTEGER PRIMARY KEY AUTOINCREMENT,
    path TEXT NOT NULL,
    code INTEGER NOT NULL,
    FOREIGN KEY (code) REFERENCES itensEncontrados(code)
);

CREATE TABLE itensProcurados (
    codp INTEGER PRIMARY KEY AUTOINCREMENT,
    codu INTEGER NOT NULL,
    data INTEGER NOT NULL,
    codc INTEGER NOT NULL,
    descricao TEXT NOT NULL,
    local TEXT NOT NULL,
    recompensaFinanceira INTEGER NOT NULL,
    recompensaSimbolica TEXT,
    FOREIGN KEY (codu) REFERENCES usuarios(codu),
    FOREIGN KEY (codc) REFERENCES categorias(codc)
);  
               
CREATE TABLE palavrasChaveItensProcurados(
    codpce INTEGER PRIMARY KEY AUTOINCREMENT,
    termo TEXT NOT NULL,
    codp INTEGER NOT NULL,
    FOREIGN KEY (codp) REFERENCES itensProcurados(codp)
);
               
CREATE TABLE imagensItensProcurados(
    codie INTEGER PRIMARY KEY AUTOINCREMENT,
    path TEXT NOT NULL,
    codp INTEGER NOT NULL,
    FOREIGN KEY (codp) REFERENCES itensProcurados(codp)
);  

CREATE TABLE anuncios (
    coda INTEGER PRIMARY KEY AUTOINCREMENT,
    dataInicio INTEGER NOT NULL,
    status TEXT NOT NULL,
    code INTEGER NOT NULL,
    encontrou INTEGER NOT NULL,
    dono INTEGER,
    dataFim INTEGER,
    FOREIGN KEY (code) REFERENCES itensEncontrados(code),
    FOREIGN KEY (encontrou) REFERENCES usuarios(codu),   
    FOREIGN KEY (dono) REFERENCES usuarios(codu)         
);

CREATE TABLE solicitacoes (
    cods INTEGER PRIMARY KEY AUTOINCREMENT,
    dataInicio INTEGER NOT NULL,
    status TEXT NOT NULL,
    codp INTEGER NOT NULL,
    dono INTEGER NOT NULL,
    encontrou INTEGER,
    dataFim INTEGER,
    FOREIGN KEY (codp) REFERENCES itensProcurados(codp),
    FOREIGN KEY (encontrou) REFERENCES usuarios(codu),   
    FOREIGN KEY (dono) REFERENCES usuarios(codu)       
);                                
""")

conn.commit()
conn.close()

conn = sqlite3.connect("AchadosEPerdidos/AchadosEPerdidos.db")
cursor = conn.cursor()

cursor.executescript("""
INSERT INTO categorias(codc, nome)
VALUES
    (1, 'Roupas'),
    (2, 'Eletrônicos'),
    (3, 'Documentos pessoais'),
    (4, 'Acessórios e itens pessoais'),
    (5, 'Materiais de escritório'),
    (6, 'Outros');
    
INSERT INTO usuarios (nome, email, telefone, senha, nota_media, quantidade_notas, cargo) 
VALUES
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

INSERT INTO mensagens (conteudo, remetente, destinatario, data) 
VALUES
    ('Oi, encontrei seu item.', 1, 2, 20240101),
    ('Ainda está procurando?', 2, 1, 20240102),
    ('Vi seu anúncio.', 3, 1, 20240103),
    ('Pode me enviar mais informações?', 4, 5, 20240104),
    ('Qual a recompensa?', 6, 7, 20240105),
    ('Posso entregar amanhã.', 8, 9, 20240106),
    ('Vamos marcar um encontro?', 9, 10, 20240107),
    ('Tenho algo parecido.', 5, 3, 20240108),
    ('Parece que encontrei!', 7, 2, 20240109),
    ('Podemos conversar?', 10, 1, 20240110);

INSERT INTO denuncias (descricao, denunciador, denunciado) 
VALUES
    ('Spam frequente', 1, 3),
    ('Ofensa nas mensagens', 2, 4),
    ('Conteúdo inapropriado', 5, 6),
    ('Abuso de sistema', 7, 8),
    ('Perfil falso', 9, 10);

INSERT INTO itensEncontrados (codu, data, codc, descricao, local) 
VALUES
    (1, 20240301, 1, 'Jaqueta preta encontrada', 'Praça Central'),
    (2, 20240302, 2, 'Celular Samsung no mercado', 'Rua das Flores'),
    (3, 20240303, 3, 'Carteira com documentos', 'Terminal Rodoviário'),
    (4, 20240304, 4, 'Relógio dourado', 'Shopping Center'),
    (5, 20240305, 5, 'Estojo com canetas', 'Biblioteca Municipal'),
    (6, 20240306, 1, 'Blusa vermelha', 'Academia Central'),
    (7, 20240307, 2, 'Notebook Dell', 'Café do Ponto'),
    (8, 20240308, 3, 'RG em nome de Ana', 'Praia Grande'),
    (9, 20240309, 4, 'Bolsa feminina', 'Estação Norte'),
    (10, 20240310, 6, 'Chave de carro', 'Estacionamento A');

INSERT INTO palavrasChaveItensEncontrados (termo, code) 
VALUES
    ('jaqueta', 1), ('preta', 1),
    ('celular', 2), ('samsung', 2),
    ('carteira', 3),
    ('relógio', 4),
    ('estojo', 5),
    ('blusa', 6),
    ('notebook', 7),
    ('chave', 10);

INSERT INTO imagensItensEncontrados (path, code) 
VALUES
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

INSERT INTO itensProcurados (codu, data, codc, descricao, local, recompensaFinanceira, recompensaSimbolica) 
VALUES
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

INSERT INTO palavrasChaveItensProcurados (termo, codp) 
VALUES
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

INSERT INTO imagensItensProcurados (path, codp) 
VALUES
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

INSERT INTO anuncios (dataInicio, status, code, encontrou, dono, dataFim) 
VALUES
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

INSERT INTO solicitacoes (dataInicio, status, codp, dono, encontrou, dataFim) 
VALUES
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