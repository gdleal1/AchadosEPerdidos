import sqlite3
from datetime import datetime, timedelta

class ItemSearch:
    def __init__(self, db_path):
        self.db_path = db_path
    
    def search_item(self, 
                    item_name:str=None, 
                    category:str=None, 
                    local:str=None, 
                    date:str=None):
        """
        Search for items in the database based on the given criteria.
        If a date is provided, searches for items found within 7 days after that date.
        
        Returns:
            list: List of matching items as dictionaries
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Base query
        query = """
        SELECT ie.code, ie.description, c.name as category, ie.local, ie.date
        FROM foundItems ie
        JOIN categories c ON ie.codc = c.codc
        WHERE 1=1
        """
        
        params = []
        
        # Add conditions based on provided parameters
        if item_name:
            query += " AND ie.description LIKE ?"
            params.append(f"%{item_name}%")
        
        if category:
            query += " AND c.name = ?"
            params.append(category)
        
        if local:
            query += " AND ie.local LIKE ?"
            params.append(f"%{local}%")
        
        if date:
            # Convert input date (YYYYMMDD) to datetime and calculate end date (7 days later)
            try:
                input_date = datetime.strptime(str(date), "%d/%m/%Y")
                start_date = input_date.date()  # Get date object without time
                end_date = (input_date + timedelta(days=7)).date()

                # Format both dates consistently (either as strings or integers)
                query += " AND ie.date BETWEEN ? AND ?"
                params.extend([
                    start_date.strftime("%Y%m%d"),  # or int(start_date.strftime("%Y%m%d"))
                    end_date.strftime("%Y%m%d")     # must match the type of first parameter
                ])
            except ValueError:
                print("Invalid date format. Please use YYYYMMDD format.")
                return []
        
        # Execute query
        cursor.execute(query, params)
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        conn.close()
        return results

    def get_item_image_paths(self, item_code:int) -> list:
        """
        Retrieve image paths for a specific item based on its code.
        
        Returns:
            list: List of image paths
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        query = "SELECT path FROM foundItemsImages WHERE code = ?"
        cursor.execute(query, (item_code,))
        
        image_paths = [row[0] for row in cursor.fetchall()]
        
        conn.close()
        return image_paths

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
        
        query = "SELECT * FROM users WHERE name = ? AND password = ?"
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
            INSERT INTO usuarios (name, email, cellphone, password, average_rating, rating_count, role)
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

#Example usage:
if __name__ == "__main__":
    #check verify login
    db_path = "Database/AchadosEPerdidos.db"
    item_search = ItemSearch(db_path)

    codu = 1
    code = 1

    print(item_search.get_user_info(codu))
    print(item_search.get_item_image_paths(code))
    

