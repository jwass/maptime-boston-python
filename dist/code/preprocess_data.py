# Download Boston 311 data from http://data.cityofboston.gov
# https://data.cityofboston.gov/City-Services/311-Service-Requests/awu8-dc52
# and export as CSV. It's a fairly large file: 334MB
# The CSV is processed using pandas (http://pandas.pydata.org/)
import json

# This script uses pandas and geopandas to conver the downloaded
# CSV to a GeoJSON file
import geopandas as gpd
import pandas as pd
import shapely.geometry


def convert(in_csv_filename, out_geojson_filename):
    # Read the CSV into a Pandas DataFrame object
    df = pd.read_csv(in_csv_filename)

    # Find all the rows related to rodent activity
    rodent_rows = df['CASE_TITLE'] == 'Rodent Activity'

    # Select only the rodent rows removing all others
    df = df[rodent_rows]

    # Create Shapely Point objects for each row
    df['geometry'] = df.apply(row_to_point, axis=1)

    # Filter out only the columns we need: geometry and open_dt
    df = df[['geometry', 'OPEN_DT']]

    # The set_geometry() method creates a GeoDataFrame using the column
    # named 'geometry' as the primary geo column
    df = df.set_geometry('geometry')

    with open(out_geojson_filename, 'w') as f:
        # The GeoDataFrame .to_json() method returns a GeoJSON
        # FeatureCollection dictionary of the GeoDataFrame.
        f.write(df.to_json())


def row_to_point(row):
    x = row['LONGITUDE']
    y = row['LATITUDE']
    return shapely.geometry.Point(x, y)
