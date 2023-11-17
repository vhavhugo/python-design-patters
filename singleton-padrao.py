class Singleton:
    __instance__ = None
    def __init__(self):
        if not Singleton.__instance:
            print(" __init__ method called.. ")
        else:
            print("Instance already created:", self.getInstance())
    
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance
    
s = Singleton() ## classe é inicializada, mas o objeto não é criado
print("Object created", Singleton.getInstance()) #O objeto é criado aqui
s1 = Singleton() ## instância já criada