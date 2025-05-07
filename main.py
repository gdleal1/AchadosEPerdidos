import sqlite3

conn = sqlite3.connect("AchadosEPerdidos.db")
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
    quantidade_notas INTEGER NOT NULL
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