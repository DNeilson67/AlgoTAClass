from a import A
class X(A):
    def __init__(self):
        self.__x = True
        A.__init__(self)
    def getSelfX(self):
        return self.__x
