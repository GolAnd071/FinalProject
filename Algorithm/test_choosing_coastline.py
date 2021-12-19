import unittest
from random import randint
import choosing_coastline as cc


class Test_choosing_coastline(unittest.TestCase):
    def setUp(self):
        def make_array(n):
            arr = []
            for _ in range(n):
                r = []
                for __ in range(n):
                    r.append(randint(0, 1))
                arr.append(r)
            arr[0][0] = 0
            print(arr)
            return arr

        self.maps = []
        self.coastlines = []
        self.brokenlines = []
        for i in range(20):
            self.maps.append(make_array(3))
            cstln = cc.Coastline((0, 0), 3, self.maps[i])
            print(i, ' Coastline created\n')
            print(i, ' Coastline line started crating')
            cstln.create_line()
            print(f'cstln.coords:{cstln.coords}')
            print(i, ' Coastline line created\n')
            print(i, ' BrokenLine started crating')
            brln = cc.BrokenLine(randint(1, 3), cstln.coords)
            print(i, ' BrokenLine created\n')
            print(i + 1, ' Coastline started crating')
            self.coastlines.append(cstln)
            self.brokenlines.append(brln)
        for i in range(20):
            self.maps.append(make_array(10))
            cstln = cc.Coastline((0, 0), 10, self.maps[i])
            print(i + 20, ' Coastline created\n')
            print(i + 20, ' Coastline line started crating')
            cstln.create_line()
            print(i + 20, ' Coastline line created\n')
            print(i + 20, ' BrokenLine started crating')
            brln = cc.BrokenLine(randint(1, 10), cstln.coords)
            print(i + 20, ' BrokenLine created\n')
            print(i + 21, ' Coastline started crating')
            self.coastlines.append(cstln)
            self.brokenlines.append(brln)

    def test_create_line(self):
        for i in range(len(self.brokenlines)):
            self.brokenlines[i].create_line()
            print(i, ' BrokenLine line created\n')

    def test_get_lenght(self):
        for i in range(len(self.brokenlines)):
            self.brokenlines[i].get_length()
            print(i, ' BrokenLine lenght had got\n')


if __name__ == '__main__':
    unittest.main()
