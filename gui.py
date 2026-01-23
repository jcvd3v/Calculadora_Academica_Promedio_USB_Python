import customtkinter as ctk

# Appearance.
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Window settings
app = ctk.CTk()
app.title("Calculadora Academica USB")
app.geometry("600x400")

# Grid settings. 2 Columns: Subjects/Buttons
app.grid_columnconfigure(0, weight=3)  # Subjects Column
app.grid_columnconfigure(1, weight=1)  # Buttons Column
app.grid_rowconfigure(0,1)

# Table
frame = ctk.CTkFrame (
    app,
    border_width=2,
    border_color="gray",
    corner_radius=20
)
frame.pack(pady=20, padx=10, fill="both", expand=True)

# Buttons
btn_add = ctk.CTkButton(frame, text="Agregar Materia")
btn_add.pack()
btn_delete = ctk.CTkButton(frame, text="Eliminar Materia")
btn_delete.pack()
btn_modify = ctk.CTkButton(frame, text="Modificar Materia")
btn_modify.pack()
btn_stats = ctk.CTkButton(frame, text="Ver Estadisticas")
btn_stats.pack()

# Run
app.mainloop()