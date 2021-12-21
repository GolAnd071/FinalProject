import unittest
from random import randint
import Algorithm as cc


class AlgorithmTests(unittest.TestCase):
    def setUp(self):
        def make_array(n):
            arr = []
            for _ in range(n):
                r = []
                for __ in range(n):
                    r.append(randint(0, 1))
                arr.append(r)
            arr[0][0] = 0
            for i in range(n):
                print(arr[i])
            return arr

        self.maps = []
        self.coastlines = []
        self.brokenlines = []
        # for i in range(20):
        #     self.maps.append(make_array(3))
        #     cstln = cc.Coastline((0, 0), 3, self.maps[i])
        #     print(i, ' Coastline created\n')
        #     print(i, ' Coastline line started crating')
        #     print('Coastline cords: ', cstln.get_coastline())
        #     print(i, ' Coastline line created\n')
        #     print(i, ' BrokenLine started crating')
        #     brln = cc.BrokenLine(randint(1, 3), cstln.get_coastline())
        #     print(i, ' BrokenLine created\n')
        #     print(i, ' BrokenLine line started creating')
        #     brln.create_line()
        #     print('BrokenLine vertices: ', brln.vertices)
        #     print(i, ' BrokenLine line created')
        #     print(i, ' BrokenLine step: ', brln.step)
        #     print(i, ' BrokenLine lenght: ', brln.get_length(), '\n')
        #     print(i + 1, ' Coastline started crating')
        #     self.coastlines.  append(cstln)
        #     self.brokenlines.append(brln)
        for i in range(20):
            self.maps.append(make_array(10))
            cstln = cc.Coastline((0, 0), 10, self.maps[i])
            print(i + 20, ' Coastline created\n')
            print(i + 20, ' Coastline line started crating')
            cstln.create_coastline()
            print('Coastline cords: ', cstln.coords)
            print(i + 20, ' Coastline line created\n')
            print(i + 20, ' BrokenLine started crating')
            brln = cc.BrokenLine(randint(1, 10), cstln.coords)
            print(i + 20, ' BrokenLine created\n')
            print(i + 20, ' BrokenLine line started creating')
            brln.create_line()
            print('BrokenLine vertices: ', brln.vertices)
            print(i + 20, ' BrokenLine line created')
            print(i + 20, ' BrokenLine step: ', brln.step)
            print(i + 20, ' BrokenLine lenght: ', brln.get_length(), '\n')
            print(i + 21, ' Coastline started crating')
            self.coastlines.append(cstln)
            self.brokenlines.append(brln)

    def test_pass(self):
        pass


if __name__ == '__main__':
    unittest.main()
