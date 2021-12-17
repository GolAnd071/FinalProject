import unittest
from random import randint
import choosing_coastline as cc


def make_array(n):
    arr = []
    for _ in range(n):
        r = []
        for __ in range(n):
            r.append(randint(0, 1))
        arr.append(r)
    return arr


class Test_choosing_coastline(unittest.TestCase):
    def setUp(self):
        self.maps = []
        self.coastlines = []
        self.brokenlines = []
        for i in range(20):
            self.maps.append(make_array(3))
            cstln = cc.Coastline((0, 0), 0, self.maps[i])
            print(i, ' Coastline created')
            cstln.create_line()
            print(i, ' Coastline line created')
            brln = cc.BrokenLine(randint(1, 3), cstln.coords)
            print(i, ' BrokenLine created')
            self.coastlines.append(cstln)
            self.brokenlines.append(brln)
        for i in range(10):
            self.maps.append(make_array(10))
            cstln = cc.Coastline((0, 0), 0, self.maps[i + 20])
            print(i + 20, ' Coastline created')
            cstln.create_line()
            print(i + 20, ' Coastline line created')
            brln = cc.BrokenLine(randint(1, 10), cstln.coords)
            print(i + 20, ' BrokenLine created')
            self.coastlines.append(cstln)
            self.brokenlines.append(brln)

    def test_create_line(self):
        for i in range(len(self.brokenlines)):
            self.brokenlines[i].create_line()
            print(i, ' BrokenLine line created')

    def test_get_lenght(self):
        for i in range(len(self.brokenlines)):
            self.brokenlines[i].get_length()
            print(i, ' BrokenLine lenght had got')


if __name__ == '__main__':
    unittest.main()



#def main():
#    cstln = [(0, 5), (1, 4), (2, 4), (3, 3), (4, 2), (4, 1), (5, 2), (5, 3), (6, 4), (7, 4)]
#    line = BrokenLine(int(input()), cstln)
#    line.create_line()
#    print(line.vertices)


#if __name__ == '__main__':
#    main()
