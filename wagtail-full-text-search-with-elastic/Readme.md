- Create network: `docker network create wagtail-full-text-search-with-elasticsearch`

- Start elasticsearch

``` bash
docker run --name elasticsearch \
--hostname elasticsearch \
--network wagtail-full-text-search-with-elasticsearch \
--rm \
-p 9200:9200 \
-p 9300:9300 \
-v elasticsearch-data:/usr/share/elasticsearch/data \
-e "discovery.type=single-node" \
elasticsearch:5.6-alpine
```

- List indexes: `curl -X GET localhost:9200/_cat/indices?v`

- Create index: `curl -X PUT  localhost:9200/wagtail?pretty`

- Create python container 

``` bash
docker run -it \
--hostname wagtail \
--rm \
--network wagtail-full-text-search-with-elasticsearch \
-p 8000:8000 \
python:3 /bin/bash
```

- Use alpine test hostname configuration 

``` bash
docker run -it \
--rm \
--network wagtail-full-text-search-with-elasticsearch \
alpine /bin/sh

ping elasticsearch
```


- Setup wagtail

``` bash
pip3 install Django wagtail "elasticsearch>=5.0.0,<6.0.0"

wagtail start mysite

pip3 install -r requirements.txt

python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver 0.0.0.0:8000
```

- Setup elasticsearch as backend for search

``` json
# mysite/settings/base.py
WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.search.backends.elasticsearch5',
        'URLS': ['http://elasticsearch:9200'],
        'INDEX': 'wagtail',
        'TIMEOUT': 5,
        'OPTIONS': {},
        'INDEX_SETTINGS': {},
    }
}
```





