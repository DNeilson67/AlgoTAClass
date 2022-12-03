from m import M
class B(M):
    def __init__(self):
        self.__b = True
        M.__init__(self)
    def getSelfB(self):
        return self.__b
        