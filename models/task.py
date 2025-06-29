from typing import Dict

class Task:
    def __init__(self, titulo: str, completada: bool = False):
        self.titulo = titulo
        self.completada = completada

    def to_dict(self) -> Dict:
        return {
            "titulo": self.titulo,
            "completada": self.completada
        }

    @staticmethod
    def from_dict(data: Dict):
        return Task(data["titulo"], data["completada"])
