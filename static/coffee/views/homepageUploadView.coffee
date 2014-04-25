define ['backbone', 'underscore', 'jquery', 'dropzone'], (Backbone, _, $, Dropzone)->
  class HomePageUploadView extends Backbone.View
    el: '.file-upload-block'
    initialize: ()->
      @.$('.dropzone').dropzone
        paramName: 'geom'
        url: '.'
        clickable: true
        uploadprogress: (file, progress, bytesSent)->
          console.log progress, bytesSent
        success: (file, data)->
          window.location.href = '#/routes/'+data.routeUUID

  return HomePageUploadView