from dataclasses import dataclass

from flask import request


@dataclass
class Langage:
    id: int
    langages: str
    framework: str

    def __repr__(self) -> str:
        return f"{self.langages} is language. {self.framework} is framework"

    def get(self):
        return {"id": self.id, "Language": self.langages, "framework": self.framework}

    @classmethod
    def insert(cls, languages):
        new_language = request.get_json()
        new_language["id"] = len(languages) + 1
        languages.append(new_language)
