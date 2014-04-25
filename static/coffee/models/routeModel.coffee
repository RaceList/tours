define ['backbone', 'underscore', 'jquery'], (Backbone, _, $)->
  class RouteModel extends Backbone.Model
    url: '/api/routes/d0112c1e-0778-4fb1-9d8f-b47696bc794b/'
    defaults:
      title: ''
      description: ''
      geom: ''
      st_asgeojson: []

  return RouteModel