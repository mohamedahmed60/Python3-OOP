class Car:
    def __init__(self,speed):
        self.speed = speed



    def speed_up(self,extra_speed):
        self.speed ++ extra_speed


    def __add__(self,other):
        return self.speed + other


    def __radd__(self,other):
        return self.speed + other


    def __sub__(self,other):
        return self.speed - other


    def __rsub__(self,other):
        return other - self.speed


bmw = Car(200)
tyota = Car(120)

print( 20 - bmw)
