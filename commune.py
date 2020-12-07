class Commune:
    def __init__(self, code, name, latitude, longitude):
        self.code = code
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.mesure = 0

    def __str__(self):
        return " code : " + self.code + " name : " + self.name + " lat : " + str(self.latitude) + " long : " + str(self.longitude)
