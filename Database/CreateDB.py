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
    average_rating INTEGER NOT NULL,
    rating_count INTEGER NOT NULL,
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

CREATE TABLE denouncesImages (
    coddi INTEGER PRIMARY KEY AUTOINCREMENT,
    path TEXT NOT NULL,
    codd INTEGER NOT NULL,
    FOREIGN KEY (codd) REFERENCES denounces(codd)
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
    FOREIGN KEY (codu) REFERENCES users(codu),
    FOREIGN KEY (codc) REFERENCES categories(codc)
);  
               
CREATE TABLE foundItemsKeywords(
    codpce INTEGER PRIMARY KEY AUTOINCREMENT,
    searchTerm TEXT NOT NULL,
    code INTEGER NOT NULL,
    FOREIGN KEY (code) REFERENCES foundItems(code)
);
               
CREATE TABLE foundItemsImages(
    codie INTEGER PRIMARY KEY AUTOINCREMENT,
    path TEXT NOT NULL,
    code INTEGER NOT NULL,
    FOREIGN KEY (code) REFERENCES foundItems(code)
);

CREATE TABLE wantedItems (
    codp INTEGER PRIMARY KEY AUTOINCREMENT,
    codu INTEGER NOT NULL,
    date INTEGER NOT NULL,
    codc INTEGER NOT NULL,
    description TEXT NOT NULL,
    local TEXT NOT NULL,
    financialReward INTEGER NOT NULL,
    symbolicReward TEXT,
    FOREIGN KEY (codu) REFERENCES users(codu),
    FOREIGN KEY (codc) REFERENCES categories(codc)
);  
               
CREATE TABLE wantedItemsKeywords(
    codpce INTEGER PRIMARY KEY AUTOINCREMENT,
    searchTerm TEXT NOT NULL,
    codp INTEGER NOT NULL,
    FOREIGN KEY (codp) REFERENCES wantedItems(codp)
);
               
CREATE TABLE wantedItemsImages(
    codie INTEGER PRIMARY KEY AUTOINCREMENT,
    path TEXT NOT NULL,
    codp INTEGER NOT NULL,
    FOREIGN KEY (codp) REFERENCES wantedItems(codp)
);  

CREATE TABLE announcements (
    coda INTEGER PRIMARY KEY AUTOINCREMENT,
    startDate INTEGER NOT NULL,
    status TEXT NOT NULL,
    code INTEGER NOT NULL,
    finder INTEGER NOT NULL,
    owner INTEGER,
    endDate INTEGER,
    FOREIGN KEY (code) REFERENCES foundItems(code),
    FOREIGN KEY (finder) REFERENCES users(codu),   
    FOREIGN KEY (owner) REFERENCES users(codu)         
);

CREATE TABLE requests (
    cods INTEGER PRIMARY KEY AUTOINCREMENT,
    startDate INTEGER NOT NULL,
    status TEXT NOT NULL,
    codp INTEGER NOT NULL,
    owner INTEGER NOT NULL,
    finder INTEGER,
    endDate INTEGER,
    FOREIGN KEY (codp) REFERENCES wantedItems(codp),
    FOREIGN KEY (finder) REFERENCES users(codu),   
    FOREIGN KEY (owner) REFERENCES users(codu)       
);                                
""")

conn.commit()
conn.close()