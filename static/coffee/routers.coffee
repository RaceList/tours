define ['backbone', 'underscore', 'jquery', 'views/homepageuploadview', 'views/routeMapDetailsView', 'models/routeModel'], (Backbone, _, $, HomePageUploadView, RouteMapDetailView, RouteModel)->
  class AppRouter extends Backbone.Router

    routes:
      'routes/:routeUUID': 'showRouteDetails'
      '*actions': 'defaultAction'

    showRouteDetails: (uuid)->
      console.log 'details'
      window.homePageUploadView?.remove()
      $('.file-upload-block')?.remove()
      console.log 'Loading RouteMapDetailView'
      model = new RouteModel
        uuid: uuid
      model.fetch
        async: false
      console.log model
      window.routeMapDetailsView = new RouteMapDetailView
        model: model

      return

    defaultAction: ()->
      window.homePageUploadView = new HomePageUploadView()
      return

  return AppRouter