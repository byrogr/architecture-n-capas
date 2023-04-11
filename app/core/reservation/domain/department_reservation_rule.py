from app.core.property.domain.property import Property
from app.core.reservation.domain.reservation_rule import ReservationRule


class DeparmentReservationRule(ReservationRule):
    def couldCancel(self, property: Property, days: int) -> bool:
        return False
