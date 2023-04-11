from app.data_access.property_gateway import PropertyGateway
from app.core.property.domain.property_dto import PropertyDTO


class PropertyService:
    propertyGateway: PropertyGateway = None

    def __init__(self) -> None:
        self.propertyGateway = PropertyGateway()

    def getAllProperties(self) -> list:
        properties: list = []
        rows = self.propertyGateway.getAll()
        for row in rows:
            property = PropertyDTO(row[0], row[1], row[2], row[3])
            properties.append(property)
        return properties
