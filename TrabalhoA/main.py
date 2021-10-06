import json
import time
import msgpack
import statistics

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


def JSON(n, data):
    s = open("json_time_s.txt", "w")
    d = open("json_time_d.txt", "w")
    times_s = []
    times_d = []
    for i in range(n):
        with open('json_serialized.txt', 'w') as f:
            startS = time.perf_counter()
            json.dump(data, f, cls=Encoder)
            endS = time.perf_counter()


        with open('json_serialized.txt') as f:
            startD = time.perf_counter()
            json.load(f)
            endD = time.perf_counter()

        timeS = endS - startS
        timeD = endD - startD

        times_s.append(timeS)
        times_d.append(timeD)

        s.write(str(timeS) + '\n')
        d.write(str(timeD) + '\n')

        #print(f"[JSON] - Serialization time: {timeS}")
        #print(f"[JSON] - Deserialization time {timeD}")

    s.write('\n' + str(statistics.mean(times_s)))
    s.write('\n' + str(statistics.pstdev(times_s)))
    d.write('\n' + str(statistics.mean(times_d)))
    d.write('\n' + str(statistics.pstdev(times_d)))

    s.close()
    d.close()


def MSGPACK(n, data):
    s = open("msgpack_time_s.txt", "w")
    d = open("msgpack_time_d.txt", "w")
    times_s = []
    times_d = []
    for i in range(n):
        with open('msgpack_serialized.txt', 'wb') as f:
            startS = time.perf_counter()
            msgpack.pack(data, f, default=encoder_msgpack)
            endS = time.perf_counter()

        with open('msgpack_serialized.txt', 'rb') as f:
            startD = time.perf_counter()
            msgpack.unpack(f)
            endD = time.perf_counter()

        timeS = endS - startS
        timeD = endD - startD

        times_s.append(timeS)
        times_d.append(timeD)

        s.write(str(timeS) + '\n')
        d.write(str(timeD) + '\n')

        #print(f"[MSG PACK] - Serialization time: {timeS}")
        #print(f"[MSG PACK] - Deserialization time: {timeD}")

    s.write('\n' + str(statistics.mean(times_s)))
    s.write('\n' + str(statistics.pstdev(times_s)))
    d.write('\n' + str(statistics.mean(times_d)))
    d.write('\n' + str(statistics.pstdev(times_d)))

    s.close()
    d.close()


def encoder_msgpack(o):
    return o.__dict__


def gen_owners(n, owners):
    for i in range(1, n + 1):
        name = "Owner " + str(i)
        owners.append(Owner(i, name, "19/10/2000", "912345678", "Coimbra"))


def gen_pets(n, pets):
    for i in range(1, n + 1):
        name = "Pet " + str(i)
        species = "Species " + str(i)
        description = name + " that belongs to " + species
        if i % 2 == 0:
            pets.append(Pet(i, name, species, "Male", 8, "10/04/2005", description, i))
        else:
            pets.append(Pet(i, name, species, "Female", 4, "10/04/2005", description, i))


def gen_data(n):
    data = []
    gen_owners(n, data)
    gen_pets(n, data)
    return data


if __name__ == '__main__':
    data = gen_data(100) #gerar dados
    reps = 10
    JSON(reps, data)
    MSGPACK(reps, data)