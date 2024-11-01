import math

def calcArea(r, h):
    return calcSideArea(r, h) + 2 * math.pi * r**2

def calcSideArea(r, h):
    return 2 * math.pi * r * h

def calcVolume(r, h):
    return math.pi * r**2 * h
