class Circle:
    """An implementation of circle"""
    def __init__(self, coords, R):
        self.coords = coords
        self.radius = R

    def __contains__(self, point):
        dis = (point[0] - self.coords[0])**2 + (point[1] - self.coords[1])**2
        if dis < self.radius **2:
            return True
        else:
            return False