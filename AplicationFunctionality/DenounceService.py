import sqlite3

class DenounceService:
    def __init__(self, db_path="Database/AchadosEPerdidos.db"):
        self.db_path = db_path

    def get_denounces(self) -> list:
        """
        Retrieve all denouncer users names from the database.
        
        Returns:
            list: A list of dictionaries containing denounce information
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT denounces.*, 
               denouncer_user.name AS denouncer_name, 
               denounced_user.name AS denounced_name
            FROM denounces
            JOIN users AS denouncer_user ON denounces.denouncer = denouncer_user.codu
            JOIN users AS denounced_user ON denounces.denounced = denounced_user.codu
        """)
        rows = cursor.fetchall()

        columns = [column[0] for column in cursor.description]
        denounces = [dict(zip(columns, row)) for row in rows]

        conn.close()
        return denounces

    def add_denounce(self, 
                     title: str, 
                     description: str, 
                     denouncer: int, 
                     denounced: str) -> bool:
        """
        Add a new denounce to the database.
        
        Returns:
            bool: True if the denounce was successfully added, False otherwise
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Check if denounced exists
        cursor.execute("SELECT codu FROM users WHERE email = ?", (denounced,))
        denounced_user = cursor.fetchone()

        if not denounced_user:
            print("Denounced user not found.")
            return False

        try:
            cursor.execute("""
                INSERT INTO denounces (title, description, denouncer, denounced)
                VALUES (?, ?, ?, ?)
            """, (title, description, denouncer, denounced_user[0]))
            conn.commit()
            return True
        except sqlite3.IntegrityError as e:
            print(f"Error inserting denounce: {e}")
            return False
        finally:
            conn.close()

if __name__ == "__main__":
    
    # Very rought unitary test
    service = DenounceService()
    # Show all denounces
    denounces = service.get_denounces()
    print("Existing Denounces:")
    for denounce in denounces:
        print(denounce)