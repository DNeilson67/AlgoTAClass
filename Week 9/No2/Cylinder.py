from Circle import Circle

class Cylinder(Circle):
    def __init__(self, radius, color, height = 1.0):
        super().__init__(radius,color)
        self.height = height
    def getHeight(self):
        return self.height
    def setHeight(self,height):
        self.height = height
    def getVolume(self):
        return self.getArea()*self.getHeight()