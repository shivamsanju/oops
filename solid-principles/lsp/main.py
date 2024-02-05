'''
If you use a base class/interface and you put a derived class then 
everything should work
'''

class Rectange:
    def __init__(self, height:int, width: int) -> None:
        self._height = height
        self._width = width

    @property
    def width(self) -> int:
        return self._width
    
    @width.setter
    def width(self, width: int) -> None:
        self._width = width

    @property
    def height(self) -> int:
        return self._height
    
    @height.setter
    def height(self, height: int) -> None:
        self._height = height

    def area(self) -> int:
        return self._height * self._width


def print_area_of_rectangle(r: Rectange) -> None:
    print(r.area())

r = Rectange(2,5)
print_area_of_rectangle(r)

'''
If we substitute with a derived class Square it should work
'''

class Square(Rectange):
    def __init__(self, side: int) -> None:
        super().__init__(side, side)

s = Square(5)

print_area_of_rectangle(s)