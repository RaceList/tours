from wtforms import *
from wtforms.validators import *

from util import MultiValueDict

class BaseForm(Form):
    def __init__(self, handler=None, obj=None, prefix='', formdata=None, **kwargs):
        if handler:
            formdata = MultiValueDict()
            for name in handler.request.arguments.keys():
                formdata.setlist(name, handler.get_arguments(name))
        Form.__init__(self, formdata, obj=obj, prefix=prefix, **kwargs)


class GeoUploadForm(BaseForm):
    geom = FileField(u'Geo file', validators=[validators.required()])