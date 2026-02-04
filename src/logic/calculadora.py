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

    def agregar_materia(self, codigo, creditos, nota):
        self.materias.append(Materia(codigo, creditos, nota))
        dh.escribir_materia(codigo, float(creditos), float(nota))

    def eliminar_materia(self):
        codigo = input("ID: ")
        self.materias = [m for m in self.materias if m.codigo != codigo]
        dh.actualizar_materias(self.materias)

    def modificar_materia(self):
        codigo = input("ID: ")
        for m in self.materias: 
            if m.codigo == codigo:
                m.creditos = input("Creditos: ")
                m.nota = input("Nota: ")
        dh.actualizar_materias(self.materias)
    
    def ver_estadisticas(self):
        nota_promedio = 0
        for m in self.materias:
            nota_promedio += m.nota 
        nota_promedio = nota_promedio/len(self.materias)
        materias_fuertes = [m for m in self.materias if m.nota >= nota_promedio]
        materias_debiles = [m for m in self.materias if m.nota < nota_promedio] 
        print("Materias fuertes:")
        for m in materias_fuertes:
            print(m.codigo)
        print("Materias debiles:")
        for m in materias_debiles:
            print(m.codigo)