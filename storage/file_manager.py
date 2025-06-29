import json
import os
from typing import List
from models.task import Task

TAREAS_FILE = "tareas.json"

def cargar_tareas() -> List[Task]:
    if os.path.exists(TAREAS_FILE):
        with open(TAREAS_FILE, "r") as archivo:
            data = json.load(archivo)
            return [Task.from_dict(t) for t in data]
    return []

def guardar_tareas(tareas: List[Task]) -> None:
    with open(TAREAS_FILE, "w") as archivo:
        json.dump([t.to_dict() for t in tareas], archivo, indent=4)
