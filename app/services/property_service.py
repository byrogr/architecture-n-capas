from app.core.property.domain.property_service import PropertyService as PropertyServiceDomain


class PropertyService:
    def __init__(self) -> None:
        self.propertyService = PropertyServiceDomain()

    def findAll(self):
        return self.propertyService.getAllProperties()
