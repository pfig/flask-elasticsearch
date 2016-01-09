import unittest

from flask import Flask
from flask.ext.elasticsearch import Elasticsearch


class FlaskElasticsearchTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_extension_supports_factory_pattern(self):
        es = Elasticsearch()
        self.assertTrue(es is not None)

    def test_default_values_are_set(self):
        es = Elasticsearch()
        app = Flask('MyApp')
        es.init_app(app)
        self.assertEqual(app.config['ELASTICSEARCH_CONNECTION'],
                         'http://127.0.0.1:9200')
        self.assertEqual(app.config['ELASTICSEARCH_USERNAME'], '')
        self.assertEqual(app.config['ELASTICSEARCH_PASSWORD'], '')
        self.assertFalse(app.config['ELASTICSEARCH_USE_SSL'])

    def test_configuration_overrides_defaults(self):
        host_str = 'http://srv1.example.com:9200,http://srv2.example.com:9200'
        username = 'es_user'
        password = 'es_password'
        es = Elasticsearch()
        app = Flask('MyApp')
        app.config.from_pyfile('sample.cfg')
        es.init_app(app)
        self.assertEqual(app.config['ELASTICSEARCH_CONNECTION'], host_str)
        self.assertEqual(app.config['ELASTICSEARCH_USERNAME'], username)
        self.assertEqual(app.config['ELASTICSEARCH_PASSWORD'], password)
        self.assertTrue(app.config['ELASTICSEARCH_USE_SSL'])
