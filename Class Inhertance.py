class Parent:
    def print_last_name(self):
        print('Master')

class Child(Parent):
    def print_first_name(self):
        print('Humming')

    def print_last_name(self):   # This function will overwrite over the function from the Parent
        print('Masterrrrrr')

ghaith = Child()
ghaith.print_first_name()
ghaith.print_last_name()


class Mario:

    def move(self):
        print('I\'m moving')


class Mushroom:

    def eat_mushroom(self):
        print('I\'m big')


class BigMario(Mario, Mushroom):
    pass

bm = BigMario()
bm.move()
bm.eat_mushroom()
