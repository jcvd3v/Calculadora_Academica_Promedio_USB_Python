# Sistema de Calificaciones USB. Sumar calificaciones USB y Creditos Inscritos. Calcular el promedio actual. Calcular Notas Minimas Requeridas para mantener el promedio. Identifica Estado de PP.
# Implementar dataclass en futuras versiones.
# Agregar Interfaz Grafica, Ingreso De Datos, Registro Academico del Estudiante, USBID, Base de Datos para ese Usuario en base a su USBID, Estadisticas de Materias Fuertes Y debiles para recomendar en cuales debe enfocarse.
# Integrar base de datos
# Crear tabla en base de datos con el titulo de la id del usuario en lugar de usuario, así aseguro que haya solo una por cada usuario.
# Si es la primera vez que el usuario abre el programa (no existe base de datos) que le pida ingresar materias.

# ============== Modelos ============= #
from src.models.materia import Materia

# ============== Servicios ============= #
from src.logic.calculadora import Calculadora
import src.utils.data_handler as dh

materias = dh.leer_materias()

if __name__ == "__main__":
    calculadora = Calculadora(materias)
    calculadora.mostrar_materias()
    print(calculadora.promedio())
    calculadora.periodo_de_prueba()
    calculadora.agregar_materia()
    calculadora.mostrar_materias()
    calculadora.eliminar_materia()
    calculadora.mostrar_materias()
    