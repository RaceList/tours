define ['backbone', 'underscore', 'jquery'], (Backbone, _, $)->
  class RouteModel extends Backbone.Model
    initialize: (options)->
      @.uuid = options.uuid

    url: ()->
      '/api/routes/'+ @.uuid + '/'
    defaults:
      title: ''
      description: ''
      geom: ''
      st_asgeojson: []

  return RouteModel