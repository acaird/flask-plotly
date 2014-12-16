import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/flaskly/')
from flaskPlotly import app as application
