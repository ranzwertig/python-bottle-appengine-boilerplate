import datetime
from lib import bottle
from google.appengine.ext.webapp import util 
from google.appengine.ext import db
from google.appengine.api import users

from plugins import hooks
from controllers import index, error
from config import config

app = bottle.Bottle(config=config.production)

#set controller routes
index.initRoutes(app)
error.initRoutes(app)

# init plugins
hooks.init_hooks(app)   
util.run_wsgi_app(app)
