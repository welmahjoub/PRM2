class Commune:
    def __init__(self, code, name: str, latitude, longitude):
        self.code = code
        self.name = name.lower()
        self.latitude = latitude
        self.longitude = longitude
        self.score = 0

    def __str__(self):
        return " code : " + self.code + " name : " + self.name + \
               " lat : " + str(self.latitude) + " long : " + str(self.longitude) + " score : " + str(self.score)

    def __hash__(self):
        return hash(('name', self.name))

    def __eq__(self, other):
        if not isinstance(other, Commune):
            return NotImplemented

        return self.name == other.name or self.code == other.code