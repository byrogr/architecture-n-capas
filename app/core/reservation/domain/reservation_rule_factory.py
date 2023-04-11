from app.core.reservation.domain.reservation_rule import ReservationRule
from app.core.reservation.domain.department_reservation_rule import DeparmentReservationRule
from app.core.reservation.domain.room_reservation_rule import RoomReservationRule
from app.core.reservation.domain.bed_reservation_rule import BedReservationRule


class SingletonReservationRuleFactory(type):
    _instances = {}

    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwds)
            cls._instances[cls] = instance
        return cls._instances[cls]


class ReservationRuleFactory(metaclass=SingletonReservationRuleFactory):

    def getRule(self, type: int) -> ReservationRule:
        rule: ReservationRule = None
        if type == 1:
            rule = DeparmentReservationRule()
        elif type == 2:
            rule = RoomReservationRule()
        elif type == 3:
            rule = BedReservationRule()
        return rule
