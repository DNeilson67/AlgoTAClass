class Circle:
    def __init__(self,radius = 1.0,color ="red"):
        self.__radius = radius
        self.__color = color

    def getRadius(self):
        return self.__radius

    def setRadius(self,radius):
        self.__radius = radius
    
    def getColor(self):
        return self.__color
    
    def setColor(self,color):
        self.__color = color
    
    def getArea(self):
        return 3.14*self.getRadius()**2