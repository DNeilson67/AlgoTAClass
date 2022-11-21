class Point:
    def __init__ (self, x, y):
        self.__x = x
        self.__y = y
    def set_x(self,x):
        self.__x = x
    def set_y(self,x):
        self.__y = x
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y

def get_json_str(x):
    return {"__class__": "Point", "x": x.get_x(), "y": x.get_y()}

def read_json_str(x,y):
    int(x)
    int(y)
    z = Point(x,y)
    return get_json_str(z)

z = read_json_str(1,2)
print(z)