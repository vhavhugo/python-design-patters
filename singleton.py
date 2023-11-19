class Singleton(object):
     #__new__ = método especial para instaciar objeto
    def __new__(cls):
        #hasttr = método especial para saber se um objeto tem determinada propriedade
        # verifica se o objeto cls tem a propiedade instance, que confere se a classe já tem um objeto.
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
    
s = Singleton()
print("Object created", s)

s1 = Singleton()
print("Object created", s1)