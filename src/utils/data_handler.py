import csv
from src.models.materia import Materia

def leer_materias():
    with open('data\materias.csv', 'r', newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        materias = []
        for materia in lector:
            materias.append(Materia(materia[0],float(materia[1]),float(materia[2])))
    return materias

def escribir_materia(codigo, creditos, nota):
    datos = [codigo, creditos, nota]
    with open('data\materias.csv', 'a', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(datos)

def actualizar_materias(materias_actualizadas):
    datos = materias_actualizadas
    with open('data\materias.csv', 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(datos)