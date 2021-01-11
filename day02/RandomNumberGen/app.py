import time


class Rng():
    def __init__(self, m, a, b, x):
        self.m = m
        self.a = a
        self.b = b
        self.x = x

    def gen(self, n):
        liste = []
        for i in range(n):
            timestamp = int(time.time() % 15)
            self.x = (self.a * self.x + self.b) * timestamp
            self.x = self.x % n

        return self.x


class creature():
    def __init__(self, blood_colour, eyes_colour):
        self.blood_colour = blood_colour
        self.eyes_colour = eyes_colour
        self.hunger = 0
        self.damage = 100
        self.health = 1000

    def health_setter(self, value):
        self.health = value

    def health_getter(self):
        return self.health

    def eat(self, food_value):
        self.hunger = self.hunger + food_value

    def walk(self, steps):
        self.hunger = self.hunger - steps / 10

    def attack(self, object):
        object.health_setter(object.health_getter() - self.damage)


rng1 = Rng(7, 5, 8, 13)

print(rng1.gen(100))
print(int(time.time()))
