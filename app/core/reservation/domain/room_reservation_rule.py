from app.core.reservation.domain.reservation_rule import ReservationRule
from app.core.property.domain.property import Property


class RoomReservationRule(ReservationRule):
    def couldCancel(self, property: Property, days: int) -> bool:
        if days < 3:
            return False
        return True
