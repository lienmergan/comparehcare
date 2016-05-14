web: gunicorn backend.wsgi --log-file -
web: uwsgi --lazy --http-socket :$PORT --module backend.wsgi -L -p 4  -l 128 --check-static staticfiles --static-map /static=staticfiles


