
class Client:
    def __init__(self, name, cargo_weight, is_vip=False):
        self.name = name
        try:
            cargo_weight = int(cargo_weight)
            self.cargo_weight = cargo_weight
        except ValueError:
            raise ValueError("Вес груза должен быть указан числом")
        if not isinstance(is_vip, bool):
            raise ValueError("Флаг VIP статуса указывается типом bool")
        self.is_vip = is_vip

    def __str__(self):
        return f"Клиент (имя: {self.name}, вес груза: {self.cargo_weight}, VIP: {self.is_vip})"
