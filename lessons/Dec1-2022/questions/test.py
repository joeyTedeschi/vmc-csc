class Car:
    type = ''
    colour = ''
    tire_size = 24
    max_speed = '200km'
    fuel = 100

    # def __init__(self, type, colour, tireSize, maxSpeed, fuel):
    #     self.type = type
    #     self.colour = colour
    #     self.tireSize = tireSize
    #     self.maxSpeed = maxSpeed
    #     self.fuel = fuel


honda = Car()
toyota = Car()

honda.type = 'Honda'
honda.colour = 'black'
honda.max_speed = '180km'

toyota.type = 'Toyota'
toyota.colour = 'red'
toyota.max_speed = '160km'

print(
    f'This is my {honda.type}, it is a {honda.colour} car with a max speed of {honda.max_speed}')
print(
    f'This is my {toyota.type}, it is a {toyota.colour} car with a max speed of {toyota.max_speed}')


class Room:
    length = 0.0
    width = 0.0

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def print_area(self):
        print(f'Area of room is: {self.length * self.width}')


living_room = Room(20, 9.5)
living_room.print_area()
