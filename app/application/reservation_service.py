class ReservationService:
    def canCancelReservation(self, daysToBooking: int, propertyType: int) -> str:
        enableToCancel = True
        messageToCancel = "---> Se puede cancelar la reserva <---"
        if daysToBooking < 3:
            enableToCancel = False
        else:
            if propertyType == 1:
                enableToCancel = False

        if not enableToCancel:
            messageToCancel = "---> No se puede cancelar la reserva <---"
        return messageToCancel
