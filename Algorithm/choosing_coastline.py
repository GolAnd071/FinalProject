# TODO: load pix massive from another module # We don't need to load it, we will create an object of this class in module, where pix massive is - GolAnd071


def check_if_border(neighbor_area):
    '''Cheking if there are water bordering pixels in area'''
    coords = [(0, 1), (1, 0), (1, 2), (2, 1)]
    for c in coords:
        if neighbor_area[c] == 1:  # cheking if pixel is water pixel
            return True
    return False


def check_if_reached_array_frames(coords, array_size):
    '''Cheking if we've reached array frames'''
    for c in coords:
        if c >= array_size - 1:
            return True
    return False


class Coastline:
    def __init__(self, start_point, data_size, data):
        self.coords = [start_point]
        self.start_point = start_point
        self.data = data
        self.data_size = data_size

    def get_next_neighborhood_area(self, center: tuple):
        data = self.data
        y, x = center
        neighborhood_area = [[data[y + 1, x - 1], data[y + 1, x], data[y + 1, x + 1]],
                             [data[y, x - 1], data[y, x], data[y, x + 1]],
                             [data[y - 1, x - 1], data[y - 1, x], data[y + 1, x + 1]]]
        return neighborhood_area

    def get_new_coords(self) -> tuple:
        y, x = self.coords[-1]
        next_neighbor_area = self.get_next_neighborhood_area(center=(y, x))
        for i in range(3):
            for j in range(3):
                if (i, j) not in (self.coords[-2], self.coords[-1]) and next_neighbor_area[
                    i, j] == 0 and check_if_border(i, j):
                    return y + i, x + j

    def create_line(self):
        """
        Creates a list of coordinates of coastline
        """
        while not check_if_reached_array_frames(self.coords[-1], self.data_size) or \
                self.coords[-1] == self.start_point:
            self.coords += [self.get_new_coords()]


class BrokenLine:
    def __init__(self, step, cords):
        self.step = step
        self.start_point = cords[0]
        self.vertices = [self.start_point]
        self.cords = cords

    def create_line(self):
        """
        Creates a list of coordinates of vertices of broken line of coastline
        """
        cur = self.start_point
        for i in range(len(self.cords)):
            dists = [((cur[0] - self.cords[i][0] - 0.5) ** 2 + (cur[0] - self.cords[i][0] - 0.5) ** 2) ** 0.5,
                     ((cur[0] - self.cords[i][0] - 0.5) ** 2 + (cur[0] - self.cords[i][0] + 0.5) ** 2) ** 0.5,
                     ((cur[0] - self.cords[i][0] + 0.5) ** 2 + (cur[0] - self.cords[i][0] - 0.5) ** 2) ** 0.5,
                     ((cur[0] - self.cords[i][0] + 0.5) ** 2 + (cur[0] - self.cords[i][0] + 0.5) ** 2) ** 0.5]
            if min(dists) <= self.step <= max(dists):
                self.vertices.append(self.cords[i])
                cur = self.cords[i]

    def get_length(self):
        """
        Returns length of broken line
        """
        return self.step * len(self.vertices)
