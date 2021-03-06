# -*- coding: utf-8 -*-
__doc__ = """
Module to host a Django application from within a CherryPy server.

Instead of creating a clone to `runserver` like other similar
packages do, we simply setup and host the Django application
using WSGI and CherryPy's capabilities to serve it.

In order to configure the application, we use the `settings.configure(...)`
function provided by Django.

Since the CherryPy WSGI server doesn't offer a log
facility, we add a straightforward WSGI middleware to do so, based
on the CherryPy built-in logger. Obviously any other log middleware
can be used instead.

Note this application admin site uses the following credentials:
admin/admin

Thanks to Damien Tougas for his help on this recipe.
"""
if __name__ == '__main__':
    import cherrypy
    import os
    cherrypy.config.update({
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 8090,
        'checker.on': False,
    })

    from djangoplugin import DjangoAppPlugin
    import service_settings
    service_settings.setup_env()
    DjangoAppPlugin(cherrypy.engine, service_settings).subscribe()
	
    cherrypy.quickstart()
