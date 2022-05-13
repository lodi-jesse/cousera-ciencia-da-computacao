class Triangulo:

    def __init__(self, a, b, c):
        self.t2 = None
        self.a = a
        self.b = b
        self.c = c

    def getTriangulo(self):
        lista = [self.a, self.b, self.c]
        lista = sorted(lista)
        return lista

    def semelhante(self, t2):
        newLista = []
        self.t2 = t2.getTriangulo()
        for i in t2.getTriangulo():
            newLista.append(i / 2)

        if newLista == t1.getTriangulo():
            return True
        else:
            return False


