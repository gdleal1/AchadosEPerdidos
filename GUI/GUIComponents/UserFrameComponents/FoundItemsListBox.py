import customtkinter as ck

class FoundItemsListBox(ck.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.item_frames = []

    def add_item(self, item_name):
        item_frame = ck.CTkFrame(self)
        item_frame.pack(fill="x", padx=5, pady=5)

        item_frame.grid_columnconfigure(0, weight=1)
        item_frame.grid_columnconfigure(1, weight=0)

        # Item label
        item_label = ck.CTkLabel(item_frame, text=item_name)
        item_label.grid(row=0, column=0, padx=(10, 5), pady=5, sticky="w")

        # Right-side container for entry + button
        actions_frame = ck.CTkFrame(item_frame, fg_color="transparent")
        actions_frame.grid(row=0, column=1, padx=10, pady=5, sticky="e")

        # Entry
        item_entry = ck.CTkEntry(actions_frame, width=120, placeholder_text="Dono")
        item_entry.pack(side="left", padx=(0, 5))

        # Button
        item_button = ck.CTkButton(actions_frame, text="Item foi devolvido",
                                   command=lambda: self._change_item_status(item_name, item_entry.get()))
        item_button.pack(side="left")

        self.item_frames.append(item_frame)

    def clear_items(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.item_frames.clear()

    def _change_item_status(self, item_name, message):
        print(f"Item '{item_name}' marcado como devolvido. Mensagem: {message}")
