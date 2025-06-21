import customtkinter as ck

class FoundItemsListBox(ck.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.item_frames = []

    def add_item(self, item_name):
        # Creates a frame for each item
        item_frame = ck.CTkFrame(self)
        item_frame.pack(fill="x", padx=5, pady=5)

        # Item label
        item_label = ck.CTkLabel(item_frame, text=item_name)
        item_label.pack(side="left", padx=(10, 5), pady=5)

        # Button to change item status
        item_button = ck.CTkButton(item_frame, text="Item foi devolvido",
                                   command=lambda: self._change_item_status(item_name))
        item_button.pack(side="right", padx=10, pady=5)

        self.item_frames.append(item_frame)

    def clear_items(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.item_frames.clear()

    def _change_item_status(self, item_name):
        pass
