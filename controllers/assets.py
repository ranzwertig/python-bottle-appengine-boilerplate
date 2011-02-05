from lib import *

def initRoutes(app=None):
    if not app:
        app = bottle.default_app()
        
    @app.route('/styles/:filename')
    def css(filename):
        return static_file(filename, root='.\\assets\\css\\')
        
    @app.route('/images/:filename')
    def css(filename):
        return static_file(filename, root='.\\assets\\img\\')
        
    @app.route('/scripts/:filename')
    def css(filename):
        return static_file(filename, root='.\\assets\\script\\')


