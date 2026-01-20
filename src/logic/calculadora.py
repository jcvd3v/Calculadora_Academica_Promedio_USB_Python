from src.models.materia import Materia
import src.utils.data_handler as dh
class Calculadora:
    def __init__(self, materias):
        self.materias = materias
    def promedio(self):
        total_creditos = 0
        total_notas = 0
        for materia in self.materias:
            nota = materia.nota * materia.creditos
            total_creditos += materia.creditos
            total_notas += nota
        promedio = total_notas/total_creditos
        return promedio
    def periodo_de_prueba(self):
        promedio = self.promedio()
        if promedio < 3.0:
            print("Estás en Periodo de Prueba")
            return True
        else:
            print("No estás en Periodo de Prueba")
            return False
    def mostrar_materias(self):
        for materia in self.materias:
            print (f"{materia.codigo} Creditos: {materia.creditos} Nota Obtenida: {materia.nota}")
    def agregar_materia(self):
        codigo = input("ID: ")
        creditos = int(input("Creditos: "))
        nota = int(input("Nota Obtenida: "))
        self.materias.append(Materia(codigo, creditos, nota))
        dh.escribir_materia(codigo, float(creditos), float(nota))

    def eliminar_materia(self):
        codigo = input("ID: ")
        self.materias = [m for m in self.materias if m.codigo != codigo]
        #dh.borrar_materia(codigo)
