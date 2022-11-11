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

