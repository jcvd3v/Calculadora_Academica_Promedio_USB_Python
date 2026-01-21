# Revisa el indice completo del estudiante con cada materia inscrita hasta ahora y determina el promedio.
# agrega materias (no a la base de datos solo a la simulacion) y permite probar distintas notas y saca la cuenta para decir si aprueba o no con eso
# ============== Modelos ============= #
from materia import Materia

# ============== Servicios ============= #
from src.logic.calculadora import Calculadora
import src.utils.data_handler as dh

materias_cursadas = dh.leer_materias()
materias_en_curso = []
calculadora = Calculadora(materias_cursadas)
promedio_minimo = 3
promedio_actual = (calculadora.promedio())
promedio_simulado = 0

for materia in materias_cursadas:
    print (materia.creditos, materia.nota)
calculadora.agregar_materia()

