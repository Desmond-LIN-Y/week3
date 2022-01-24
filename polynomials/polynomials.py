from numbers import Number
from numbers import Integral

from black import re


class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Number):
            return Polynomial((self.coefficients[0]-other,) + self.coefficients[1:])
        elif isinstance(other, Polynomial):
            if len(self.coefficients)>len(other.coefficients):
                other.coefficients += tuple([0*a for a in range(len(self.coefficients)-len(other.coefficients))])
                coefs = tuple(a - b for a, b in zip(self.coefficients, other.coefficients))

            # Append the high degree coefficients from the higher degree
            # summand.
                return Polynomial(coefs)
            else:
                self.coefficients += tuple([0*a for a in range(len(other.coefficients)-len(self.coefficients))])
                coefs = tuple(a - b for a, b in zip(self.coefficients, other.coefficients))

            # Append the high degree coefficients from the higher degree
            # summand.
                return Polynomial(coefs)
        else:
            return(NotImplemented)
    
    def __rsub__(self, other):
        return (self - other) * (-1)

    def __mul__(self, other):

        if isinstance(other, Number):
            coefs = tuple(i * other for i in self.coefficients)
            return Polynomial(coefs)
        
        elif isinstance(other, Polynomial):
            coefs = [0] * (self.degree() + other.degree() + 1) 
            for i in range(self.degree()+1):
                for j in range(other.degree()+1):
                    coefs[i+j] += self.coefficients[i] * other.coefficients[j]

            return Polynomial(tuple(coefs))
        
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __call__(self, number):
        if isinstance(number, Number):
            sum = 0
            for i in range(self.degree()+1):
                sum += self.coefficients[i] * pow(number, i)
            
            return sum
        
        else:
            return NotImplemented

    def __pow__(self, int):
        if isinstance(int, Integral):
            coefs = Polynomial((1,))
            for i in range(int):
                coefs = coefs * self
            return coefs
        else:
            return NotImplemented

    def dx(self):
        coefs=[]
        if self.degree() == 0:
            return Polynomial((0,))
        for i in range(1, self.degree()+1): 
            coefs.append((i) * self.coefficients[i])
        return Polynomial(tuple(coefs))

def derivative(poly):
    return poly.dx()



