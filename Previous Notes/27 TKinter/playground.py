

# unlimited arguments
def add(n1, n2):
    return n1 + n2

# if you wanted to add 8 numbers it would error out

# the * gives the ability to have unlimited arguments args is commonly used but can be named anything
def add(*args):
    for n in range:
        print(n)
#unlimited positional arguments
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(1,2,8,12,2))

# keyword arguments or "kwargs"  requires 2 '*' this will turn everything into a dict
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # #or
    # print(kwargs["add"])

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
    # the result is 25. 2 + 3 = 5 and then 5 * 5= 25


calculate(2, add=3, multiply=5)

#with.get it doesnt error out if a keyword is not listed when called
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="honda", model="pilot")
print

