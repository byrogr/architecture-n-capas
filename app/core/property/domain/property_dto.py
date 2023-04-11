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
        self.typeText = self.getPropertyTypeText()
        self.maxGuest = maxGuest

    @classmethod
    def getPropertyTypeText(cls) -> str:
        typeText: str = ""
        if cls.type == 1:
            typeText = "Departamento"
        elif cls.type == 2:
            typeText = "Mini-Departamento"
        elif cls.type == 3:
            typeText = "Cuarto"
        return typeText
