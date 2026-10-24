def add(*args):
    num = 0
    for arg in args:
        num +=arg
    return num

print(add(1,2,3,4))

def calculate(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key,value)


calculate(add = 3, multiply = 5)

class Car():
    def __init__(self,**kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
my_car= Car(make = "Nissan",)
print(my_car.model)

