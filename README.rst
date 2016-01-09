An Elasticsearch connector for Flask
------------------------------------

.. image:: https://travis-ci.org/pfig/flask-elasticsearch.svg?branch=master
    :alt: CI for master branch
    :target: https://travis-ci.org/pfig/flask-elasticsearch

.. image:: https://travis-ci.org/pfig/flask-elasticsearch.svg?branch=develop
    :alt: CI for develop branch
    :target: https://travis-ci.org/pfig/flask-elasticsearch

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
