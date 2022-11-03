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
