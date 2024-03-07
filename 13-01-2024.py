class car:
    def __init__(self, color, seats, brand):

        self.color = color
        self.seats = seats
        self.brand = brand

    def get_parameters(self):
        return [self.color, self.seats, self.brand]

car1 = car('blue', 5, 'Mahindra')
car2 = car('black', 7, 'Hero Honda')

print(car1.get_parameters())
print(car2.get_parameters())

car1.color = 'white'
car2.seats = 5
car2.brand = 'Mahindra'

print(car1.get_parameters())
print(car2.get_parameters())