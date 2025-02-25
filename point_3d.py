class Integer:
    @classmethod
    def verify_coord(cls, coord):
        if type (coord) != int:
            raise TypeError("coordinate is not good")

    def __set_name__(self,owner,name):
        self.name = "_" + name
    
    def __get__(self, instance, owner):
        return getattr(instance,self.name) #instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        self.verify_coord(value)
        setattr(instance, self.name, value) #instance.__dict__[self.name] = value


class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

   
    
p = Point3D(1,200,3)
print(p.__dict__)