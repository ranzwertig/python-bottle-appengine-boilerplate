from lib import bottle
from plugins import decorators
from google.appengine.api import users

def initRoutes(app=None):
    if not app:
        app = bottle.default_app()
        
    @app.route('/')
    @decorators.private
    @bottle.view('index_default')
    def default():
        return dict(content='hello, '+users.get_current_user().nickname())
        
    @app.route('/logout')
    @app.route('/logout/')
    def logout():
        user = users.get_current_user()
        if user:
            bottle.redirect(users.create_logout_url(bottle.request.url))
        else:
            return 'sucessfully logged out'
