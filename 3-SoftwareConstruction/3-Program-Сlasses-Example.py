# Створення об'єктного типу (клас) Consumer
class Consumer:
    def __init__(self, name, surname, consumer_id, email):
        self.name = name
        self.surname = surname
        self.consumer_id = consumer_id
        self.email = email

    def info_consumer(self):
        self.name = input("Введіть своє ім'я: ")
        self.surname = input("Введіть своє прізвище: ")
        self.email = input("Введіть свою пошту: ")
        return self.name, self.surname, self.email


# Створення об'єктного типу (клас) Loc
class Loc:
    def __init__(self):
        # Координати
        self.x = random.randint(-2070, 2070)

class Area:
    def __init__(self):
        # Радіус пошуку
        self.x = random.randint(1, 5)


# Створення об'єктного типу (клас) Location
class Location:
    def __init__(self, xCoord, yCoord, area):
        self.consumer_location = consumer_location
        self.xCoord = xCoord  # позиция по плоскости х
        self.yCoord = yCoord  # позиция по плоскости y
        self.area = area  # радіус пошуку

    def location_sharing(self):
        xCoord = Loc()
        self.xCoord = xCoord
        yCoord = Loc()
        self.yCoord = yCoord
        area = Area()
        self.area = area
        if self.xCoord == "":
            print("Результат = -1")
        elif self.area == "":
            print("Результат = -2")
        elif 1 > self.area > 5:
            print("Результат = -2")
        elif self.yCoord == "" and self.area == "":
            print("Результат = -3")
        else:
            return print("Результат = 1;", xCoord, yCoord, area)


# Створення об'єктного типу (клас) Obj
class Obj:
    def __init__(self):
        # Якість повітря та температура
        self.x = random.randint(0, 100)


# Створення об'єктного типу (клас) Environment
class Environment:
    def __init__(self, air_quality, temperature):
        self.air_quality = air_quality  # якість повітря
        self.temperature = temperature  # температура повітря

    # Пошук інформації про якість повітря
    def info_air(self):
        self.air_quality = Obj()
        return self.air_quality

    # Пошук інформації про температуру повітря
    def info_temperature(self):
        self.temperature = Obj()
        return self.temperature

    # Місцезнаходження користувача
    def information_sharing(self):
        return print(self.consumer_location)

    # Відправка загальної інформації про якість повітря та температуру поітря за місцезнаходженням користувача
    def send_info(self):
        return print(
            "AIR: " + self.air_quality + "% " + "Temperature: " + self.temperature + "% on " + self.consumer_location)


# Створення об'єктного типу (клас) Map
class Map:
    def __init__(self, name_of_the_institution, rating):
        self.name_of_the_institution = name_of_the_institution
        self.rating = rating

# Пошук найближчих галерей
    def galleries_find(self):
        self.name_of_the_institution = "Random"
        self.rating = random.randint(1, 5)
        return self.name_of_the_institution, self.rating

# Відправка інформації про найближчі галереї
    def send_result(self):
        return print(
            "Назва Галереї" + self.name_of_the_institution + "Рейтинг Галереї" + self.rating)
