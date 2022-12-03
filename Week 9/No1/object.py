from x import X
from y import Y
from z import Z

class Object(X,Y,Z):
    def __init__(self):
        self.__object = True
        X.__init__(self)
        Y.__init__(self)
        Z.__init__(self)
    
n = Object()
print(f"\n M = {n.getSelfM()} \n A = {n.getSelfA()} \n B = {n.getSelfB()} \n X = {n.getSelfX()} \n Y = {n.getSelfY()} \n Z = {n.getSelfZ()}")
