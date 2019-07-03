1. Create network: `docker network create full-text-search-playground`

2. Run mysql

``` bash
docker run --rm \
--network full-text-search-playground \
-e MYSQL_ALLOW_EMPTY_PASSWORD=yes \
-e MYSQL_DATABASE=test \
-p 3306:3306 \
mysql --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci --default-authentication-plugin=mysql_native_password
```


3. Run python container: 

``` bash
docker run -it \
--rm  \
--network full-text-search-playground \
-p 8000:8000 \
python:3 /bin/bash
```
