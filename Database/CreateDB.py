import sqlite3

conn = sqlite3.connect("Database/AchadosEPerdidos.db")
cursor = conn.cursor()

# Create a sample table
cursor.executescript("""
CREATE TABLE users (
    codu INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    cellphone INTEGER UNIQUE NOT NULL, 
    password TEXT NOT NULL,
    role TEXT NOT NULL
);
               
CREATE TABLE denounces (
    codd INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    denouncer INTEGER NOT NULL,
    denounced INTEGER NOT NULL,
    FOREIGN KEY (denouncer) REFERENCES users(codu),
    FOREIGN KEY (denounced) REFERENCES users(codu)
);
               
CREATE TABLE categories (
    codc INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE foundItems (
    code INTEGER PRIMARY KEY AUTOINCREMENT,
    codu INTEGER NOT NULL,
    date INTEGER NOT NULL,
    codc INTEGER NOT NULL,
    description TEXT NOT NULL,
    local TEXT NOT NULL,
    status TEXT NOT NULL,
    completeDescription TEXT NOT NULL,
    owner INTEGER,
    endDate INTEGER, 
    FOREIGN KEY (codu) REFERENCES users(codu),
    FOREIGN KEY (codc) REFERENCES categories(codc),
    FOREIGN KEY (owner) REFERENCES users(codu)
);  
               
CREATE TABLE foundItemsKeywords(
    codpce INTEGER PRIMARY KEY AUTOINCREMENT,
    searchTerm TEXT NOT NULL,
    code INTEGER NOT NULL,
    FOREIGN KEY (code) REFERENCES foundItems(code)
);                           
""")

conn.commit()
conn.close()