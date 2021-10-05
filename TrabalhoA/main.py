import json
import sys
import time
import msgpack


def serialize(d):
    with open('jsonSerialized.txt', 'w') as f:
        json.dump(d, f, cls=Encoder)

def deserialize():
    with open('jsonSerialized.txt') as f:
        json.load(f)

def gen_owners(n, owners):
    for i in range(1, n + 1):
        name = "Owner" + str(i)
        owners.append(Owner(i, name, "19/10/2000", "912345678", "Coimbra"))

def gen_pets(n, pets):
    for i in range(1, n + 1):
        name = "Pet" + str(i)
        species = "Species" + str(i)
        description = name + "that belongs to " + species
        if i % 2 == 0:
            pets.append(Pet(i, name, species, "Male", 8, "10/04/2005", description, i))
        else:
            pets.append(Pet(i, name, species, "Female", 4, "10/04/2005", description, i))

def genData(n):
    data = []
    gen_owners(n, data)
    gen_pets(n, data)
    return data


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


def encoderMsgPack(o):
    return o.__dict__

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = genData(100) #gerar dados

    startS = time.perf_counter()
    serialize(data)
    endS = time.perf_counter()

    startD = time.perf_counter()
    deserialize()
    endD = time.perf_counter()

    print(f"[JSON] - Serializing time: {endS - startS}")
    print(f"[JSON] - Deserialization time {endD - startD}")

    # MSG PACK
    print("MSG PACK")

    with open('msgPackSerialized.txt', 'wb') as f:
        mpStartS = time.perf_counter()
        msgpack.pack(data, f, default=encoderMsgPack)
        mpEndS = time.perf_counter()

    mpStartD = time.perf_counter()
    with open('msgPackSerialized.txt', 'rb') as f:
        unpackedOwners = msgpack.unpack(f)
    mpEndD = time.perf_counter()

    print(f"[MSG PACK] - Serialization time: {mpEndS - mpStartS}")
    print(f"[MSG PACK] - Deserialization time: {mpEndD - mpStartD}")
    #print(packed)
    #print(unpacked)