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
        previewTemplate:
          """
          <div class="dz-preview dz-file-preview">
          <div class="dz-details">
            <div class="dz-filename"><span data-dz-name></span></div>
          </div>
          <div class="dz-progress"><span class="dz-upload" data-dz-uploadprogress></span></div>
          <div class="dz-success-mark"><span>✔</span></div>
          <div class="dz-error-mark"><span>✘</span></div>
          <div class="dz-error-message"><span data-dz-errormessage></span></div>
          </div>
          """


  return HomePageUploadView