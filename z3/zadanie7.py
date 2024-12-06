import json
from dataclasses import dataclass

@dataclass
class Person:
    n : str
    s : str
    a : str
    z : str
    p : str

    def save_to_json(self, file):
        with open(file, 'w', encoding='utf-8') as fil:
            json.dump(self.__dict__, fil, ensure_ascii=False, indent=4)

    @classmethod
    def open_from_json(cls, file):
        with open(file, 'r', encoding='utf-8') as fil:
            data = json.load(fil)

        return cls(**data)


x = Person("Jan", "Kowalski", "Krakow 132", "33-103", "123456789012")
print(x.__dict__)

x.save_to_json("x1.json")
y = Person.open_from_json("x1.json")

print(y.__dict__)
