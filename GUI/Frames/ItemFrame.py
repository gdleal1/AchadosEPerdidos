import customtkinter as ck
from GUI.GUIComponents.SharedComponents.LogoImage import LogoImage

class ItemFrame(ck.CTkFrame):
    def __init__(self, master, item_data, click_callback):
        super().__init__(master, corner_radius=10)
        self.item_data = item_data
        self.click_callback = click_callback
        
        self.configure(cursor="hand2")
        self.bind("<Button-1>", lambda e: self.click_callback(self.item_data))
        
        # Item name
        self.item_name_label = ck.CTkLabel(
            self, 
            text=f"📦 {item_data['description'].title()}", 
            font=("Arial", 14, "bold")
        )
        self.item_name_label.pack(anchor="w", padx=10, pady=(5, 0))
        self.item_name_label.bind("<Button-1>", lambda e: self.click_callback(self.item_data))
        self.item_name_label.configure(cursor="hand2")

        # Item info
        self.info_label = ck.CTkLabel(
            self,
            text=f"Local: {item_data['location'].title()}  |  Data: {item_data['date']} |  Categoria: {item_data['category']}",
            font=("Arial", 12)
        )
        self.info_label.pack(anchor="w", padx=10, pady=(0, 5))
        self.info_label.bind("<Button-1>", lambda e: self.click_callback(self.item_data))
        self.info_label.configure(cursor="hand2")

        self.pack(fill="x", padx=10, pady=10)