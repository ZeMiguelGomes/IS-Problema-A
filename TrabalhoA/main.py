import json
import sys
import time


def serialize(o):
    return json.dumps(o, indent=4, cls=Encoder)


def deserialize(d):
    return json.loads(d)


def gen_owners(n):
    owners = []
    for i in range(1, n + 1):
        name = "Owner" + str(i)
        owners.append(Owner(i, name, "912345678", "Coimbra"))

    return owners


class Owner(object):
    def __init__(self, id, name, birth, phone, address):
        self.id = id
        self.name = name
        self.birth = birth
        self.phone = phone
        self.address = address


class Pet(object):
    def __init__(self, id, name, species, gender, weight, birth, description, owner):
        self.id = id
        self.name = name
        self.species = species
        self.gender = gender
        self.weight = weight
        self.birth = birth
        self.description = description
        self.owner = owner


class Encoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi()
    owners = gen_owners(1000)

    startS = time.perf_counter()
    jsonData = serialize(owners)
    endS = time.perf_counter()

    startD = time.perf_counter()
    x = deserialize(jsonData)
    endD = time.perf_counter()

    print(endS-startS)
    print(endD-startD)
    print(x)
