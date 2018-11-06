import math
class Vector(object):
    def __init__(self, x=0, y=0):
       self.__x = float(x)
       self.__y = float(y)
    def __str__(self):
        out_str = "({:.2f}, {:.2f})".format(self.__x, self.__y)
        return out_str
    def __repr__(self):
       return str(self)
    def __add__(self , vector):
        new_x = self.__x + vector.__x
        new_y = self.__y + vector.__y
        v = Vector(new_x, new_y)
        return v
    def __sub__(self, vector): 
        new_x = self.__x - vector.__x
        new_y = self.__y - vector.__y
        v = Vector(new_x, new_y)
        return v
    def __mul__(self, other): 
        if type(other) == Vector:        
            new_x = self.__x * other.__x
            new_y = self.__y * other.__y
            v = Vector(new_x, new_y)
            return v
        
        if type(other) == int:
            newx = self.__x * other
            newy = self.__y * other
            b = Vector(newx, newy)
            return b
            
    def __rmul__(self, other): 
        if type(other) == int:
            newx = self.__x * other
            newy = self.__y * other
            b = Vector(newx, newy)
            return b
        new_x = self.__x * other.__x
        new_y = self.__y * other.__y
        v = new_x + new_y
        return v
    def __eq__(self, vector):
        if self.__x == vector.__x:
            if self.__y == vector.__y:
                return True
            else:
                return False
        else:
            return False
    def magnitude(self):
        v = math.sqrt(self.__x * self.__x + self.__y * self.__y)
        return v
    def unit(self):
        if self.magnitude() == 0:
            raise ValueError("Cannot convert zero vector to a unit vector")
        x = self.magnitude()
        self.__x = 1/x*(self.__x)
        self.__y = 1/x *(self.__y)
       
#new = Vector()
#print(new)
#
#x = 5
#y = 10
#v1 = Vector()
l = [1,2,3]
print(l)
l.append(4)
print(l)

v1 = Vector(1, 2)
v = Vector(1,2)
v2 = Vector(3, 4)
print(v1.magnitude())
print(v1 == v2)
print(v1 * v2)
print(5 * v1)
v1.unit()
print(v1)



