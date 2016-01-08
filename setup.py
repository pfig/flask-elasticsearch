"""
Flask-Elasticsearch
-------------------

An Elasticsearch connector for Flask.

This provides a low-level Elasticsearch client, for full details
on functionality please see ``elasticsearch.Elasticsearch``.
"""
from setuptools import setup


setup(
    name='Flask-Elasticsearch',
    version='0.0.1',
    url='https://pfig.github.io/flask-elasticsearch',
    license='MIT',
    author='Pedro Figueiredo',
    author_email='pfig@me.com',
    description='An Elasticsearch connector for Flask',
    long_description=__doc__,
    py_modules=['flask_elasticsearch'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'elasticsearch'
    ],
    test_suite='test_flask_elasticsearch.FlaskElasticsearchTestCase',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
