import math

class Calculator:

    def __init__(self):
        pass

    def add(self, a, b):
        res = float(a) + float(b)
        return res

    def subtract(self, a, b):
        res = float(b) - float(a)
        return res

    def multiply(self, a, b):
        return float(a) * float(b)

    def divide(self, a, b):
        return float(b) / float(a)

    def square(self, a):
        return float(a) * float(a)
