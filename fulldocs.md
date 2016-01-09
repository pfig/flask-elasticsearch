---
title: "Flask-Elasticsearch :: Documentation"
layout: default
---

### Full Documentation

#### Configuration variables

* `ELASTICSEARCH_CONNECTION`<br>
  A comma-separated list of Elasticsearch URIs, in the form
  `scheme://host:port`, e.g.,
  `http://srv1.example.com:9200,http://srv2.example.com:9200`
  Defaults to `http://127.0.0.1:9200`.

* `ELASTICSEARCH_USERNAME`<br>
  The username to use to connect to Elasticsearch, if any.

* `ELASTICSEARCH_PASSWORD`<br>
  The password to use to connect to Elasticsearch, if any.

* `ELASTICSEARCH_USE_SSL`
  Whether to use SSL when connecting to Elasticsearch.
  Defaults to `False`.
