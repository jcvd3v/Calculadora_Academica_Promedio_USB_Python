import customtkinter as ctk
from src.models.materia import Materia
import src.utils.data_handler as dh
subjects = dh.leer_materias()

app = ctk.CTk()

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

for n, m in enumerate(subjects):  # n=index, m=subject instance
    print(n, m.codigo, m.creditos, m.nota)
    lblco = ctk.CTkLabel(frame_table,text=str(m.codigo))
    lblco.grid(row=n+1, column=0, padx=10, pady=2)
    lblcr = ctk.CTkLabel(frame_table,text=str(m.creditos))
    lblcr.grid(row=n+1, column=1, padx=10, pady=2)
    lblno = ctk.CTkLabel(frame_table,text=str(m.nota))
    lblno.grid(row=n+1, column=2, padx=10, pady=2)
    checkbox = ctk.CTkCheckBox(frame_table, text="")
    checkbox.grid(row=n+1, column=3, padx=10, pady=2)

app.mainloop()