# TODO: load pix massive from another module # We don't need to load it, we will create an object of this class in module, where pix massive is - GolAnd071
import numpy as np

def checking_if_border(neighbor_area: np.array):
    '''Cheking if there are water bordering pixels in area'''
    coords = [(0,1), (0,1), (2, 1), (1, 2)] # [(0, 1), (1, 0), (1, 2), (2, 1)] - GolAnd071
    for c in coords:
        if neighbor_area[c] == 1: #cheking if pixel is water pixel
            return True
    return False


class Coastline:
    def __init__(self):
        self.coords = []

    def get_next_neighborhood_area(self, pix: np.array) -> np.array:
        # TODO: checking if next_neighborhood_area go beyond the pix
        y, x = self.coords[-1]
        neighborhood_area = [[pix[y + 1, x - 1], pix[y + 1, x], pix[y + 1, x + 1]],
                             [pix[y, x - 1], pix[y, x], pix[y, x + 1]],
                             [pix[y - 1, x - 1], pix[y - 1, x], pix[y + 1, x + 1]]]
        return neighborhood_area

    def get_next_coords(self) -> tuple:
        # TODO: checking if next_coords go beyond the pix
        x,y = self.coords[-1]
        for i in range(3):
            for j in range(3):
                if (i, j) not in (self.coords[-2], self.coords[-1]) and next_neighbor_area[i, j] == 0 and checking_if_border(i, j):
                    return y+i, x+j

    #TODO: add function choose_first_coords or choose_first_point

coastline = Coastline()

# TODO: get all coastline.coords using cycle

# TODO: add function make_mask_with_coastline
# def make_mask_with_coastline(color):
#     for i in range(pix_size):
#         for
# pix = [[0, 1, 0, 0, 1],
#        [0, 1, 1, 0, 0
#        []]
