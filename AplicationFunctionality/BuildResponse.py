class FoundItemProcessor:
    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.processed_items = []
        self._process_items()

    def _process_items(self):
        """Process raw database records into clean item objects"""
        for item in self.raw_data:
            processed = {
                'id': item['code'],
                'description': item['description'],
                'category': item['category'],
                'location': item['local'],
                'date': self._format_date(item['date']),
                'status': 'found'  # Could be dynamic if your system tracks status
            }
            self.processed_items.append(processed)

    def _format_date(self, date_int):
        """Convert YYYYMMDD integer to human-readable date"""
        date_str = str(date_int)
        return f"{date_str[6:8]}/{date_str[4:6]}/{date_str[0:4]}"

    def get_all_items(self):
        """Return all processed items"""
        return self.processed_items

    def get_item_by_id(self, item_id):
        """Get specific item by its ID"""
        for item in self.processed_items:
            if item['id'] == item_id:
                return item
        return None

    def filter_by_category(self, category_name):
        """Filter items by category name"""
        return [item for item in self.processed_items 
                if item['category'].lower() == category_name.lower()]

    def search_in_descriptions(self, search_term):
        """Search for term in item descriptions"""
        return [item for item in self.processed_items 
                if search_term.lower() in item['description'].lower()]


# Example usage:
if __name__ == "__main__":
    # Simulated database response
    db_response = [{
        'code': 1,
        'description': 'Jaqueta preta encontrada',
        'category': 'Roupas',
        'local': 'Praça Central',
        'date': 20240301
    }]

    # Process the data
    processor = FoundItemProcessor(db_response)

    # Get all items in clean format
    print("All items:")
    for item in processor.get_all_items():
        print(item)

    # Example of filtering
    print("\nClothing items:")
    for item in processor.filter_by_category("Roupas"):
        print(item)

    # Example of searching
    print("\nSearch results for 'preta':")
    for item in processor.search_in_descriptions("preta"):
        print(item)