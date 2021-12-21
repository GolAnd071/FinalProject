import queue

def check_if_go_out_of_array(coords, array_size):
    """ Checking if we've gone out array """

    for c in coords:
        if c > array_size - 1 or c < 0:
            return True
    return False


class Coastline:
    shifts = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    finish_point = (-3, -3)

    # TODO: check if algo depends on bypass direction (shifts order)
    # TODO: replace tuples array by numpy array

    def __init__(self, start_point, data_size, data):
        self.coords = [start_point]  # include coastline coords in all lines (with dead end lines)
        self.start_point = start_point
        self.data = data
        self.data_size = data_size

    def check_if_point_is_border(self, coord: tuple):
        """ Checking if there are water bordering pixels in area """
        data = self.data
        y, x = coord
        for i in range(-1, 2):
            for j in range(-1, 2):
                neighbor_coord = y + i, x + j
                if not check_if_go_out_of_array(neighbor_coord, self.data_size):
                    if abs(data[y + i][x + j]) == 1:
                        return True
        return False

    def check_if_came_back(self, new_coord):
        """ Checking if we were here (in any line) """
        if new_coord in self.coords:
            return True
        else:
            return False

    def get_next_coords(self, curr_coord) -> list:
        next_coords = []
        y, x = curr_coord
        for i, j in self.shifts:
            next_coord = y + i, x + j
            if not check_if_go_out_of_array(next_coord, self.data_size):
                if not self.check_if_came_back(next_coord) and \
                        self.data[y + i][x + j] == 0 and \
                        self.check_if_point_is_border(coord=next_coord):
                    next_coords += [next_coord]
        if next_coords:
            return next_coords
        else:
            return [self.finish_point]

    def start_choosing_line(self, lines=None) -> list:
        """
        Note: real coastline has branches with dead ends.
        create_lines makes lines with no branching
        line is a list of coastline coordinates
        Remember: self.coords includes coordinates in all branches
        """
        # if_lines_has_equal_length = all(len(l) == len(lines[0]) for l in lines)


        lines = [[]]
        i = 0

        q = queue.LifoQueue()
        q.put(self.start_point)

        while not q.empty():
            current_coord = q.get()
            self.coords.append(current_coord)
            lines[i].append(current_coord)
            next_coords = self.get_next_coords(current_coord)
            if self.finish_point in next_coords:
                i += 1
            else:
                for j in range(len(next_coords) - 1):
                    lines.insert(i + j + 1, lines[i])
                for coord in next_coords:
                    q.put(coord)

        return lines

    def create_coastline(self):
        max_len = 0
        mainline = None
        for line in self.start_choosing_line():
            if len(line) >= max_len:
                max_len = len(line)
                mainline = line
        self.coords = mainline


class BrokenLine:
    def __init__(self, step, cords):
        self.step = step
        self.start_point = cords[0]
        self.vertices = [self.start_point]
        self.cords = cords
        self.line_created = False
        self.island = False

    def create_line(self):
        """ Creates a list of coordinates of vertices of broken line of coastline """

        def get_dists_range(first_point, second_point):
            dists = [(first_point[0] - second_point[0] - 0.5) ** 2 + (first_point[1] - second_point[1] - 0.5) ** 2,
                     (first_point[0] - second_point[0] - 0.5) ** 2 + (first_point[1] - second_point[1] + 0.5) ** 2,
                     (first_point[0] - second_point[0] + 0.5) ** 2 + (first_point[1] - second_point[1] - 0.5) ** 2,
                     (first_point[0] - second_point[0] + 0.5) ** 2 + (first_point[1] - second_point[1] + 0.5) ** 2]
            return min(dists), max(dists)

        def is_step_in_dist_range(first_point, second_point):
            min_dist, max_dist = get_dists_range(first_point, second_point)
            return min_dist <= self.step ** 2 <= max_dist

        cur = self.start_point
        for i in range(len(self.cords)):
            if is_step_in_dist_range(cur, self.cords[i]):
                self.vertices.append(self.cords[i])
                cur = self.cords[i]
        if is_step_in_dist_range(self.cords[0], self.cords[-1]):
            self.island = True
        self.line_created = True

    def get_length(self):
        """ Returns length of broken line """
        if self.line_created:
            if self.island:
                return self.step * len(self.vertices)
            else:
                return self.step * (len(self.vertices) - 1)
        return 0
