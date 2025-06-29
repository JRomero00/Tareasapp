from typing import List
from models.task import Task

def mostrar_tareas(tareas: List[Task]) -> None:
    if not tareas:
        print("No hay tareas registradas.")
    else:
        for i, tarea in enumerate(tareas, start=1):
            estado = "✅" if tarea.completada else "❌"
            print(f"{i}. {tarea.titulo} - {estado}")

def pedir_opcion() -> str:
    print("\n--- Menú ---")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")
    return input("Elige una opción: ")

def pedir_titulo() -> str:
    return input("Ingresa el título de la tarea: ")

def pedir_indice() -> int:
    try:
        return int(input("Ingresa el número de tarea: ")) - 1
    except ValueError:
        return -1

def mostrar_mensaje(mensaje: str) -> None:
    print(mensaje)
