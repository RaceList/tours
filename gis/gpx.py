import gpxpy

from .base import BaseParser


class GPXParser(BaseParser):
    extensions = ['.gpx']

    def parse(self):
        self.gpx = gpxpy.parse(self.file)
        segments = []
        for track in self.gpx.tracks:
            for segment in track.segments:
                segments.append([(x.latitude, x.longitude) for x in segment.points])
        self.segments = segments
        self.to_multylinestring = self.__to_multilinesting()

    def __to_multilinesting(self):
        '''
            MULTILINESTRING((10 10, 20 20), (15 15, 30 15))
        '''
        geo_type = 'MULTILINESTRING'
        strings = ''
        segments_list = []
        for segment in self.segments:
            strings += '('
            strings += ','.join([
                '{0} {1} '.format(x[0], x[1]) for x in segment
            ])
            strings += ')'
            segments_list.append(strings)
        return '{} ( {} )'.format(geo_type, ','.join(segments_list))




