- Setup wagtail

``` bash
pip3 install Django wagtail 

wagtail start mysite

pip3 install -r requirements.txt

./manage.py migrate
./manage.py createsuperuser
./manage.py runserver 0.0.0.0:8000
```

