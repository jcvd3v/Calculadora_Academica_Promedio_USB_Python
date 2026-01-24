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

# Table headers
headers = ["ID", "Creditos", "Nota"]
for i, head in enumerate(headers):
    label = ctk.CTkLabel(frame_table, text=head, font=ctk.CTkFont(weight="bold"))
    label.grid(row=0, column=i, padx=10, pady=5)

# ----- RIGHT SECTION ----- #
# Buttons
frame_controls = ctk.CTkFrame(app, fg_color="transparent")
frame_controls.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

btn_add = ctk.CTkButton(frame_controls, text="Agregar Materia")
btn_add.pack()

btn_delete = ctk.CTkButton(frame_controls, text="Eliminar Materia")
btn_delete.pack()

btn_modify = ctk.CTkButton(frame_controls, text="Modificar Materia")
btn_modify.pack()

btn_stats = ctk.CTkButton(frame_controls, text="Ver Estadisticas")
btn_stats.pack()

# Average box
lbl_average = ctk.CTkLabel(frame_controls, text=f"Promedio: 1",
                           height=60, 
                           fg_color="white", 
                           text_color="black",
                           corner_radius=8)

lbl_average.pack(side="bottom", fill="x", pady=20)

# Run
app.mainloop()