import customtkinter as ck
from AplicationFunctionality.ItemService import ItemService
from tkinter import messagebox

class FoundItemsListBox(ck.CTkScrollableFrame):
    def __init__(self, master, frame_ref, **kwargs):
        super().__init__(master, **kwargs)
        self.item_frames = []
        self.clear_items()  
        self.frame = frame_ref

    def add_item(self, item):
        
        if (item['status'] != 'active'):
            return
        
        item_frame = ck.CTkFrame(self)
        item_frame.pack(fill="x", padx=5, pady=5)

        item_frame.grid_columnconfigure(0, weight=1)
        item_frame.grid_columnconfigure(1, weight=0)

        # Salva código do item
        item_code = item['code']

        # Item label
        item_label = ck.CTkLabel(item_frame, text=item['description'])
        item_label.grid(row=0, column=0, padx=(10, 5), pady=5, sticky="w")

        # Right-side container for entry + button
        actions_frame = ck.CTkFrame(item_frame, fg_color="transparent")
        actions_frame.grid(row=0, column=1, padx=10, pady=5, sticky="e")

        # Entry
        item_entry = ck.CTkEntry(actions_frame, width=120, placeholder_text="E-mail do usuário")
        item_entry.pack(side="left", padx=(0, 5))

        # Button
        item_button = ck.CTkButton(actions_frame, text="Item foi devolvido",
                                   command=lambda: self._change_item_status(item_code, item_entry.get()))
        item_button.pack(side="left")

        # Button to cancel item
        cancel_button = ck.CTkButton(actions_frame, text="✕", width=30,
                                     fg_color="red", hover_color="#990000",
                                     command=lambda: self._cancel_item_ad(item_code))
        cancel_button.pack(side="left")

        self.item_frames.append(item_frame)

    def clear_items(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.item_frames.clear()

    
    def _change_item_status(self, item_code, user_email):
        itemService = ItemService()
        itemMarkedFound = itemService.mark_item_as_found(item_code, user_email)
        if itemMarkedFound:
            messagebox.showinfo("Sucesso", "Item marcado como encontrado com sucesso!")
            # Update the session and frame
            self.frame.session.initialize_session(self.frame.session.user_codu)
            self.frame.update_frame(self.frame.session)
            self.frame.master.recreate_admin_frame()
        
        else:
            messagebox.showerror("Erro", "Não foi possível marcar o item como encontrado. Verifique se o e-mail do dono está correto.")

    def _cancel_item_ad(self, item_code):
        itemService = ItemService()
        itemMarkedRemoved = itemService.remove_item(item_code)
        if itemMarkedRemoved:
            messagebox.showinfo("Sucesso", "Item removido com sucesso!")
            # Update the session and frame
            self.frame.session.initialize_session(self.frame.session.user_codu)
            self.frame.update_frame(self.frame.session)
            self.frame.master.recreate_admin_frame()
        
        else:
            messagebox.showerror("Erro", "Não foi possível remover o item.")


        


        
