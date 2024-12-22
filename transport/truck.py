from .vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, capacity, color, current_load=0):
        super().__init__(capacity, current_load)
        self.color = color

    def __str__(self):
        return (f"Грузовик(ID: {self.vehicle_id}, грузоподъёмность: {self.capacity}, количество груза в грузовике: {self.current_load}, цвет: {self.color})")