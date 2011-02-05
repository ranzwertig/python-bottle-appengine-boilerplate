from lib import *

def initRoutes(app=None):
    if not app:
        app = bottle.default_app()
        
    @app.route('/denied')
    def restricted():
        abort(401, "Sorry, access denied.")
     
    @bottle.error(404)
    def error404(error):
        return 'Nothing here, sorry'


