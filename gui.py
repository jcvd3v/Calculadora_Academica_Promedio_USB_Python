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
app.grid_rowconfigure(0,weight=1)

# ----- LEFT SECTION ----- #
# Table
frame_table = ctk.CTkScrollableFrame (
    app,
    border_width=2,
    border_color="gray",
    corner_radius=20,
    label_text="Materias"
)

frame_table.grid (
    row=0, 
    column=0, 
    padx=20, 
    pady=20, 
    sticky="nsew")

frame_table.pack()

# Table headers
headers = ["ID", "Creditos", "Nota"]
for i, head in enumerate(headers):
    label = ctk.CTkLabel(frame_table, text=head, font=ctk.CTkFont(weight="bold"))
    label.grid(row=0, column=i, padx=10, pady=5)

# Buttons
btn_add = ctk.CTkButton(app, text="Agregar Materia")
btn_add.pack()
btn_delete = ctk.CTkButton(app, text="Eliminar Materia")
btn_delete.pack()
btn_modify = ctk.CTkButton(app, text="Modificar Materia")
btn_modify.pack()
btn_stats = ctk.CTkButton(app, text="Ver Estadisticas")
btn_stats.pack()

# Run
app.mainloop()