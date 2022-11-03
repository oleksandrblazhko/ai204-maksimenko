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
