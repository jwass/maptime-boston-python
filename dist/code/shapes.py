from shapely.geometry import Point, LineString, Polygon

# Create a Point with x, y coordinates
point1 = Point(1.5, 0.5)
point2 = Point(2.5, 2.5)

# Create a LineString with a list of (x, y) tuples
line1 = LineString([(0.5, 1.5), (3.5, 1.5)])

poly1 = Polygon([(1.0, 0.0), (3.0, 0.0), (2.0, 2.0)])
poly2 = Polygon([(2.0, 0.5), (3.5, 0.5), (3.5, 1.0), (2.0, 1.0)])

# Polygons can have holes. Specify them as a list of list of (x, y) tuples
poly_w_hole = Polygon([(0.0, 0.0), (5.0, 0.0), (5.0, 5.0), (0.0, 5.0)],
                      [[(1.0, 1.0), (2.0, 1.0), (2.0, 2.0), (1.0, 2.0)],
                       [(3.0, 3.0), (4.0, 3.0), (4.0, 4.0), (3.0, 4.0)]])
