from xml.sax.handler import ContentHandler
import numpy as np
from contextlib import suppress


class MapXmlHandler(ContentHandler):
    @property
    def ways(self):
        return self.__Ways
    def startDocument(self):
        self.__Points = dict()
        self.__Ways = dict()

    def endDocument(self):
        del self.__Points

    def startElement(self, name, attrs):
        with suppress(AttributeError):
            if self.__InRelation: return
        if name == 'node':
            lon = float(attrs['lon'])
            lat = float(attrs['lat'])
            self.__CurrentNode = (lat, lon)
            self.__CurrentNodeId = int(attrs['id'])
        elif name == 'way':
            self.__CurrentWayId = int(attrs['id'])
            self.__CurrentWay = {
                'points': [],
                'tags': dict()
            }
        elif name == 'relation':
            self.__InRelation = True
        elif name == 'nd':
            iid = int(attrs['ref'])
            P = self.__Points[iid]
            self.__CurrentWay['points'].append(P)
        elif name == 'tag':
            key = attrs['k']
            value = attrs['v']
            with suppress(AttributeError):
                self.__CurrentWay['tags'][key] = value
        elif name in ('osm', 'bounds'):
            pass
        else:
            print('start elm ', name)

    def endElement(self, name):
        if name != 'relation':
            with suppress(AttributeError):
                if self.__InRelation: return
        if name == 'node':
            self.__Points[self.__CurrentNodeId] = self.__CurrentNode
            del self.__CurrentNode
            del self.__CurrentNodeId
        elif name == 'way':
            P = self.__CurrentWay['points']
            P = np.array(P, dtype=np.float32)
            self.__CurrentWay['points'] = P
            self.__Ways[self.__CurrentWayId] = self.__CurrentWay
            del self.__CurrentWay
            del self.__CurrentWayId
        elif name == 'relation':
            del self.__InRelation
        elif name in ('nd', 'tag', 'osm', 'bounds'):
            pass
        else:
            print('end elm ', name)