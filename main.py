from transport import Client, Truck, Train, TransportCompany

Menu = True
all_clients = []
all_vehicles = []
all_company = []


def menu():
    print(f"Меню".center(35,"~"))
    print(f"1 - Создать клиента")
    print(f"2 - Управлять транспортом")
    print(f"3 - Управлять компаниями")
    print(f"4 - Вывести информацию о всех клиентах")
    print(f"5 - Вывести информацию о всех транспортах")
    print(f"6 - Вывести информацию о всех компаниях")
    print(f"7 - Выход")

def vehicle_menu():
    print(f" Управлять транспортом".center(35,"~"))
    print(f"1 - Создать грузовик")
    print(f"2 - Создать поезд")
    print(f"3 - Загрузить груз клиента в транспорт")

def company_menu():
    print(f"Управлять компаниями".center(35,"~"))
    print(f"1 - Создать компанию")
    print(f"2 - Добавить транспортное средство в компанию")
    print(f"3 - Список всех транспортных средств компании")
    print(f"4 - Добавить клиента в компанию")
    

while Menu:
    menu()
    input_num = input("Введите номер: ")
    if not input_num.isdigit():
        print("Введите корректное значение номера пункта меню!")
        continue  

    input_num = int(input_num)

    if input_num == 1:
        name = input("Введите имя нового клиента: ")
        cargo = input("Введите вес груза нового клиента: ")
        while True:
            is_vip = input("Укажите, является ли новый клиент VIP? (1 - да / 2 - нет) ")
            if is_vip in ("1", "2"):  
                is_vip = (is_vip == "1")  
                break
            else:
                print("Введите корректное значение (1 или 2)")

        if not cargo.isdigit():
            print("Некорректный формат веса груза! Введите целое число.")
            continue 

        cargo = int(cargo)
        if cargo < 0:
            print("Вес груза не может быть отрицательным!")
        else:
            all_clients.append(Client(name, cargo, is_vip))
            print("Новый клиент создан!")



    elif input_num == 2:
        vehicle_menu()
        while True:
            input_num = input("Введите номер: ")
            if not input_num.isdigit():
                print("Введите корректное числовое значение!")
                continue
            input_num = int(input_num)
            if 1 <= input_num <= 3:
                break
            else:
                print("Введите число от 1 до 3.")

        if input_num == 1:
            while True:
                capacity_str = input("Введите грузоподъемность грузовика: ")
                if not capacity_str.isdigit():
                    print("Грузоподъемность должна быть целым числом!")
                    continue
                capacity = int(capacity_str)
                if capacity < 0:
                    print("Грузоподъемность не может быть отрицательной!")
                    continue
                color = input("Введите цвет грузовика: ")
                if not color.isalpha():
                    print("Цвет грузовика должен содержать только буквы!")
                    continue
                all_vehicles.append(Truck(capacity, color))
                print("Грузовик создан!")
                break

        elif input_num == 2:
            while True:
                capacity_str = input("Введите грузоподъемность поезда: ")
                number_of_cars_str = input("Введите количество вагонов: ")
                if not capacity_str.isdigit() or not number_of_cars_str.isdigit():
                    print("Грузоподъемность и количество вагонов должны быть целыми числами!")
                    continue
                capacity = int(capacity_str)
                number_of_cars = int(number_of_cars_str)
                if capacity < 0 or number_of_cars < 0:
                    print("Грузоподъемность и количество вагонов не могут быть отрицательными!")
                    continue
                all_vehicles.append(Train(capacity, number_of_cars))
                print("Поезд создан!")
                break

        elif input_num == 3:
            while True:
                target_vehicle = input("Введите номер транспорта для загрузки: ")
                target_client = input("Введите номер клиента для загрузки: ")
                if not target_vehicle.isdigit() or not target_client.isdigit():
                    print("Введите корректные номера транспорта и клиента!")
                    break
                target_vehicle = int(target_vehicle)
                target_client = int(target_client)
                if not (1 <= target_vehicle <= len(all_vehicles) and 1 <= target_client <= len(all_clients)):
                    print("Номер транспорта или клиента вне допустимого диапазона!")
                    break
                try:
                    all_vehicles[target_vehicle - 1].load_cargo(all_clients[target_client - 1])
                    print("Груз загружен!")
                    break
                except Exception:
                    print(f"Произошла ошибка при загрузке груза")



    elif input_num == 3:
        company_menu()
        input_num = input("Введите номер: ")

        if input_num.isdigit():
            input_num = int(input_num)
        else:
            print("Введите корректное значение!")
    
        if input_num == 1:
            name = input("Введите название компании: ")
            company = TransportCompany(name)
            all_company.append(company)
            print("Компания создана!")
    
        elif input_num == 2:
            vehicle = input("Введите номер транспорта, который хотите добавить в компанию: ")
            company = input("Введите номер компании, к которой хотите добавить транспорт: ")
        
            if vehicle.isdigit() and company.isdigit():
                vehicle = int(vehicle)
                company = int(company)
                try:
                    all_company[company - 1].add_vehicle(all_vehicles[vehicle - 1])
                    print("Транспорт успешно добавлен!")
                except Exception:
                    print(f"Произошла ошибка! Проверьте корректность введенных данных!")
            else:
                print("Введите корректные значения!")
    
        elif input_num == 3:
            company = input("Введите номер компании, список транспорта которой вы хотите посмотреть: ")
        
            if company.isdigit():
                company = int(company)
                print(f"Вот список транспорта компании с идентификатором {company}:")
                company -= 1
                id = 0
                for vehicle in all_company[company].list_vehicles():
                    id += 1
                    print(f"{id}. {vehicle}")
            else:
                print("Введите корректное значение!")
    
        elif input_num == 4:
            company = input("Введите номер компании, куда хотите добавить клиента: ")
            client = input("Введите номер клиента, которого хотите добавить в компанию: ")
        
            if company.isdigit() and client.isdigit():
                company = int(company)
                client = int(client)
                try:
                    all_company[company - 1].add_client(all_clients[client - 1])
                    print("Клиент успешно добавлен!")
                except ValueError:
                    print("Введите корректное значение!")
            else:
                print("Введите корректные значения!")



    elif input_num == 4:
        if not all_clients:
            print("Клиентов нет!")
        else:
            id = 0
            for client in all_clients:
                id += 1
                vip = "Да" if client.is_vip else "Нет"
                print(f"{id}. Имя: {client.name}. Вес груза: {client.cargo_weight}. VIP-статус: {vip}")



    elif input_num == 5:
        if not all_vehicles:
            print("Созданного транспорта нет!")
        else:
            id_number = 0
            for vehicle in all_vehicles:
                id_number += 1
                print(f"{id_number}. {vehicle}")
            print()


    elif input_num == 6:
        if not all_company:
            print("Созданных компаний нет!")
        else:
            id = 0
            for company in all_company:
                id += 1
                print(f"{id}. Название компании: {company.name}")
                print(f"Список транспортных средств:")
                if company.list_vehicles(): #Проверка на пустоту списка транспорта
                    for vehicle in company.list_vehicles():
                        print(f"| {vehicle}")
                else:
                    print("| Транспортных средств нет.") #Сообщение если транспорта нет.

                print(f"Список клиентов компании:")
                if company.list_clients(): #Проверка на пустоту списка клиентов
                    for client in company.list_clients():
                        vip = "Да" if client.is_vip else "Нет"
                        print(f"Имя клиента: {client.name}. Вес груза: {client.cargo_weight}. VIP-статус: {vip}")
                else:
                    print("| Клиентов нет.") #Сообщение если клиентов нет.




    elif input_num == 7:
        Menu = False
        