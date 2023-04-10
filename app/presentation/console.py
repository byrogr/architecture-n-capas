from app.application.property_service import PropertyService
from app.application.reservation_service import ReservationService


class Console:
    propertyService = None
    reservationService = None

    def __init__(self) -> None:
        self.propertyService = PropertyService()
        self.reservationService = ReservationService()

    def start(self):
        while True:
            print("\nOperaciones del sistema\n")
            print("1. Listar propiedades")
            print("2. ¿Es posible cancelar reserva?")
            print("3. Salir\n")
            opt = int(input("Ingrese una opción: "))

            if opt == 3:
                break

            if opt == 1:
                properties: list = self.propertyService.getAllProperties()
                print("\nListado de propiedades\n")
                for property in properties:
                    print(
                        f'Nombre: {property.name}, Tipo: {property.typeText}, Húespedes: {property.maxGuest}'
                    )
                    print(f"{'---'*50}")
            elif opt == 2:
                print("\n")
                daysToBooking = int(input(
                    "¿Cuántos días faltan para el inicio de la reserva? "
                ))
                propertyType = int(input(
                    "¿Qué tipo de propiedad es? (1 = Departamento, 2 = Mini-Departamento, 3 = Cuarto) "
                ))
                messageToCancel = self.reservationService.canCancelReservation(
                    daysToBooking,
                    propertyType
                )
                print(f"\n {messageToCancel}")

        print("Sesión terminada")
