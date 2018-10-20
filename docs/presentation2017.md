## Geospatial analytics in Python

November 2017

<small>Christopher Prince</small>

---

### Topics

<section style="text-align: left;">

What we'll cover:
* Spatial data formats
* Feature creation
* Map projections
* Plotting
* Spatial operations and manipuation
* Statistical methods

What we won't cover:
* Interfaces to GIS packages (like QGIS or ArcGIS)


---

### Geopandas installation

Installation is a *lot* easier than it used to be. Both <code>pip</code> and <code>conda</code> should take care of the dependencies you will need.

It's still not a 1.0 release, though, so it's a good idea to setup a seperate environment for it.

If you use the PUI kernels on <code>compute</code>, the installation is already taken care of!

- -

### What is geopandas?

Geopandas is the GIS-extension of <code>pandas</code>. It also builds on other spatial packages:

* fiona
* shapely
* pyproj
* rtree
* pysal

---

### Fiona

Fiona reads and writes GIS files in various formats. 99.9% of the time you will be working with either:
* *Shapefile*: Actually a set of database files, though it's common to refer to just the \*.shp file. Other attributes and metadata are stored in (necessary) supplemental files.
* *GeoJSON*: A JSON file with additional geometry attributes, and possibly a metadata header.

- -

### GeoJSON example

<pre>
{
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [125.6, 10.1]
  },
  "properties": {
    "name": "Dinagat Islands"
  }
}
</pre>

---

### Shapely

Shapely is a python library for geometric operations using the GEOS library.

Shapely can perform:
* geometry validation
* geometry creation (e.g. collections)
* geometry operations
  
- -

### Geometry creation

Shapely supports the creation of primitive geometry features. These include:

<code>
* Point
* LineString
* LinearRing
* Polygon</code>

Multipart collections are also supported: <code>MultiPoint, MultiLineString</code> and <code>MultiPolygon</code>

- -
### Shapely geometric operations
<img src="images/shapely/difference.png" height=500>
<small style="text-align: left;">source: http://kjordahl.github.io/SciPy-Tutorial-2015/</small>

- -
### Shapely geometric operations
<img src="images/shapely/intersection-sym-difference.png" height=500>
<small style="text-align: left;">source: http://kjordahl.github.io/SciPy-Tutorial-2015/</small>

- -
### Shapely geometric operations
<img src="images/shapely/cascaded_union.png" height=500>
<small style="text-align: left;">source: http://kjordahl.github.io/SciPy-Tutorial-2015/</small>
  
- -
### Shapely geometric operations
<img src="images/shapely/union.png" height=500>
<small style="text-align: left;">source: http://kjordahl.github.io/SciPy-Tutorial-2015/</small>
  
- -
### Shapely geometric operations
<pre>
> from shapely.geometry import LineString
> line = LineString([(0, 0), (1, 1), (0, 2), (2, 2), (3, 1), (1, 0)])
> dilated = line.buffer(0.5)
> eroded = dilated.buffer(-0.3)
</pre>

<p><center>
<img src="images/shapely/buffer-trim.png" height=300>
</center></p>
<small style="text-align: left;">source: http://kjordahl.github.io/SciPy-Tutorial-2015/</small>
 
- -
### Binary predicates 
<code>object.almost_equals(other[, decimal=6])</code>
<code>object.contains(other)</code>
<code>object.crosses(other)</code>
<code>object.disjoint(other)</code>
<code>object.equals(other)</code>
<code>object.intersects(other)</code>
<code>object.touches(other)</code>
<code>object.within(other)</code>
<footer class="source"><a href=http://toblerity.github.io/shapely/manual.html#binary-predicates>details</a></footer></article>
 

---

### Geographic projection

<iframe width="784" height="443" src="https://www.youtube.com/embed/vVX-PrBRtTY?rel=0&amp;controls=0&amp;showinfo=0&amp;start=46" frameborder="0" allowfullscreen></iframe><!-- .element: class="fragment" data-fragment-index="1" -->
<small>https://youtu.be/vVX-PrBRtTY?t=46s</small><!-- .element: class="fragment" data-fragment-index="1" -->

- -

<img src="images/Mercator_projection_SW.jpg" height=500>

<small>Mercator projection (1569)</small>
- -

<img src="images/Craig_projection_SW.jpg" height=500>

<small>Craig retroazimuthal projection (1909)</small>

- -

<img src="images/Česká_republika,_Křovák.png" height=500>

<small>Křovák's projection (black) versus WGS84 projection (orange)</small>

- -

### pyproj

Pyproj provides an interface to the PROJ.4 library which performs the transformations between coordinate reference systems (CRS). This can be done explicitly by specifying datums, geodetic ellipse, origin, and other parameters in a "PROJ4 string".

Many common projections are indexed with a numerical code from the European Petroleum Survey Group, and using these is generally much simpler with fiona.

- -

### projection example
<section style="text-align: left;">

PROJ.4 string (North American Equidistant Conic):
<code>naec = '+proj=eqdc +lat_0=40 +lon_0=-96 +lat_1=20 +lat_2=60 +x_0=0 +y_0=0 +datum=NAD83 +units=m +no_defs'</code>

Fiona EPSG 4326 (WGS84 lat/long):

<code>
from fiona.crs import from_epsg
states.crs = from_epsg(4326)
</code>

Transforming from one to the other:

<code>states.to_crs(naec)</code>

---

## Lab
