'''
Intersection:
Given two straight line segments (represented as a start point and an end point), 
compute the point of intersection, if any.
'''

from dataclasses import dataclass


@dataclass
class Point:
    x:int
    y:int

'''

y = ax+b
we want

x so that a1x+b1 = a2x+b2
-> (a1 - a2)x = b2 - b1
-> x = (b2 - b1) / (a1 - a2) 

'''


def intersection(lineA: tuple[Point, Point], lineB: tuple[Point, Point]) -> Point | None:

    (slopeA, intersectA) = computeSlopeAndYIntersect(lineA)
    (slopeB, intersectB) = computeSlopeAndYIntersect(lineB)

    # special case if slopeA == slopeB, check intersect and  [a1 < b1 < a2] 
    if slopeA == slopeB:
        return lineB[0] if intersectB == intersectA else None

    x = (intersectB - intersectA)/ (slopeA - slopeB) 
    
    if lineA[0].x <= x <= lineA[1].x and lineB[0].x <= x <= lineB[1].x:
        return Point(x, slopeA*x + intersectA)

    return None


def computeSlopeAndYIntersect(line:tuple[Point, Point]) -> tuple[float, float]:

    pointA = line[0]
    pointB = line[1]

    slope = (pointB.y - pointA.y) / (pointB.x - pointA.x)
    # y = ax+b
    # b = y - ax
    intersect = pointA.y - slope*pointA.x
    return (slope, intersect)