from collections import deque

COLOR_MAP = {
    'B':'□', 
    'W':'■',
}


class Pixel:
    def __init__(self, x, y, color=None):
        self._x = x
        self._y = y
        self._color = color
    
    def get_coordinates(self):
        return (self._x, self._y)
    
    def get_color(self):
        return self._color
    
    def set_color(self, color):
        self._color = color


class Screen:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._pixels = [[Pixel(i, j, 'W') for i in range(width)] for j in range(height)]
    
    def show(self):
        for row in self._pixels:
            for pixel in row:
                print(COLOR_MAP[pixel._color], end='')
            print()
        print()
    
    def get_pixel(self, x, y):
        if self.validate_coordinate(x, y):
            return self._pixels[x][y]
        return None
    
    def validate_coordinate(self, x, y):
        if 0 <= x < len(self._pixels) and 0 <= y < len(self._pixels[0]):
            return True
        return False
    
    def paint_fill(self, x, y, new_color):
        if not self.validate_coordinate(x, y):
            raise Exception("Out of Range.")

        original_color = self.get_pixel(x, y).get_color()
        Q = deque()
        Q.append(self.get_pixel(x, y))
        while Q:
            popped_pixel = Q.popleft()
            if popped_pixel.get_color() == original_color:
                popped_pixel.set_color(new_color)
                px, py = popped_pixel.get_coordinates()
                p1 = self.get_pixel(px-1, py)
                if p1:
                    Q.append(p1)
                p2 =  self.get_pixel(px+1, py)
                if p2:
                    Q.append(p2)
                p3 =  self.get_pixel(px, py-1)
                if p3:
                    Q.append(p3)
                p4 =  self.get_pixel(px, py+1)
                if p4:
                    Q.append(p4)


if __name__ == '__main__':
    s = Screen(11, 11)
    s.show()

    for i in range(11):
        if i < 6:
            s._pixels[5+i][i].set_color('B')
            s._pixels[5-i][i].set_color('B')
        else:
            s._pixels[i-5][i].set_color('B')
            s._pixels[15-i][i].set_color('B')
    s.show()

    s.paint_fill(5, 5, 'B')
    s.show()

    s.paint_fill(0, 0, 'B')
    s.show()

    s.paint_fill(0, 0, 'W')
    s.show()