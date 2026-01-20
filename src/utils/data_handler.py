import csv
import pandas as pd
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
    with open('data\materias_test.csv', 'a', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(datos)

def borrar_materia(materias_restantes):
    datos = materias_restantes
    with open('data\materias_test.csv', 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(datos)
'''
def borrar_materia(codigo):
    materias = leer_materias()
    datos = [m for m in materias if m.codigo != codigo]
    with open('data\materias_test.csv', 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(datos)


def borrar_materia(ruta, columna, valor):
    df = pd.read_csv(ruta, columna, valor)
    eliminar = (df[columna] == valor).sum()
    df = df[df[columna] != valor]
    df.to_csv(ruta, index=False)'''