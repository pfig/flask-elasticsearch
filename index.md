---
title: "Flask-Elasticsearch"
layout: default
---

Flask-Elasticsearch should be used in the following way:


{% highlight python %}
from flask import Flask
from flask.ext.elasticsearch import Elasticsearch

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
es = Elasticsearch(app)
{% endhighlight %}

or:

{% highlight python %}
es = Elasticsearch()
app = create_app('config.cfg')
es.init_app(app)
{% endhighlight %}

and later:

{% highlight python %}
@app.route('/docs')
def docs():
    conn = es.connection
    conn.search(...)
{% endhighlight %}

[Full documentation &raquo;](fulldocs.html)
