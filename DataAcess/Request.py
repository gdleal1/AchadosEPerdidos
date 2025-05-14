import sqlite3
from datetime import datetime, timedelta

class ItemSearch:
    def __init__(self, db_path):
        self.db_path = db_path
    
    def search_item(self, nome_item=None, categoria=None, local=None, data=None):
        """
        Search for items in the database based on the given criteria.
        If a date is provided, searches for items found within 7 days after that date.
        
        Args:
            nome_item (str): Name/description of the item (partial match)
            categoria (str): Category name (exact match)
            local (str): Location where item was found (partial match)
            data (int): Date when item was found (YYYYMMDD format)
                      Items found within 7 days after this date will be returned
            
        Returns:
            list: List of matching items as dictionaries
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Base query
        query = """
        SELECT ie.code, ie.descricao, c.nome as categoria, ie.local, ie.data
        FROM itensEncontrados ie
        JOIN categorias c ON ie.codc = c.codc
        WHERE 1=1
        """
        
        params = []
        
        # Add conditions based on provided parameters
        if nome_item:
            query += " AND ie.descricao LIKE ?"
            params.append(f"%{nome_item}%")
        
        if categoria:
            query += " AND c.nome = ?"
            params.append(categoria)
        
        if local:
            query += " AND ie.local LIKE ?"
            params.append(f"%{local}%")
        
        if data:
            # Convert input date (YYYYMMDD) to datetime and calculate end date (7 days later)
            try:
                input_date = datetime.strptime(str(data), "%d/%m/%Y")
                start_date = input_date.date()  # Get date object without time
                end_date = (input_date + timedelta(days=7)).date()

                # Format both dates consistently (either as strings or integers)
                query += " AND ie.data BETWEEN ? AND ?"
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


# Example usage:
if __name__ == "__main__":
    searcher = ItemSearch("../DB/AchadosEPerdidos.db")  # Replace with your actual DB path
    
        # Search for the black jacket found in "Praça Central" around March 2024
    results = searcher.search_item(
        nome_item="jaqueta",
        local="Praça Central",
        data="28/02/2024"
    )
    
    print("Found items:")
    for item in results:
        print(f"ID: {item['code']}")
        print(f"Description: {item['descricao']}")
        print(f"Category: {item['categoria']}")
        print(f"Location: {item['local']}")
        print(f"Date: {item['data']}")
        print("-" * 30)

    print(results)