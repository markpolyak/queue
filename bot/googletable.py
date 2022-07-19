import gspread


# Класс, реализующий соединение с Google таблицей, открытие, чтенние и запись данных в таблице
class GoogleTable:

    # Конструктор класса
    def __init__(self, filename):
        self.spread = gspread.service_account(filename=filename)  # Соединение с Google таблицу
        self.sh = None  # Открытая таблица
        print("Вы подключились к Google таблицам.")

    # Деструктор класса
    def __del__(self):
        print("Вы отключились от Google таблиц.")

    # Открытие таблицы
    def open_table(self, name):
        self.sh = self.spread.open(name)

    # Чтение данных
    def read_data(self):
        # Словарь данных
        value_list = {"subject": self.sh.sheet1.col_values(1)[1:], "teacher": self.sh.sheet1.col_values(2)[1:],
                      "time": self.sh.sheet1.col_values(3)[1:], "students": self.sh.sheet1.col_values(4)[1:],
                      "priority": self.sh.sheet1.col_values(5)[1:]}
        return value_list

    # Запись студентов в очередь
    def write_students(self, row, data):
        self.sh.sheet1.update(f"D{row}", data)

    # Запись приоритетности в очередь
    def write_priority(self, row, data):
        self.sh.sheet1.update(f"E{row}", data)

    # Удаление очереди
    def delete_queue(self, row):
        self.sh.sheet1.update(f"A{row}", "")
        self.sh.sheet1.update(f"B{row}", "")
        self.sh.sheet1.update(f"C{row}", "")
        self.sh.sheet1.update(f"D{row}", "")
        self.sh.sheet1.update(f"E{row}", "")

    # Создание очереди
    def create_queue(self, subject, teacher, time, user, priority):
        row = len(self.sh.sheet1.col_values(1)) + 1  # Вычисление номера строки для записи
        self.sh.sheet1.update(f"A{row}", subject)
        self.sh.sheet1.update(f"B{row}", teacher)
        self.sh.sheet1.update(f"C{row}", time)
        self.sh.sheet1.update(f"D{row}", user["group"] + " " + user["name"])
        self.sh.sheet1.update(f"E{row}", priority)
