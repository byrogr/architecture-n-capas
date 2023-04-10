from app.data_access.property_gateway import PropertyGateway


class PropertyService:
    propertyGateway: PropertyGateway = None

    def __init__(self) -> None:
        self.propertyGateway = PropertyGateway()

    def getAllProperties(self) -> list:
        return self.propertyGateway.getAll()
