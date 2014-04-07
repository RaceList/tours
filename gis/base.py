class UnexpectedParsingError(Exception):
    pass

class BaseParser(object):
    extensions = []

    def __init__(self, file_or_path):
        assert self.extensions
        if isinstance(file_or_path, basestring):
            self.file = open(file_or_path, 'r')
        self.parse()

    def parse(self):
        raise NotImplementedError
