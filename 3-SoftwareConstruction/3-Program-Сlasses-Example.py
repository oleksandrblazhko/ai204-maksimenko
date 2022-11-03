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


class Loc:
    def __init__(self):
        self.x = random.randint(-2070, 2070)


class Location:
    def __init__(self, xCoord, yCoord):
        self.consumer_location = consumer_location
        self.xCoord = xCoord
        self.yCoord = yCoord

    def location_sharing(self):
        xCoord = Loc()
        self.xCoord = xCoord
        yCoord = Loc()
        self.yCoord = yCoord
        return print(self.consumer_location, self.xCoord, self.yCoord)


class Obj:
    def __init__(self):
        self.x = random.randint(0, 100)


class Environment:
    def __init__(self, air_quality, temperature):
        self.air_quality = air_quality
        self.temperature = temperature

    def info_air(self):
        self.air_quality = Obj()
        return self.air_quality

    def info_temperature(self):
        self.temperature = Obj()
        return self.temperature

    def information_sharing(self):
        return print(self.consumer_location)

    def send_info(self):
        return print(
            "AIR: " + self.air_quality + "% " + "Temperature: " + self.temperature + "% on " + self.consumer_location)


class Map:
    def __init__(self, name_of_the_institution, rating):
        self.name_of_the_institution = name_of_the_institution
        self.rating = rating

    def galleries_find(self):
        self.name_of_the_institution = "Random"
        self.rating = random.randint(1, 5)
        return self.name_of_the_institution, self.rating

    def send_result(self):
        return print(
            "Назва Галереї" + self.name_of_the_institution + "Рейтинг Галереї" + self.rating)
