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
            if new_coord == self.coords[-1]:
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
                    # print(f'new_coord: {new_coord}')
                    return new_coord
        return self.start_point

    def create_line(self):
        """
        Creates a list of coordinates of coastline
        """

        print(f'I am on 65 line: self.coords {self.coords}')
        i=1
        while self.get_new_coords(bypass=self.bypasses[0]) != self.start_point:
            self.coords += [self.get_new_coords(bypass=self.bypasses[0])]
            # print(f'Number of itter: {i}, прибавляем координаты: {self.coords[-1]}, bp: против час')
            i+=1
        # self.coords += [self.get_new_coords(bypass=self.bypasses[1])]
        self.coords.reverse()
        print(f'I am on 72 line: self.coords {self.coords}')
        while self.get_new_coords(bypass=self.bypasses[1]) != self.start_point:
            self.coords += [self.get_new_coords(bypass=self.bypasses[1])]
            # print(f'Number of itter: {i}, последняя координата: {self.coords[-1]},  bp: по час')
            i += 1


class BrokenLine:
    step = 0
    start_point = []
    cords = []

    def __init__(self, step, start_point, cords):
        self.step = step
        self.start_point = start_point
        self.cords = cords

    def create_line(self, cords):
        """
        Creates a list of coordinates of vertices of broken line of coastline
        @param cords: list of coastline coordinates
        """
        def add_new_cord(line: BrokenLine, previous_cord, start_cord, coords):
            epsilon = 1000000
            end_cord = [0, 0]
            for c in coords:
                d = ((start_cord[0] - c[0]) ** 2 + (start_cord[1] - c[1]) ** 2) ** 0.5
                delta = int(d) - line.step
                if epsilon ** 2 > delta ** 2 and previous_cord != [c[0], c[1]]:
                    epsilon = delta
                    end_cord = [c[0], c[1]]
            line.cords.append(end_cord)
            return start_cord, end_cord

        prev = self.start_point
        curr = self.start_point
        for _ in range(2):
            prev, curr = add_new_cord(self, prev, curr, cords)
        while ((curr[0] - self.start_point[0]) ** 2 + (curr[1] - self.start_point[1]) ** 2) >= self.step ** 2:
            prev, curr = add_new_cord(self, prev, curr, cords)

    def get_length(self):
        """
        Returns length of broken line
        """
        return self.step * len(self.cords)
