from AplicationFunctionality.UserService import UserService
from AplicationFunctionality.ItemService import ItemService


class Session:
    def __init__(self):
        self.user_service = UserService()
        self.item_service = ItemService()
        self.user_name = None
        self.user_email = None
        self.user_role = None
        self.user_cellphone = None
        self.user_average_rating = None
        self.user_rating_count = None
        self.found_items = []

    def initialize_session(self, user_codu):
        """Initialize the session with the user's information"""

        self.user_codu = user_codu
        user_infos = self.user_service.get_user_info(self.user_codu)

        self.user_name = user_infos['name']
        self.user_email = user_infos['email']
        self.user_role = user_infos['role']
        self.user_cellphone = user_infos['cellphone']
        
        self.found_items = self.item_service.items_found_by_user(self.user_codu)
        
    def is_moderator(self) -> bool:
        """Returns True if the user is a moderator"""

        return self.user_role == "moderator"
        
        