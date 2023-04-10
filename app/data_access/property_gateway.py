import sqlite3
import sys

from app.domain.property_dto import PropertyDTO


class SingletonPropertyGateway(type):
    _instances = {}

    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwds)
            cls._instances[cls] = instance
        return cls._instances[cls]


class PropertyGateway(metaclass=SingletonPropertyGateway):
    connection = None

    def __init__(self) -> None:
        self.setupDb()

    def setupDb(self) -> None:
        self.connection = sqlite3.connect(f'{sys.path[0]}/data/demo.db')
        print("Connection to SQLite has been established.\n")
        try:
            self.connection.execute(
                """create table properties (
                propertyId integer primary key autoincrement,
                name text not null,
                type integer not null,
                maxGuest integer not null
                )"""
            )
            print("properties table was created\n")
            self.insertDb()
        except sqlite3.OperationalError:
            print("properties table already exists\n")
        self.connection.close()

    def insertDb(self) -> None:
        print("records inserted success\n")
        self.connection.execute(
            "insert into properties(name, type, maxGuest) values (?,?,?)",
            ("Apartamento de 3 habitaciones en el sur de la ciudad", 1, 5)
        )
        self.connection.execute(
            "insert into properties(name, type, maxGuest) values (?,?,?)",
            ("Habitación con cama doble", 2, 2)
        )
        self.connection.execute(
            "insert into properties(name, type, maxGuest) values (?,?,?)",
            ("Sofá cama en apartamento bonito", 3, 1)
        )
        self.connection.commit()

    def getAll(self) -> list:
        properties: list[PropertyDTO] = []
        try:
            self.connection = sqlite3.connect(f'{sys.path[0]}/data/demo.db')
            resultSet = self.connection.execute(
                "SELECT propertyId, name, type, maxGuest FROM properties"
            )
            for row in resultSet.fetchall():
                property = PropertyDTO(row[0], row[1], row[2], row[3])
                properties.append(property)
            return properties
        except sqlite3.OperationalError:
            print("could not get the records from database")
