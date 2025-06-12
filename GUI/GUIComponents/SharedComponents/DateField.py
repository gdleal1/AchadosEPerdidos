from tkcalendar import DateEntry

class DateField(DateEntry):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            date_pattern='dd/mm/yyyy',
            background='gray',
            foreground='white',
            **kwargs
        )
        self.bind("<Key>", lambda e: "break")