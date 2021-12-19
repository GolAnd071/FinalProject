def check_if_go_out_of_array(coords, array_size):
    '''Cheking if we've reached array frames'''

    for c in coords:
        if c > array_size - 1 or c < 0:
            return True
    return False


class Coastline:
    counterclockwise_bypass = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    clockwise_bypass = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    bypasses = counterclockwise_bypass, clockwise_bypass
    # TODO: check if algo depends on bypass direction (shifts order)
    # TODO: replace tuples array by numpy array

    def __init__(self, start_point, data_size, data):
        self.coords = [start_point]
        self.start_point = start_point
        self.data = data
        self.data_size = data_size

    def check_if_point_is_border(self, coord: tuple):
        '''Cheking if there are water bordering pixels in area'''
        data = self.data
        y, x = coord
        for i in range(-1, 2):
            for j in range(-1, 2):
                neighbor_coord = y + i, x + j
                if not check_if_go_out_of_array(neighbor_coord, self.data_size) and neighbor_coord != coord:
                    if data[y + i][x + j] == 1:
                        return True
        return False

    def check_if_came_back(self, new_coord):
        if len(self.coords) <= 1:
            if new_coord == self.start_point:
                return True
            else:
                return False
        elif new_coord in (self.coords[-2], self.coords[-1]):
            return True
        else:
            return False

    def get_new_coords(self, bypass) -> tuple:
        y, x = self.coords[-1]
        for i, j in bypass:
            new_coord = y + i, x + j
            if not check_if_go_out_of_array(new_coord, self.data_size):
                if not self.check_if_came_back(new_coord) and \
                        self.data[y + i][x + j] == 0 and \
                        self.check_if_point_is_border(coord=new_coord):
                    return new_coord
        return self.start_point

    def create_line(self):
        """
        Creates a list of coordinates of coastline
        """
        while self.get_new_coords(bypass=self.bypasses[0]) != self.start_point:
            self.coords += [self.get_new_coords(bypass=self.bypasses[0])]
        self.coords.reverse()
        
        while self.get_new_coords(bypass=self.bypasses[1]) != self.start_point:
            self.coords += [self.get_new_coords(bypass=self.bypasses[1])]



class BrokenLine:
    def __init__(self, step, cords):
        self.step = step
        self.start_point = cords[0]
        self.vertices = [self.start_point]
        self.cords = cords

    def create_line(self):
        """
        Creates a list of coordinates of vertices of broken line of coastline
        @param cords: list of coastline coordinates
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
