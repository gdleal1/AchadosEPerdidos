import customtkinter as ck
from tkinter import messagebox
from AplicationFunctionality.ItemService import ItemService

class AnnounceButton(ck.CTkButton):
    def __init__(self, master, frame_ref, session, **kwargs):
        super().__init__(master, text="Anunciar Item", command=self.announce_action, **kwargs)
        self.frame = frame_ref
        self.session = session
    
    
    def announce_action(self):
        itemService = ItemService()
        item_name = self.frame.item_name_entry.get()
        description = self.frame.description_text.get("1.0", "end-1c").strip()
        category = self.frame.category_combobox.get()
        location = self.frame.location_entry.get()
        date = self.frame.date_entry.get()
        codu = self.session.user_codu

        addedItem = itemService.add_found_item(codu, category, item_name, description, date, location)

        if addedItem:
            messagebox.showinfo("Sucesso", "Item anunciado com sucesso!")
        
        else:
            messagebox.showerror("Erro", "Não foi possível anunciar o item. Verifique os dados e tente novamente.")
        