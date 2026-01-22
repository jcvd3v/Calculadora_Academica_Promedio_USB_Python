# ============== Modelos ============= #
from src.models.materia import Materia

# ============== Servicios ============= #
from src.logic.calculadora import Calculadora
import src.utils.data_handler as dh

materias = dh.leer_materias()

if __name__ == "__main__":
    calculadora = Calculadora(materias)
    calculadora.modificar_materia()
    calculadora.mostrar_materias()