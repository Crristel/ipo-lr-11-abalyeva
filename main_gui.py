import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
from transport import Client, Truck, Train, TransportCompany

class TransportApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Транспортная Компания")
        self.transport_company = TransportCompany("Global Transport")
        self._setup_ui()
        self.load_and_display_data()


    def _setup_ui(self):
        self._create_menu()
        self._create_controls()
        self._create_tables()
        self._create_status_bar()
        self.clients_listbox.bind("<Double-Button-1>", self.edit_client)
        self.vehicles_listbox.bind("<Double-Button-1>", self.edit_vehicle)


    def _create_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Экспорт результата", command=self.export_result)
        file_menu.add_command(label="О программе", command=self.show_about)
        file_menu.add_command(label="Выход", command=self.root.quit)
        menu_bar.add_cascade(label="Файл", menu=file_menu)


    def _create_controls(self):
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)
        tk.Button(frame, text="Добавить клиента", command=self.add_client).pack(side=tk.LEFT, padx=5)
        tk.Button(frame, text="Добавить транспорт", command=self.add_vehicle).pack(side=tk.LEFT, padx=5)
        tk.Button(frame, text="Удалить клиента", command=self.delete_client).pack(side=tk.LEFT, padx=5)
        tk.Button(frame, text="Удалить транспорт", command=self.delete_vehicle).pack(side=tk.LEFT, padx=5)


    def _create_tables(self):
        clients_frame = tk.Frame(self.root)
        clients_frame.pack(side=tk.LEFT, padx=10, pady=10)
        tk.Label(clients_frame, text="Список клиентов").pack()
        self.clients_listbox = tk.Listbox(clients_frame, height=10, width=50)
        self.clients_listbox.pack()

        vehicles_frame = tk.Frame(self.root)
        vehicles_frame.pack(side=tk.RIGHT, padx=10, pady=10)
        tk.Label(vehicles_frame, text="Список транспортных средств").pack()
        self.vehicles_listbox = tk.Listbox(vehicles_frame, height=10, width=50)
        self.vehicles_listbox.pack()

    
    def _create_status_bar(self):
        self.status_bar = tk.Label(self.root, text="Готово", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)


    def load_and_display_data(self):
        self.clients_listbox.delete(0, tk.END)
        self.vehicles_listbox.delete(0, tk.END)
        for client in self.transport_company.list_clients():
            self.clients_listbox.insert(tk.END, f"{client}")
        for vehicle in self.transport_company.list_vehicles():
            self.vehicles_listbox.insert(tk.END, f"{vehicle}")


    def add_client(self):
         self._open_client_window("Добавить клиента")

    
    def edit_client(self, event):
        selected_index = self.clients_listbox.curselection()
        if selected_index:
            client = self.transport_company.clients[selected_index[0]]
            self._open_client_window("Редактировать клиента", client)


    def _open_client_window(self, title, client=None):
        self.status_bar.config(text=f"{title}...")
        client_window = tk.Toplevel(self.root)
        client_window.title(title)

        tk.Label(client_window, text="Имя клиента").pack(pady=5)
        client_name_entry = tk.Entry(client_window)
        

        if client:
            client_name_entry.insert(0, client.name)
        client_name_entry.pack(pady=5)
        
        tk.Label(client_window, text="Вес груза (в кг)").pack(pady=5)
        cargo_weight_entry = tk.Entry(client_window)
        if client:
            cargo_weight_entry.insert(0, client.cargo_weight)
        cargo_weight_entry.pack(pady=5)

        vip_status = tk.BooleanVar(value=client.is_vip if client else False)
        tk.Checkbutton(client_window, text="VIP клиент", variable=vip_status).pack(pady=5)


        def save_client():
            name = client_name_entry.get().strip()
            try:
                cargo_weight = int(cargo_weight_entry.get().strip())

                if not name.isalpha() or len(name) < 2:
                    raise ValueError("Имя должно содержать только буквы и быть не менее 2 символов.")
                if cargo_weight <= 0 or cargo_weight > 10000:
                    raise ValueError("Вес груза должен быть положительным числом не более 10000 кг.")

                if not client and any(c.name == name for c in self.transport_company.clients):
                        raise ValueError("Клиент с таким именем уже существует.")

                if client:
                    client.name = name
                    client.cargo_weight = cargo_weight
                    client.is_vip = vip_status.get()
                    self.status_bar.config(text="Клиент обновлен")
                else:
                    new_client = Client(name, cargo_weight, vip_status.get())
                    self.transport_company.add_client(new_client)
                    self.status_bar.config(text="Клиент добавлен")
                
                self.load_and_display_data()
                client_window.destroy()
            except ValueError as e:
                messagebox.showerror("Ошибка ввода", str(e))

        tk.Button(client_window, text="Сохранить", command=save_client).pack(pady=5)
        tk.Button(client_window, text="Отмена", command=client_window.destroy).pack(pady=5)

    
    def add_vehicle(self):
        self._open_vehicle_window("Добавить транспортное средство")

    
    def edit_vehicle(self, event):
        selected_index = self.vehicles_listbox.curselection()
        if selected_index:
           vehicle = self.transport_company.vehicles[selected_index[0]]
           self._open_vehicle_window("Редактировать транспортное средство", vehicle)

    
    def _open_vehicle_window(self, title, vehicle=None):
        self.status_bar.config(text=f"{title}...")
        vehicle_window = tk.Toplevel(self.root)
        vehicle_window.title(title)
        
        tk.Label(vehicle_window, text="Тип транспорта").pack(pady=5)
        vehicle_type_var = tk.StringVar()
        vehicle_type_var.set("Грузовик" if isinstance(vehicle, Truck) else "Поезд" if vehicle else "Грузовик")
        tk.OptionMenu(vehicle_window, vehicle_type_var, "Грузовик", "Поезд").pack(pady=5)

        tk.Label(vehicle_window, text="Грузоподъемность (в кг)").pack(pady=5)
        capacity_entry = tk.Entry(vehicle_window)
        if vehicle:
            capacity_entry.insert(0, vehicle.capacity)
        capacity_entry.pack(pady=5)

        if isinstance(vehicle, Truck):
             tk.Label(vehicle_window, text="Цвет").pack(pady=5)
             color_entry = tk.Entry(vehicle_window)
             color_entry.insert(0, vehicle.color)
             color_entry.pack(pady=5)
        elif isinstance(vehicle, Train):
            tk.Label(vehicle_window, text="Количество вагонов").pack(pady=5)
            number_of_cars_entry = tk.Entry(vehicle_window)
            number_of_cars_entry.insert(0, vehicle.number_of_cars)
            number_of_cars_entry.pack(pady=5)


        def save_vehicle():
            vehicle_type = vehicle_type_var.get()
            try:
                capacity = int(capacity_entry.get())
                if capacity <= 0 or capacity > 10000:
                    raise ValueError("Грузоподъемность должна быть положительным числом не более 10000 кг.")

                if vehicle_type == "Грузовик":
                    if vehicle is None:
                        color = simpledialog.askstring("Цвет грузовика", "Введите цвет грузовика")
                        if not color or not color.isalpha():
                            raise ValueError("Цвет грузовика не может быть числом")
                        vehicle_obj = Truck(capacity, color)
                    else:
                        color = color_entry.get()
                        vehicle.capacity = capacity
                        vehicle.color = color
                        vehicle_obj = vehicle
                elif vehicle_type == "Поезд":
                    if vehicle is None:
                        number_of_cars = simpledialog.askinteger("Количество вагонов", "Введите количество вагонов")
                        if number_of_cars <= 0:
                            raise ValueError("Количество вагонов должно быть положительным целым числом")
                        vehicle_obj = Train(capacity, number_of_cars)
                    else:
                         number_of_cars = int(number_of_cars_entry.get())
                         vehicle.capacity = capacity
                         vehicle.number_of_cars = number_of_cars
                         vehicle_obj = vehicle
                
                if not vehicle:
                    self.transport_company.add_vehicle(vehicle_obj)
                    self.status_bar.config(text="Транспортное средство добавлено")
                else:
                    self.status_bar.config(text="Транспортное средство обновлено")
                
                self.load_and_display_data()
                vehicle_window.destroy()

            except ValueError as e:
                messagebox.showerror("Ошибка ввода", str(e))

        tk.Button(vehicle_window, text="Сохранить", command=save_vehicle).pack(pady=5)
        tk.Button(vehicle_window, text="Отмена", command=vehicle_window.destroy).pack(pady=5)

    
    def delete_client(self):
         selected_client_index = self.clients_listbox.curselection()
         if selected_client_index:
            del self.transport_company.clients[selected_client_index[0]]
            self.load_and_display_data()
            self.status_bar.config(text="Клиент удален")
         else:
            messagebox.showwarning("Удаление клиента", "Выберите клиента для удаления")

    
    def delete_vehicle(self):
        selected_vehicle_index = self.vehicles_listbox.curselection()
        if selected_vehicle_index:
            del self.transport_company.vehicles[selected_vehicle_index[0]]
            self.load_and_display_data()
            self.status_bar.config(text="Транспортное средство удалено")
        else:
            messagebox.showwarning("Удаление транспорта", "Выберите транспортное средство для удаления")

  
    def export_result(self):
         filepath = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
         if filepath:
            with open(filepath, "w") as f:
                f.write("Список клиентов:\n")
                for client in self.transport_company.clients:
                     f.write(f"{client}\n")
                f.write("\nСписок транспортных средств:\n")
                for vehicle in self.transport_company.vehicles:
                     f.write(f"{vehicle}\n")
            self.status_bar.config(text="Результаты экспортированы")

    def show_about(self):
        messagebox.showinfo("О программе", "Лабораторная работа 12\nВариант: 1\nФИО: Абалуева Анастасия Олеговна")

if __name__ == "__main__":
    root = tk.Tk()
    app = TransportApp(root)
    root.mainloop()
