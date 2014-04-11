define ['backbone', 'underscore', 'jquery', 'views/homepageuploadview'], (Backbone, _, $, HomePageUploadView)->
  class AppRouter extends Backbone.Router

    routes:
      'routes/:routeUUID': 'showRouteDetails'
      '*actions': 'defaultAction'

    showRouteDetails: ()->
      console.log 'details'
      return

    defaultAction: ()->
      homePageUploadView = new HomePageUploadView()
      return

  return AppRouter