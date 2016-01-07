"""
Flask-Elasticsearch
-------------------

An Elasticsearch connector for Flask.

Flask-Elasticsearch should be used in the following way::

    from flask import Flask
    from flask.ext.elasticsearch import Elasticsearch

    app = Flask(__name__)
    app.config.from_pyfile('config.cfg')
    es = Elasticsearch(app)

or::

    es = Elasticsearch()
    app = create_app('config.cfg')
    es.init_app(app)

and later::

    @app.route('/docs')
    def docs():
        conn = es.connection
        conn.search(...)
"""
from elasticsearch import Elasticsearch as Es
from flask import current_app


# The stack on which to store the Elasticsearch connection.
#   Flask >= 0.9 -> _app_ctx_stack
#   Flask <  0.9 -> _request_ctx_stack
try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import __request_ctx_stack as stack


class Elasticsearch(object):
    """An Elasticsearch connector

    Your application's configuration will need the following parameters:
        * ``ELASTICSEARCH_CONNECTION``: a comma-separated list of URLs,
                                        defaults to `http://127.0.0.1:9200`.
        * ``ELASTICSEARCH_USERNAME``: the username to connect with, if any;
                                      defaults to `''`.
        * ``ELASTICSEARCH_PASSWORD``: the password to use, if any;
                                      defaults to `''`.
        * ``ELASTICSEARCH_USE_SSL``: whether to use SSL for the connection,
                                     defaults to `False`.
    """
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('ELASTICSEARCH_CONNECTION',
                              'http://127.0.0.1:9200')
        app.config.setdefault('ELASTICSEARCH_USERNAME', '')
        app.config.setdefault('ELASTICSEARCH_PASSWORD', '')
        app.config.setdefault('ELASTICSEARCH_USE_SSL', False)
        # Use the new style teardown_appcontext if it's available,
        # otherwise fall back to the request context.
        if hasattr(app, 'teardown_appcontext'):
            app.teardown_appcontext(self.teardown)
        else:
            app.teardown_request(self.teardown)

    def connect(self):
        return Es(
            current_app.config['ELASTICSEARCH_CONNECTION'].split(','),
            http_auth=(current_app.config['ELASTICSEARCH_USERNAME'],
                       current_app.config['ELASTICSEARCH_PASSWORD']),
            use_ssl=current_app.config['ELASTICSEARCH_USE_SSL'],
            sniff_on_start=True,
            sniff_on_connection_fail=True
        )

    def teardown(self, exception):
        ctx = stack.top
        if hasattr(ctx, 'elasticsearch_connection'):
            ctx.elasticsearch_connection = None

    @property
    def connection(self):
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, 'elasticsearch_connection'):
                ctx.elasticsearch_connection = self.connect()
            return ctx.elasticsearch_connection
