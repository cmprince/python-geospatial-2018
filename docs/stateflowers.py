# coding: utf-8
import pandas as pd
import geopandas as gpd
from matplotlib import pyplot as plt
from fiona.crs import from_epsg

flowers = pd.read_csv('./stateflowers.txt', delimiter='\t')
flowers[flowers.State=='Ohio']
flowers[flowers['Common name']=='Violet']
states = gpd.read_file('./data/cb_2016_us_state_5m.shp')
states = states.merge(flowers, left_on='NAME', right_on='State')
get_ipython().magic('matplotlib qt')
f, ax = plt.subplots(figsize=(6,6))
states.plot(ax=ax)
states.crs = from_epsg(4326)
naec = '+proj=eqdc +lat_0=40 +lon_0=-96 +lat_1=20 +lat_2=60 +x_0=0 +y_0=0 +datum=NAD83 +units=m +no_defs'
states.to_crs(naec).plot(ax=ax)
ax.set_axis_off()
ax.set_title('USA! USA!')
ax.set_aspect(1)
states_proj = states.to_crs(naec)
states_proj.plot(ax=ax)
states_proj.apply(lambda state: ax.annotate(s=state.NAME, xy=state.geometry.centroid.coords[0], ha='center'), axis=1)
states_proj.plot(ax=ax)
states_proj.apply(lambda state: ax.annotate(s=state['Common name'], xy=state.geometry.centroid.coords[0], ha='center'), axis=1)
ax.set_axis_off()
ax.set_title('USA flowers')
states.centroids = states.geometry.centroid
states.centroids
states.plot()
states.centroids.plot()
from shapely.geometry import Point
Point(1,2)
Point(1,2).plot(ax=ax)
gpd.GeoSeries(Point(1,2)).plot()
