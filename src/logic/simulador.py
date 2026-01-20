# Revisa el indice completo del estudiante con cada materia inscrita hasta ahora y determina el promedio.
# agrega materias (no a la base de datos solo a la simulacion) y permite probar distintas notas y saca la cuenta para decir si aprueba o no con eso
# ============== Modelos ============= #
from materia import Materia
from usuario import Usuario

# ============== Servicios ============= #
from calculadora import Calculadora

# ============== Base de Datos ============= #
import database

materias = database.materias_cursadas()
materias_en_curso = []
calculadora = Calculadora(materias)
promedio_minimo = 3
promedio_actual = (calculadora.promedio())
promedio_simulado = 0

for materia in materias:
    print (materia.creditos, materia.nota)

def agregar_materia():
    codigo = input("ID: ")
    creditos = int(input("Creditos: "))
    nota = int(input("Nota Obtenida: "))
        materias.append(Materia(codigo, creditos, nota))

