"""To launch application with your local options pass them to command line, e.g.::

    python app.py --option_name=value

"""
from tornado.options import define, options


define('port', default=8888, help="run on the given port", type=int)
define('address', default='', help="run on the given IP", type=str)

define('debug', default=True, type=bool)

define('db_name', default='route', type=str)
define('db_user', default='rootart', type=str)
