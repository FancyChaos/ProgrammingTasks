# parent class. classes that derive from this one inherit ripen() and is_ripe
class Fruit:

    # when instantiating this class, __init__ is called.
    # This sets is_ripe for the newly created object to False
    def __init__(self):
        self.is_ripe = False

    # because of the "self." this method only affects this particular instance
    def ripen(self):
        self.is_ripe = True


class Apple(Fruit):

    # it's possible to override a function from the parent class,
    # even __init__!
    def __init__(self, color):
        # this calls __init__() from Fruit. Otherwise Aplles wouldn't have the
        # is_ripe attribute
        super().__init__()
        self.color = color


class Grape(Fruit):

    # it's possible to override a function from the parent class,
    # even __init__. Grapes now don't have a is_ripe attribute!
    def __init__(self, variant):
        self.isRaisin = False
        self.variant = variant

    # it's possible to override a function from the parent class!
    def ripen(self):
        self.isRaisin = True


grannySmith = Apple("green")
gala = Apple("red")

grape = Grape("seedless")
grape.ripen()

print(f"One of my apples is {gala.color}, the other is {grannySmith.color}!")
if grape.isRaisin:
    print(f"My {grape.variant} grape is so old it turned into a raisin!")

print(gala.is_ripe)
