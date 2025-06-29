from typing import List
from models.task import Task
from storage.file_manager import cargar_tareas, guardar_tareas
from views.cli_view import (
    mostrar_tareas,
    pedir_opcion,
    pedir_titulo,
    pedir_indice,
    mostrar_mensaje
)

def ejecutar_aplicacion():
    tareas: List[Task] = cargar_tareas()

    while True:
        opcion = pedir_opcion()

        if opcion == "1":
            mostrar_tareas(tareas)

        elif opcion == "2":
            titulo = pedir_titulo()
            tareas.append(Task(titulo))
            guardar_tareas(tareas)
            mostrar_mensaje("Tarea agregada.")

        elif opcion == "3":
            mostrar_tareas(tareas)
            indice = pedir_indice()
            if 0 <= indice < len(tareas):
                tareas[indice].completada = True
                guardar_tareas(tareas)
                mostrar_mensaje("Tarea completada.")
            else:
                mostrar_mensaje("Índice inválido.")

        elif opcion == "4":
            mostrar_tareas(tareas)
            indice = pedir_indice()
            if 0 <= indice < len(tareas):
                tareas.pop(indice)
                guardar_tareas(tareas)
                mostrar_mensaje("Tarea eliminada.")
            else:
                mostrar_mensaje("Índice inválido.")

        elif opcion == "5":
            mostrar_mensaje("¡Hasta luego!")
            break

        else:
            mostrar_mensaje("Opción inválida.")
