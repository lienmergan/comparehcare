# BAP CompareHCare

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone https://github.com/lienmergan/comparehcare.git
$ cd comparehcare

$ pip install -r requirements.txt

$ createdb mybap_django

$ python manage.py migrate

$ heroku local
```

The app should now be running on [localhost:5000](http://localhost:5000/).