from src.models.materia import Materia
import src.utils.data_handler as dh
subjects = dh.leer_materias()

for n, m in enumerate(subjects):  # n=index, m=subject instance
    print(n, m.codigo, m.creditos, m.nota)

materia=Materia("Ma", 3, 3)
for c, cr, n in enumerate(materia):
    print(c, cr, n)