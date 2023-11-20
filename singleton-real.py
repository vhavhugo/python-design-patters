import sqlite3

#connection = _sqlite3.connect("aquarium.db")

from typing import Any

class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
           
class Database(metaclass=MetaSingleton):
    connection = None
    def connect(self):
        if self.connect is None:
            self.connect = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj

db1 = Database().connect()
db2 = Database().connect()

print("Database Objects DB1", db1)
print("Database objects DB2", db2)