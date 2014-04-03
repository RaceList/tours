# Python imports
import os

# Tornado imports
import tornado.auth
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
from tornado.web import url

# Sqlalchemy imports
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# App imports
import forms
import models
import uimodules

# Options
define("port", default=8888, help="run on the given port", type=int)
define("debug", default=False, type=bool)
define("db_path", default='postgresql+psycopg2://rootart@localhost/route', type=str)


class Application(tornado.web.Application):
  def __init__(self):
    handlers = [
      url(r'/', IndexHandler, name='index'),
    ]
    settings = dict(
      debug=options.debug,
      static_path=os.path.join(os.path.dirname(__file__), "static"),
      template_path=os.path.join(os.path.dirname(__file__), 'templates'),
      xsrf_cookies=False,
      cookie_secret="zGy9csABfiWpdsjxG2zJNMauaZMDyq",
      ui_modules=uimodules,
    )
    tornado.web.Application.__init__(self, handlers, **settings)
    engine = create_engine(options.db_path, convert_unicode=True, echo=options.debug)
    models.init_db(engine)
    self.db = scoped_session(sessionmaker(bind=engine))


class BaseHandler(tornado.web.RequestHandler):
  @property
  def db(self):
    return self.application.db


__UPLOADS__ = 'upload/'
class IndexHandler(BaseHandler):
  def get(self):
    data = {
        'form': forms.GeoUploadForm()
    }
    self.render('index.html', **data)

  def post(self):
    route = models.Route()
    self.db.add(route)
    self.db.commit()

    fileinfo = self.request.files['geom'][0]
    fname = fileinfo['filename']
    extn = os.path.splitext(fname)[1]

    #save original filename
    cname = route.uuid + extn
    fh = open(__UPLOADS__ + cname, 'w')
    fh.write(fileinfo['body'])
    fh.close()
    self.write('Hello')


def main():
  tornado.options.parse_command_line()
  http_server = tornado.httpserver.HTTPServer(Application())
  http_server.listen(options.port)
  tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
  main()
