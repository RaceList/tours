require.config
  paths:
    jquery: 'vendor/jquery-1.9.1'
    underscore: 'vendor/underscore'
    backbone: 'vendor/backbone'
    csrf: 'vendor/csrf'
    select2: 'vendor/select2'
    text: 'vendor/text'
    dropzone: 'vendor/dropzone/dropzone-amd-module'

  shim:
    backbone:
      deps: ['jquery', 'underscore']
      exports: 'Backbone'
    underscore:
      exports: '_'
    csrf:
        deps: ['jquery',]
    select2:
        deps: ['jquery',]


require ['jquery', 'backbone', 'underscore', 'views/homepageuploadview', 'dropzone'], ($, Backbone, _, HomePageUploadView, Dropzone)->
  homePageUploadView = new HomePageUploadView()

  return