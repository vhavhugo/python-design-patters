# Monostate é um conceito baseado no comportamento do mesmo estado por todos os objetos.
class Borg:
    __shared_state = {"1":"2"}
    def __init__(self):
        self.x = 1
        self.x__dict__ = self.__shared_state
        pass

b = Borg()
b1 = Borg()
b.x = 4

print("Borg Object 'b':", b) ## b e b1 são objetos distintos
print("Borg Object 'b1':", b1)
print("Borg Object 'b':", b.__dict__) ## b e b1 compartilham o mesmo estado
print("Borg Object 'b1':", b1.__dict__)

print("-------------------------##---------------------------------------")

class Borg(object):
    _shared_state = {}
    def __new__(cls, *args, **kwargs);
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__shared__state
        return obj