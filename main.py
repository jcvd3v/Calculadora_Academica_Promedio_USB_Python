# Sistema de Calificaciones USB. Sumar calificaciones USB y Creditos Inscritos. Calcular el promedio actual.  Identifica Estado de PP.
# Features a desarrollar: Agregar Interfaz Grafica, Estadisticas de Materias o ramas Fuertes Y debiles para recomendar en cuales debe enfocarse. Modificar creditos y nota de materia (no hara falta simulador).
# Si es la primera vez que el usuario abre el programa (no existe archivo csv) que le pida ingresar materias.

# ============== Modelos ============= #
from src.models.materia import Materia

# ============== Servicios ============= #
from src.logic.calculadora import Calculadora
import src.utils.data_handler as dh

materias = dh.leer_materias()

if __name__ == "__main__":
    calculadora = Calculadora(materias)
    while True:
        print("Opciones:\n1. Ver materias\n2. Ver Status\n3. Agregar materia\n4. Eliminar materia\n5. Modificar materia\n0 Salir")
        entrada = input("Elija una opción: ")
        if entrada == "1":
            calculadora.mostrar_materias()
        elif entrada == "2":
            print(calculadora.promedio())
            calculadora.periodo_de_prueba()
        elif entrada == "3":
            calculadora.agregar_materia()
        elif entrada == "4":
            calculadora.eliminar_materia()
        elif entrada == "5":
            calculadora.modificar_materia()
        elif entrada == "0":
            exit
        else:
            print("Opcion no valida")
    