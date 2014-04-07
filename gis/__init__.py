from .gpx import GPXParser


if __name__ == '__main__':
    gpx = GPXParser('/Users/rootart/Downloads/LykeWakeWalk.gpx')
    gpx.parse()