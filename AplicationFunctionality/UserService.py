import sqlite3

class UserService:
    def __init__(self, db_path):
        self.db_path = db_path

    def get_user_info(self, codu:int) -> dict:
        """
        Retrieve user information based on user ID.
        
        Returns:
            dict: User information as a dictionary
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        query = "SELECT * FROM users WHERE codu = ?"
        cursor.execute(query, (codu,))
        
        row = cursor.fetchone()
        
        if row:
            columns = [column[0] for column in cursor.description]
            user_info = dict(zip(columns, row))
        else:
            user_info = {}
        
        conn.close()
        return user_info

    def verify_login(self, username:str, password:str) -> bool:
        """
        Verify user login credentials.
            
        Returns:
            bool: True if credentials are valid, False otherwise
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        query = "SELECT * FROM users WHERE name = ? AND password = ? AND role != 'banned'"
        cursor.execute(query, (username, password))
        
        result = cursor.fetchone()
        
        conn.close()
        return result is not None
    
    def insert_new_user(self, 
                        username:str, 
                        email:str,
                        cellphone:str,
                        password:str,) -> bool:
        
        """
        Insert a new user into the database.
        
        Returns:
        bool: True if user was successfully inserted, False if username already exists
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        try:
            query = """
            INSERT INTO users (name, email, cellphone, password, average_rating, rating_count, role)
            VALUES (?, ?, ?, ?, 0, 0, 'comum')
            """
            cursor.execute(query, (username, email, cellphone, password))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            print("Username already exists.")
            return False
        finally:
            conn.close()

    def ban_user(self, codu:int) -> bool:
        """
        Ban a user by setting their role to 'banned'.
        
        Returns:
            bool: True if the user was successfully banned, False if the user does not exist
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        query = "UPDATE users SET role = 'banned' WHERE codu = ?"
        cursor.execute(query, (codu,))
        
        if cursor.rowcount == 0:
            conn.close()
            return False
        
        conn.commit()
        conn.close()
        return True

# This code defines a UserService class that provides methods to interact with user data in a SQLite database
#Example usage:
if __name__ == "__main__":
    #Unitary tests
    db_path = "Database/AchadosEPerdidos.db"
    user_service = UserService(db_path)

    # Test get_user_info
    user_info = user_service.get_user_info(1)
    print("User Info:", user_info) #expect 'codu': 1, 'name': 'Ana Silva' ...'

    # Test verify_login
    is_valid = user_service.verify_login("Ana Silva", "senha123")
    print("Login Valid:", is_valid) #expect true

    # Test insert_new_user
    new_user_result = user_service.insert_new_user("Novo Usuario", "ana@email.com", "123456789", "senha123")
    print("New User Created:", new_user_result) #expect false
