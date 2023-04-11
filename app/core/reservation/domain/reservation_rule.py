from abc import ABCMeta
from abc import abstractmethod
from app.core.property.domain.property import Property


class ReservationRule(metaclass=ABCMeta):
    @abstractmethod
    def couldCancel(self, property: Property, days: int) -> bool:
        pass
