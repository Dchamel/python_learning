class House():
    """House Description"""

    def __init__(self, street, number):
        """House Location"""
        self.street = street
        self.number = number
        self.age = 0

    def build(self):
        """House Building"""
        print('House at ' + self.street + ' street with number ' + str(self.number) + ' created Successfully')

    def houseAge(self, year):
        """House Age"""
        self.age += year


class WoodHouse(House):
    """House made of Wood"""

    def __init__(self, prospekt, number):
        super().__init__(self, number)
        self.prospekt = prospekt


House1 = House('Moskva', 20)
House2 = House('Moskva', 21)
print(House1.street + ' ' + str(House1.number))

House1.build()
print(House1.age)
House1.houseAge(5)
print(House1.age)

WdHouse = WoodHouse('Lenina', 34)
print(WdHouse.prospekt)
