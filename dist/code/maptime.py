import fiona
import shapely.geometry


class Neighborhood:
    def __init__(self, polygon, name, area):
        self.polygon = polygon
        self.name = name
        self.area = area

        self.n_rodents = 0


def read_neighborhoods(filename):
    """
    Read a shapefile of Boston neighborhood polygons

    Parameters
    ----------
    filename : string
        Path to Shapefile of Boston neighborhoods

    Returns
    -------
    neighborhoods : list of Neighborhood objects

    """
    neighborhoods = []
    with fiona.open(filename) as f:
        for feature in f:
            shape = shapely.geometry.shape(feature['geometry'])
            name = feature['properties']['Name']
            area = feature['properties']['SHAPE_area']

            n = Neighborhood(shape, name, area)
            neighborhoods.append(n)

    return neighborhoods


def read_rodents(filename):
    """
    Read a file of reported rodent activity

    Parameters
    ----------
    filename : string
        Path to file of rodent data

    Returns
    -------
    rodents : list of Shapely Point geometries

    """
    rodent_points = []
    # Since the rodent file is GeoJSON, you could use Python's
    # builtin json module instead of fiona.
    with fiona.open(filename) as f:
        for feature in f:
            point = shapely.geometry.shape(feature['geometry'])
            rodent_points.append(point)

    return rodent_points


def assign_rodent_counts(neighborhoods, rodents):
    """
    Assign rodent counts to neighborhood objects

    Finds the number of rodents in each neighborhood and updates
    the neighborhood rodent count
    
    Parameters
    ----------
    neighborhoods : list of Neighborhood objects
    rodents : list of Shapely Point geometries

    Returns
    -------
    None

    """
    # Reset counts to 0 
    for n in neighborhoods:
        n.n_rodents = 0

    # For each rodent, find the neighborhood it belongs to.
    for r in rodents:
        for n in neighborhoods:
            if n.polygon.contains(r):
                n.n_rodents += 1
                # Move on to the next rodent once we find the correct
                # neighborhood
                break
