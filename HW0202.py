#10.1
class Thing():
    pass
print(Thing)

example=Thing()
print(example)

#10.2
class Thing2():
    letters='abc'

print(Thing2.letters)

#10.3

class Thing3:
    def __int__(self):
        self.letters ='xyz'

        print(thing3.letters)

        something = Thing3()
        print(something.letters)
#10.4
class Element:
    def __init__(selfs, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

        hydrogen = Element('Hydrogen', 'H', 1)
        print(hydrogen)

# #10.5
# el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number':1}
# hydrogen = Element(el_dict['name']), el_dict['symbol'], el_dict['number'])
# hydrogen = Element(**el_dict)

#10.6
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump(self):
        print('name=%s, symbol=%s, number=%s, number=%s' % (self.name, self.symbol, self.number))

#10.7

class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self):
        return('name=%s, symbol=%s, number=%s' % (self.name, self.symbol, self.number))

#10.8

class Element:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    @property
    def name(self):
        return self.__name
    @property
    def symbol(self):
        return self.__symbol
    @property
    def number(self):
        return self.__number

#10.9
class Bear:
    def eats(self):
        return 'berries'

class Rabbit:
    def eats(self):
        return 'clover'

class Octothorope:
    def eats(self):
        return 'campers'

b = Bear()
r = Rabbit()
o = Octothorope()
print(b.eats())
print(r.eats())
print(o.eats())

#10.10
class Laser:
    def does(self):
        return 'distintegrate'
class Claw:
    def does(self):
        return 'crush'
class SmartPhones:
    def does(self):
        return 'ring'
class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhones()
    def does(self):
        return '''I haver many attachment:
My laser, to %s,
My cla, to %s.
My smartphone, to %s.'''% (
            self.laser.does(),
            self.claw.deos(),
            self.smartphone.does())

