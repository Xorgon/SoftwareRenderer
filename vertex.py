import numpy as np


class Vertex(object):
    """
    Represents a vertex with a 2D array
    """
    def __init__(self, x=0, y=0, z=0, w=1):
        self.pos = np.array([x, y, z, w])

    def set_pos(self, pos):
        self.pos = pos
        return self

    @property
    def x(self):
        return self.pos[0]

    @property
    def y(self):
        return self.pos[1]

    @property
    def z(self):
        return self.pos[2]

    @property
    def w(self):
        return self.pos[3]

    # Transform vertex using matrix
    def transform(self, matrix):
        return Vertex().set_pos(matrix.transform(self.pos))

    # Perspective divide vertex
    def perspective_divide(self):
        return Vertex().set_pos([self.x/self.w, self.y/self.w, self.z/self.w, self.w])

    # Calculate triangle area
    def triangle_area(self, max_y_vert, mid_y_vert):
        x1 = max_y_vert.x - self.x
        y1 = max_y_vert.y - self.y

        x2 = mid_y_vert.x - self.x
        y2 = mid_y_vert.y - self.y

        return (x1 * y2 - x2 * y1) / 2

    # Calculate triangle normal
    def triangle_normal(self, v2, v3):

        s1 = self.pos - v2.pos
        s2 = self.pos - v3.pos

        s1 = np.array([s1[0], s1[1], s1[2]])
        s2 = np.array([s2[0], s2[1], s2[2]])

        return np.cross(s1, s2) / np.absolute(np.cross(s1, s2)).max()