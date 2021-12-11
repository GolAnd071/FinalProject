coastline = []

start_coords = 0,0

def get_neighborhood_area(pix, y, x):
    neighborhood_area = [[pix[y+1, x-1], pix[y+1, x], pix[y+1, x+1]],
                         [pix[y, x-1], pix[y, x], pix[y, x+1]],
                         [pix[y-1, x-1], pix[y-1, x], pix[y+1, x+1]]]
    return neighborhood_area


def choosing_next_board_pixel(neighbor_area, previos_coords):
    for i in range(3):
        for j in range(3):
            if (i,j) != previos_coords and neighbor_area[i,j] == 0 and checking_if_border(i,j):
                return i,j

def checking_if_border(neighbor_area):
    coords = [(0,1), (0,1), (2, 1), (1, 2)] # neighbor pixels in area
    for c in coords:
        if neighbor_area[c] == 1: #cheking if pixel is water pixel
            return True
    return False

coastline[]


class Coastline:
    def __init__(self, step):
        self.step = step
        self.coords = []

    def get_previos_coords(self):
        return self.coords[-2]

    def get_next_neighborhood_area(self, pix):
        y, x = self.coords[-1]
        neighborhood_area = [[pix[y + 1, x - 1], pix[y + 1, x], pix[y + 1, x + 1]],
                             [pix[y, x - 1], pix[y, x], pix[y, x + 1]],
                             [pix[y - 1, x - 1], pix[y - 1, x], pix[y + 1, x + 1]]]
        return neighborhood_area

    def get_next_coords(neighbor_area, previos_coords):
        neighbor_area = self.get_next_neighborhood_area()
        for i in range(3):
            for j in range(3):
                if (i, j) != previos_coords and neighbor_area[i, j] == 0 and checking_if_border(i, j):
                    return i, j

    def move(self):

        self.x += self.vx
        self.y -= self.vy
        if (self.y >= HEIGHT-self.r - 1) or (self.y <= 10): self.vy = -self.vy
        if (self.x >= WIDTH-self.r - 1) or (self.x <= 10): self.vx = -self.vx

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )
        pygame.draw.circle(self.screen, BLACK, (self.x, self.y), self.r, 1)

coastline = Coastline(step=10)
coastline.get_next_coords() coastline.coords