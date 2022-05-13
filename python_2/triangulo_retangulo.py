class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def retangulo(self):
        if self.a > self.b and self.a > self.c:
            h = self.a ** 2
            c = self.b ** 2 + self.c ** 2
            if h == c:
                return True
            else:
                return False
        elif self.b > self.a and self.b > self.c:
            h = self.b ** 2
            c = self.a ** 2 + self.c ** 2
            if h == c:
                return True
            else:
                return False
        elif self.c > self.a and self.c > self.b:
            h = self.c ** 2
            c = self.b ** 2 + self.a ** 2
            if h == c:
                return True
            else:
                return False

        else:
            return False


t = Triangulo(3, 3, 3)
print(t.retangulo())
