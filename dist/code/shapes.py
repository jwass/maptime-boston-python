from shapely.geometry import Point, LineString, Polygon

point1 = Point(1.5, 0.5)
point2 = Point(2.5, 2.5)

line1 = LineString([(0.5, 1.5), (3.5, 1.5)])

# Shapely will automatically close the polygon
poly1 = Polygon([(1.0, 0.0), (3.0, 0.0), (2.0, 2.0)])
poly2 = Polygon([(2.0, 0.5), (3.5, 0.5), (3.5, 1.0), (2.0, 1.0)])
