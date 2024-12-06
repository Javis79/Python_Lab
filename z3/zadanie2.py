import json

class Person:
    def __init__(self, name, surname, address, zipcode, pesel):
        self.n = name
        self.s = surname
        self.a = address
        self.z = zipcode
        self.p = pesel

    def save_to_json(self, file):
        with open(file, 'w', encoding='utf-8') as fil:
            json.dump(self.__dict__, fil, ensure_ascii=False, indent=4)

    @classmethod
    def open_from_json(cls, file):
        with open(file, 'r', encoding='utf-8') as fil:
            data = json.load(fil)

        mapping = {
            "n": "name",
            "s": "surname",
            "a": "address",
            "z": "zipcode",
            "p": "pesel"
        }

        data2 = {mapping[k]: v for k, v in data.items() if k in mapping}
        return cls(**data2)


x = Person("Jan", "Kowalski", "Krakow 132", "33-103", "123456789012")
print(x.__dict__)

x.save_to_json("x.json")
y = Person.open_from_json("x.json")

print(y.__dict__)
