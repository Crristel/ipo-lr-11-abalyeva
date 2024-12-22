from .vehicle import Vehicle

class Train(Vehicle):
    def __init__(self, capacity, number_of_cars, current_load=0):
        super().__init__(capacity, current_load)
        self.number_of_cars = number_of_cars

    def __str__(self):
        return f"Поезд(ID: {self.vehicle_id}, грузоподъёмность: {self.capacity}, список клиентов, чьи грузы загружены: {self.current_load}, число вагонов: {self.number_of_cars})"