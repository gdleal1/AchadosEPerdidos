import re
from typing import Optional, List, Any
from  Aplication_functionality.SQLQueryBuilder import ItemSearch  # Adjust import to your project structure

class InputVerification:
    
    def __init__(self):
        pass

    def sanitize_input(self,value: Optional[str]) -> Optional[str]:
        if value is None:
            return None
        if not isinstance(value, str):
            raise ValueError(f"Expected a string or None, got {type(value)}")

        # Basic SQL injection check — reject suspicious patterns
        pattern = re.compile(r"(--|\b(OR|AND|SELECT|INSERT|DELETE|UPDATE|DROP|;)\b)", re.IGNORECASE)
        if pattern.search(value):
            raise ValueError(f"Potentially unsafe input detected: {value}")

        return value.strip()  # Remove leading/trailing whitespace
    

    def safe_search_and_process(self,description: Optional[str], category: Optional[str], location: Optional[str], date: Optional[str]) -> List[Any]:
        # Sanitize each input
        try:
            description = self.sanitize_input(description)
            category = self.sanitize_input(category)
            location = self.sanitize_input(location)
            date = self.sanitize_input(date)
        except ValueError as e:
            print(f"Input validation error: {e}")
            return []

        # Safe execution
        try:
            searcher = ItemSearch("DB/AchadosEPerdidos.db")
            search_results = searcher.search_item(description, category, location, date)
            return search_results
        except Exception as e:
            print(f"Error during search or processing: {e}")
            return []

   

