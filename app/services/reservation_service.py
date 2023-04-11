from app.core.property.domain.property_dto import PropertyDTO
from app.core.property.domain.property import Property
from app.core.reservation.domain.reservation_rule_factory import ReservationRuleFactory
from app.core.reservation.domain.reservation_rule import ReservationRule


class ReservationService:
    def __init__(self) -> None:
        self.reservationRuleFactory = ReservationRuleFactory()

    def couldCancel(self, propertyDto: PropertyDTO, days: int) -> bool:
        rule: ReservationRule = self.reservationRuleFactory.getRule(
            propertyDto.type
        )
        property: Property = Property(
            propertyDto.propertyId,
            propertyDto.name,
            propertyDto.type,
            propertyDto.maxGuest
        )
        return rule.couldCancel(property, days)
