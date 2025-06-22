import sqlite3
from datetime import datetime, timedelta

class ItemService:
    def __init__(self, db_path="Database/AchadosEPerdidos.db"):
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
        SELECT ie.code, ie.codu, ie.description, c.name as category, ie.local, ie.date, ie.status
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

        query += " AND ie.status = 'active'"  # Only active items
        
        query = f"""
        WITH filtered_items AS (
            {query}
        )
        SELECT fi.code, us.cellphone, fi.description, fi.category, fi.local, fi.date, fi.status
        FROM filtered_items fi
        JOIN users us ON fi.codu = us.codu
        """

        # Execute query
        cursor.execute(query, params)
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        conn.close()
        return results

    def items_found_by_user(self, codu:int):
        """
        Retrieve items found by a specific user.
        
        Returns:
            list: List of items found by the user
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        query = """
        SELECT ie.code, ie.description, c.name as category, ie.local, ie.date, ie.status
        FROM foundItems ie
        JOIN categories c ON ie.codc = c.codc
        WHERE ie.codu = ?
        """
        
        cursor.execute(query, (codu,))
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        conn.close()
        return results
    
    def mark_item_as_found(self, code:int, user_email:str):
        """
        Mark an item as found by a user.
        
        Returns:
            bool: True if the item was successfully marked as found, False otherwise
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Check if the item exists and is active
        cursor.execute("SELECT status FROM foundItems WHERE code = ? AND status = 'active'", (code,))
        item = cursor.fetchone()

        #Check if user exists
        cursor.execute("SELECT codu FROM users WHERE email = ?", (user_email,))
        user = cursor.fetchone()

        if not item or not user:
            conn.close()
            return False
        
        # Update the item's status to 'finalizado' and set the owner
        cursor.execute("""
            UPDATE foundItems 
            SET status = 'finalized', owner = ?, endDate = ?
            WHERE code = ?
        """, (user[0], datetime.now().strftime("%Y%m%d"), code))

        conn.commit()
        conn.close()
        return True
    
    def add_found_item(self, 
                     codu:int, 
                     codc:int, 
                     description:str, 
                     local:str):
        """
        Add a new found item to the database.
        
        Returns:
            bool: True if the item was successfully added, False otherwise
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        date = datetime.now().strftime("%Y%m%d")  # Get current date in YYYYMMDD format

        try:
            cursor.execute("""
                INSERT INTO foundItems (codu, date, codc, description, local, status, owner, endDate)
                VALUES (?, ?, ?, ?, ?, 'active', NULL, NULL)
            """, (codu, date, codc, description, local))
            conn.commit()
            return True
        except sqlite3.IntegrityError as e:
            print(f"Error inserting item: {e}")
            return False
        finally:
            conn.close()

    def remove_item(self, code:int):
        """
        Remove an item from the database.
        
        Returns:
            bool: True if the item was successfully removed, False otherwise
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM foundItems WHERE code = ?", (code,))
        conn.commit()
        
        if cursor.rowcount > 0:
            conn.close()
            return True
        else:
            conn.close()
            return False
        
#Example usage:
if __name__ == "__main__":
    #Unitary rudimentary tests
    item_search = ItemService()

    #search for items method
    results = item_search.search_item(item_name="jaqueta", category="Vestuário", local="Praça Central", date="01/03/2024")
    for item in results:
        print(f"Code: {item['code']}, Description: {item['description']}, Category: {item['category']}, Local: {item['local']}, Date: {item['date']}")
    
    #items found by user method
    user_items = item_search.items_found_by_user(codu=1)
    for item in user_items:
        print(f"Code: {item['code']}, Description: {item['description']}, Category: {item['category']}, Local: {item['local']}, Date: {item['date']}")

