import math

class Complex:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag


    def __add__(self, other):
        return self.__class__(self.real + other.real, self.imag + other.imag)


    def __bool__(self):
        return bool(abs(self))


    def __abs__(self):
        return math.hypot(self.real, self.imag)


    def congugate(self):
        return self.__class__(self.real , -self.imag)

    
    def phase(self):
        r = math.hypot(self.real, self.imag)
        theta = math.atan2(self.imag, self.real)
        return r, theta


    def __str__(self):
        if self.imag > 0:
            return f"{self.real}+{self.imag}i"
        return f"{self.real}{self.imag}i"


    # for developer
    def __repr__(self): # b jaye __str__ in gozine behtari hast
        return f"{self.__class__.__name__}({self.real}, {self.imag})" # karbord baraye debug


    def __mull__(self, other):
        return self.__class__(self.real * other, self.imag * other)


c1 = Complex(1, 1)
print(c1.phase())
print(math.sqrt(2), math.pi / 4)



print(bool(1))

if c1:
    print("c1")


c2 = Complex(1, 2)
print(c2)

c3 = Complex(1, -3)
print(c3)