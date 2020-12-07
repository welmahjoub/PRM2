class Commune:
    def __init__(self, code: str, name: str, code_postal: str, latitude: float, longitude: float):
        self.code = code
        self.code_postal = code_postal
        self.name = name.lower()
        self.latitude = latitude
        self.longitude = longitude
        self.score = 0

    def __str__(self):
        return self.code + "," + self.code_postal + ","+ self.name + "," + str(self.latitude) + "," + str(self.longitude) + "," + str(self.score)
