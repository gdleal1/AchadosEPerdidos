import customtkinter as ck

class ReturnedItemsListBox(ck.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.returned_items = []
    
    def add_returned_item(self, item):
        self.returned_items.append(item)

        item_frame = ck.CTkFrame(self)
        item_frame.pack(fill="x", pady=5, padx=5)

        name_label = ck.CTkLabel(item_frame, text=f"Item: {item['description']}", font=("Arial", 16, "bold"))
        found_label = ck.CTkLabel(item_frame, text=f"Encontrado por: {item['email']}")
        returned_label = ck.CTkLabel(item_frame, text=f"Devolvido para: {item['owner_email']}")

        name_label.pack(anchor="w", padx=5)
        found_label.pack(anchor="w", padx=5)
        returned_label.pack(anchor="w", padx=5)