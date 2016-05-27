# CompareHCare

## Running the app locally

- Create a free [Heroku account](https://signup.heroku.com/signup/dc).
- Make sure Python version 2.7 (at least) is installed locally - see the installation guides for [OS X](http://docs.python-guide.org/en/latest/starting/install/osx/),
[Windows](http://docs.python-guide.org/en/latest/starting/install/win/), and [Linux](http://docs.python-guide.org/en/latest/starting/install/linux/).
- Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

- Assure that Setuptools and Pip are installed locally. See the Python install guides above for installation instructions.
- Take care that you have a virtual environment installed locally. Accomplish this by running `pip install virtualenv`.
- In the top-level directory of your project, create a virtual environment for your project `virtualenv venv`.
- To activate the virtual environment use `$ venv\Scripts\activate` (Windows) or `$ source venv/bin/activate` (not Windows.). And this in the project root.
- Use `deactivate` to leave the virtual environment.
- Check the database information by `heroku pg:info --app bap-comparehcare`
- To establish a psql session with the remote database use `heroku pg:psql --app bap-comparehcare`.

Follow these steps:

```sh
$ heroku login

$ git clone https://github.com/lienmergan/comparehcare.git
$ cd comparehcare

$ pip install -r requirements.txt

$ pip install virtualenv

$ virtualenv venv

$ source venv/bin/activate

$ heroku pg:info --app bap-comparehcare

$ heroku pg:psql --app bap-comparehcare

$ heroku pg:pull DATABASE_URL mylocaldb --app bap-comparehcare

$ heroku local web
```

The app should now be running on [localhost:5000](http://localhost:5000/).
Login with the admin credentials (see txt file) into the admin [localhost:5000/admin](http://localhost:5000/admin)
or go to the API at [localhost:5000/www/api](http://localhost:5000/www/api).
