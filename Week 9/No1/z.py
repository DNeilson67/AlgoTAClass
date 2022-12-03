from b import B
from m import M
class Z(B,M):
    def __init__(self):
        self.__z = True
        M.__init__(self)
        B.__init__(self)
    def getSelfZ(self):
        return self.__z