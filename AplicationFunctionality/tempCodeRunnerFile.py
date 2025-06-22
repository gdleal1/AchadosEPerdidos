from AplicationFunctionality.UserService import UserService

class FoundItemProcessor:
    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.processed_items = []
        self._process_items()
        self.userService = UserService()