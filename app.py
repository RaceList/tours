#! /usr/bin/env python
# Python imports
import os
import datetime
import json

# Tornado imports
import tornado.auth
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import options
from tornado.web import url

# Sqlalchemy imports
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# App imports
import forms
import models
import uimodules
from gis.gpx import GPXParser

import settings


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            url(r'/', IndexHandler, name='index'),
            url(r'/api/routes/([^/]+)/', APIRouteDetailsHandler, name='api:details')
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
        db_path = 'postgresql+psycopg2://%(db_user)s@localhost:%(db_port)s/%(db_name)s' % {
            'db_user': options.db_user,
            'db_name': options.db_name,
            'db_port': options.db_port,
        }
        engine = create_engine(db_path, convert_unicode=True, echo=options.debug)
        models.init_db(engine)
        self.db = scoped_session(sessionmaker(bind=engine))


class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db


__UPLOADS__ = 'upload/'


class APIRouteDetailsHandler(BaseHandler):
    def get(self, _uuid):
        # query = self.db.query(models.Route).filter(models.Route.uuid == _uuid)
        query = self.db.execute("select ST_AsGeoJSON(geom) from route where uuid = '%s'" % _uuid)
        data = dict(query.fetchall()[0])
        self.write(
            data
        )


class IndexHandler(BaseHandler):
    def get(self):
        self.render('index.html', **{})

    def save_file(self):
        route = models.Route()
        self.db.add(route)
        self.db.commit()

        fileinfo = self.request.files['geom'][0]
        fname = fileinfo['filename']
        extn = os.path.splitext(fname)[1]

        #save original filename
        cname = route.uuid + extn
        date_pth = datetime.date.today().strftime("%Y/%m/%d/")
        dir_pth = os.path.join(__UPLOADS__, date_pth)
        if not os.path.exists(dir_pth):
            os.makedirs(dir_pth)
        pth = os.path.join(dir_pth, cname)

        fh = open(pth, 'w')
        fh.write(fileinfo['body'])
        fh.close()
        parser = GPXParser(pth)
        route.geom = parser.to_multylinestring

        route.file = pth
        self.db.add(route)
        self.db.commit()

        return route, pth

    def post(self):
        route, pth = self.save_file()
        data = {
            'routeUUID': route.uuid,
            'routeFilePTH': route.file
        }
        self.write(data)


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port, address=options.address)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
