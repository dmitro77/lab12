import CylinderOperations

class Cylinder(object):
    r = 0
    h = 0
    
    def __init__(self, r, h):
        self.r = r
        self.h = h
    
    def __str__(self):
        return "r={r}, h={h}".format(r=self.r, h=self.h)

cyl = Cylinder(r=2, h=5)

print("\nFor cylinder: ", cyl)
print("Area: ", CylinderOperations.calcArea(r=cyl.r, h=cyl.h))
print("Side area: ", CylinderOperations.calcSideArea(r=cyl.r, h=cyl.h))
print("Volume: ", CylinderOperations.calcVolume(r=cyl.r, h=cyl.h))
