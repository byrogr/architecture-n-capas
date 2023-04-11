from app.services.property_service import PropertyService
from app.services.reservation_service import ReservationService


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
                properties: list = self.propertyService.findAll()
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

                properties = self.propertyService.findAll()
                print("\nListado de propiedades")
                for i in range(0, len(properties)):
                    print(f'[{i}] {properties[i].name}')

                propertySelected = int(input(
                    "\n¿De que propiedad deseas cancelar la reserva? "
                ))
                property = properties[propertySelected]
                canCancelProperty = self.reservationService.couldCancel(
                    property,
                    daysToBooking
                )
                messageToCancel = "---> Se puede cancelar la reserva <---"
                if not canCancelProperty:
                    messageToCancel = "---> No se puede cancelar la reserva <---"

                print(f"\n {messageToCancel}")

        print("Sesión terminada")
