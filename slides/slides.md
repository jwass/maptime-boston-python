% Geospatial Processing <br> with Python
% <small>Jacob Wasserman / <a href="https://twitter.com/jwass200">@jwass2000</a></small>
% <small><a href="https://twitter.com/MaptimeBoston">Maptime Boston</a> &mdash; 2016-06-15</small>


<section>
<h3>Follow along:</h3>
<h3>[https://jwass.github.io/maptime-python](https://jwass.github.io/maptime-python)</h3>
</section>


Overview
=======

- Why Python?
- Core Geospatial Libraries
- Geospatial Python Libraries
- Write Some Code


Why Python?
===========

Scientific Computing
====================

 - [numpy](http://numpy.org): vectorized array/matrix data structures 
 - [scipy](http://scipy.org): linear algebra, optimization, and much more
 - [pandas](http://pandas.pydata.org/): data analysis, extraction, cleaning
 - [scikit-image](http://scikit-image.org/): image processing
 - [scikit-learn](http://scikit-learn.org/stable/): machine learning


Web Frameworks
==============
 - [Django](https://djangoproject.com): "batteries included" framework
 - [Flask](http://flask.pocoo.org/): "microframework" with large community of
   extensions and functionality

 Many companies are built on Python as their primary backend language


[REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop) environments
=============================

 - [Read Eval Print Loop](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop)
 - [ipython](https://ipython.org/): interactive computing environment
 - [Jupyter Notebook](http://jupyter.org/): web-based with inline results and
   presentation

Glue Language
=============

 - ["Using Python as a Glue Language"](http://docs.scipy.org/doc/numpy-1.10.1/user/c-info.python-as-glue.html)
 - Python bindings  "wrap" C/C++ libraries
 - Enables idiomatic Python constructs with C/C++ speed and memory control
   when necessary
 - We don't necessarily have to re-code a library in Python to use
   it from Python.
 - [cython](http://cython.org/): a Python-like language that compiles C
   extensions

Much More!
==========

Core Geospatial Libraries
=======


Critical Spatial Needs
=====================
  - Spatial operations / computational geometry (shape intersections, point in
    polygon, [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM) )
  - File I/O (vector / raster) for many formats
  - Raster image manipulation
  - Projections and transformations 
  - Spatial indexing 


[GEOS](https://trac.osgeo.org/geos/)
======

  - Geometry Engine Open Source
  - Defines Point, LineString, Polygon, Multi\* types
  - Spatial predicates (intersects, contains, touches, etc) and other
    operations between any combination of geometries
  - Most PostGIS geometry type (but not geography) operations use GEOS under
    the hood

[GDAL](http://www.gdal.org/)
======

 - Geospatial Data Abstraction Library
 - Both vector and raster data I/O
 - Raster manipulation capability
 - Installs utility programs ogr2ogr, ogrinfo, gdalwarp, etc.
 - OGR stands for ¯\\_(ツ)\_/¯
 - [How do you pronounce GDAL?](http://gis.stackexchange.com/questions/72120/why-do-people-pronounce-gdal-geospatial-data-abstraction-library-like-goo-dal)
   ¯\\_(ツ)\_/¯
 - See [Shaun Walbridge's Maptime Boston Presentation](https://4326.us/maptime-data-formats/#/) about geospatial file formats

[PROJ.4](https://trac.osgeo.org/proj/)
========

 - Library and `proj` utility to convert data between projections
 - Defines the `+proj=poly -m 1:25000 +lat_0=35 ...` projection definitions
 - See [Mike Foster's Maptime Boston Presentation](http://mjfoster83.github.io/projections/index.html#/) about projections

[libspatialindex](https://libspatialindex.github.io/)
=====================================================

 - Library for creating and storing spatial indexes
 - Provides indexes for spatial+temporal data too (MVTree and TPRTree)


Geospatial Libraries
========

Capability                   C/C++ Library
-----------                  -------------
Spatial Operations           [GEOS](https://trac.osgeo.org/geos/)
Vector I/O                   [GDAL (OGR)](http://www.gdal.org/)
Raster Operations and I/O    [GDAL](http://www.gdal.org/)
Projections                  [PROJ.4](https://trac.osgeo.org/proj/)
Spatial Indexing             [libspatialindex](https://libspatialindex.github.io/)

Many geospatial applications use one or more of these


Python Geospatial
=========================

Capability                   C/C++ Library                                            Python Library
-----------                  -------------                                            ---------------
Spatial Operations           [GEOS](https://trac.osgeo.org/geos/)                     [shapely](http://toblerity.org/shapely/manual.html)
Vector I/O                   [GDAL (OGR)](http://www.gdal.org/)                       [fiona](http://toblerity.org/fiona/manual.html)
Raster Operations and I/O    [GDAL](http://www.gdal.org/)                             [rasterio](https://github.com/mapbox/rasterio)
Projections                  [PROJ.4](https://trac.osgeo.org/proj/)                   [pyproj](http://jswhit.github.io/pyproj/)
Spatial Indexing             [libspatialindex](https://libspatialindex.github.io/)    [rtree](https://pypi.python.org/pypi/Rtree/)

Python "glue" libraries wrap low-level functionality.


Write Some Code
===============

Shapes
======
![](images/maptime-polygons.bmp)

```
$ ipython

In [1]: %run shapes.py

```

shapes.py
======

```
from shapely.geometry import Point, LineString, Polygon

point1 = Point(1.5, 0.5)
point2 = Point(2.5, 2.5)

line1 = LineString([(0.5, 1.5), (3.5, 1.5)])

# Shapely will automatically close the polygon
poly1 = Polygon([(1.0, 0.0), (3.0, 0.0), (2.0, 2.0)])
poly2 = Polygon([(2.0, 0.5), (3.5, 0.5), (3.5, 1.0), (2.0, 1.0)])
```
