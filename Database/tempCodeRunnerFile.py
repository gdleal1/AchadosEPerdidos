import sqlite3

conn = sqlite3.connect("Database/AchadosEPerdidos.db")
cursor = conn.cursor()
cursor.executescript("UPDATE foundItems SET status = 'active';"
)

conn.commit()
conn.close()