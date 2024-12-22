from .client import Client
from .vehicle import Vehicle

class TransportCompany:
    def __init__(self, name):
        self.name = name  # название
        self.vehicles = []  # список транспортных средств
        self.clients = [] #список клиентов

    def add_vehicle(self, vehicle):
        if not isinstance(vehicle, Vehicle):
            raise TypeError("Аргумент vehicle должен быть экземпляром класса Vehicle")
        self.vehicles.append(vehicle)

    def list_vehicles(self):
        return self.vehicles

    def add_client(self, client):
        if not isinstance(client, Client):
            raise TypeError("Аргумент client должен быть экземпляром класса Client")
        self.clients.append(client)

    def list_clients(self):
        return self.clients

        