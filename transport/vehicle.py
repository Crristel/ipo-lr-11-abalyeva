import random
from .client import Client

class Vehicle:
    def __init__(self, capacity, current_load=0):
        capacity = int(capacity)  
        current_load = int(current_load)  

        self.vehicle_id = str(random.randint(1000, 100000))
        self.capacity = capacity
        self.clients_list = []
        self.current_load = current_load

    def load_cargo(self, client):
        if not isinstance(client, Client):
            raise TypeError("Вы должны передать объект клиента в параметр функции!")
        
        new_weight = self.current_load + client.cargo_weight
        
        if new_weight > self.capacity:
            raise OverflowError("Грузоподъемность превышена!")
        
        self.current_load = new_weight
        self.clients_list.append(client)

    def __str__(self):
        return (f"ID транспорта: {self.vehicle_id}, грузоподъемность транспорта: {self.capacity}, загружено: {self.current_load}")
