import sys, names

def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    o1 = Owner(1, 'Ze', 19/10/2000, 987654321, 'Coimbra')
    o2 = Owner(None, None, None, None, None)
    l = []
    l.append(o1)
    l.append(o2)
    print(sys.getsizeof(l))
    print("##")
    for i in range(10):
        print(names.get_full_name())





def genOwner(n):

     for i in range (n):
         name = names.get_full_name(gender='male')
         print(name)


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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi()
    genOwner(100)
