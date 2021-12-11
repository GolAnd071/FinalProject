start_coords = 0,0

def checking_if_border(neighbor_area):
    coords = [(0,1), (0,1), (2, 1), (1, 2)] # neighbor pixels in area
    for c in coords:
        if neighbor_area[c] == 1: #cheking if pixel is water pixel
            return True
    return False


class Coastline:
    def __init__(self):
        self.coords = []

    def get_previos_coords(self):
        return self.coords[-2]

    def get_current_coords(self):
        return self.coords[-1]

    def get_next_neighborhood_area(self, pix):
        y, x = self.get_current_coords()
        neighborhood_area = [[pix[y + 1, x - 1], pix[y + 1, x], pix[y + 1, x + 1]],
                             [pix[y, x - 1], pix[y, x], pix[y, x + 1]],
                             [pix[y - 1, x - 1], pix[y - 1, x], pix[y + 1, x + 1]]]
        return neighborhood_area

    def get_next_coords(self):
        next_neighbor_area = self.get_next_neighborhood_area()
        previos_coords = self.get_previos_coords()
        x,y = current_coords = self.get_current_coords()
        for i in range(3):
            for j in range(3):
                if (i, j) not in (previos_coords, current_coords) and next_neighbor_area[i, j] == 0 and checking_if_border(i, j):
                    return y+i, x+j

coastline = Coastline()

def make_mask_with_coastline(color):
    for i in range(pix_size):
        for
pix = [[0, 1, 0, 0, 1],
       [0, 1, 1, 0, 0
       []]