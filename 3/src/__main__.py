from os.path import join, abspath, dirname, normpath
import xml.sax
import matplotlib.pyplot as plt

from MapXmlHandler import MapXmlHandler

datapath = dirname(abspath(__file__))
datapath = normpath(join(datapath, '..', 'data'))
datafilepath = join(datapath, 'map.osm')

mapdata = MapXmlHandler()
xml.sax.parse(datafilepath, mapdata)

for way in mapdata.ways.values():
    w = way['points']
    plt.plot(w[:,0], w[:,1], color='blue')

plt.axis([5.97858, 5.96586, 80.43194, 80.45374])
plt.show()
