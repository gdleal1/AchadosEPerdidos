import re
from typing import Optional, List, Any
from  AplicationFunctionality.ItemService import ItemService

import re
from typing import Optional, List, Any

class InputVerification:

    @staticmethod
    def sanitize_input(value: Optional[str]) -> Optional[str]:
        if value is None:
            return None
        if not isinstance(value, str):
            raise ValueError(f"Expected a string or None, got {type(value)}")

        # Basic SQL injection check — reject suspicious patterns
        pattern = re.compile(r"(--|\b(OR|AND|SELECT|INSERT|DELETE|UPDATE|DROP|;)\b)", re.IGNORECASE)
        if pattern.search(value):
            raise ValueError(f"Potentially unsafe input detected: {value}")

        return value.strip()  # Remove leading/trailing whitespace

    @staticmethod
    def safe_search_and_process(description: Optional[str], category: Optional[str], location: Optional[str], date: Optional[str]) -> List[Any]:
        # Sanitize each input
        try:
            description = InputVerification.sanitize_input(description)
            category = InputVerification.sanitize_input(category)
            location = InputVerification.sanitize_input(location)
            date = InputVerification.sanitize_input(date)
        except ValueError as e:
            print(f"Input validation error: {e}")
            return []

        # Safe execution
        try:
            searcher = ItemService("Database/AchadosEPerdidos.db")
            search_results = searcher.search_item(description, category, location, date)
            return search_results
        except Exception as e:
            print(f"Error during search or processing: {e}")
            return []

   

