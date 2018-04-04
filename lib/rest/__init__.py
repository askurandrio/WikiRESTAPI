"""The rest module"""
import sys
import logging

import flask
import flask_restful

from .PageCollection import PageResource


#TODO: rework logging
LOGGER = logging.getLogger('WikiRESTAPI')

STDOUT = logging.StreamHandler(sys.stdout)
STDOUT.setFormatter(logging.Formatter('%(process)d %(asctime)s: [%(levelname)s] %(message)s'))
LOGGER.addHandler(STDOUT)

APP = flask.Flask('WikiRESTAPI')
APP.config['PROPAGATE_EXCEPTIONS'] = True
API = flask_restful.Api(APP)
API.add_resource(PageResource, '/page', '/page/<int:page_id>')


@APP.errorhandler(Exception)
def _(ex):
    """Standard error handler for APP"""
    LOGGER.exception('Error when processing request')
    return {}, 500
