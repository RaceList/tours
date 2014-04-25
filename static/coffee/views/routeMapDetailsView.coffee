define ['backbone', 'underscore', 'jquery', 'leaflet'], (Backbone, _, $)->
  class RouteMapDetailView extends Backbone.View
    el: '.map-block'
    initialize: ()->
      @.render()

    render: ()->
      @.$el.html('<div id="map"></div>')
      map = new L.Map 'map'

      layer = L.tileLayer 'http://{s}.tile.cloudmade.com/9d0b97ba4e6d403aad532091aaafbc0b/997/256/{z}/{x}/{y}.png',
        attribution: 'Cloudmade'
        maxZoom: 18
      layer.addTo map

      vectorData =
        type: 'Feature'
        geometry: @.model.get 'st_asgeojson'

      vectorLayer = L.geoJson()
      vectorLayer.addTo map
      vectorLayer.addData vectorData
      console.log vectorLayer.getBounds()
      map.fitBounds vectorLayer.getBounds()



  return RouteMapDetailView