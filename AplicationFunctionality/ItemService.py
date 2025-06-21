import sqlite3
from datetime import datetime, timedelta

class ItemService:
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

#Example usage:
if __name__ == "__main__":
    #Unitary rudimentary tests
    db_path = "Database/AchadosEPerdidos.db"
    item_search = ItemService(db_path)

    #search for items method
    results = item_search.search_item(item_name="jaqueta", category="Vestuário", local="Praça Central", date="01/03/2024")
    for item in results:
        print(f"Code: {item['code']}, Description: {item['description']}, Category: {item['category']}, Local: {item['local']}, Date: {item['date']}")
    
    

