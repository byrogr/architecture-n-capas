class PropertyDTO:
    propertyId: int
    name: str = ""
    type: int = None
    typeText: str = ""
    maxGuest: int = None

    def __init__(self, propertyId: int, name: str, type: int, maxGuest: int) -> None:
        self.propertyId = propertyId
        self.name = name
        self.type = type
        if self.type == 1:
            self.typeText = "Departamento"
        elif self.type == 2:
            self.typeText = "Mini-Departamento"
        elif self.type == 3:
            self.typeText = "Cuarto"
        self.maxGuest = maxGuest
