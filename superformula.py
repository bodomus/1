import math


class SuperFormula:
    """ superformula class """
    def __init__(self, m=0, a=0, b=0, n1=0, n2=0, n3=0):
        self.m = m
        self.a = a
        self.b = b
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.radius = 0
        self.lst = []

    def get_radius(self):
        for fi in xrange(0, 360, 1):
            rad_fi = math.radians(fi)
            f1 = (math.fabs((math.cos(self.m * rad_fi / 4.0)) / self.a)) ** self.n2
            f2 = (math.fabs((math.sin(self.m * rad_fi / 4.0)) / self.b)) ** self.n3
            self.radius = (f1 + f2) ** (-1 / self.n1)
            t = (fi, self.radius)
            self.lst.append(t)

    def calc_points(self):
        points = []
        for item in self.lst:
            fi = item[0]
            r = item[1]
            x = r * math.cos(math.radians(fi))
            y = r * math.sin(math.radians(fi))
            points.append((x, y))
        return points
