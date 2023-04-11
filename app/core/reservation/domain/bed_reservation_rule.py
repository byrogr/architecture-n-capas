from app.core.reservation.domain.reservation_rule import ReservationRule
from app.core.property.domain.property import Property


class BedReservationRule(ReservationRule):
    def couldCancel(self, property: Property, days: int) -> bool:
        if days > 3 and property.maxGuest == 2:
            return False
        return True
