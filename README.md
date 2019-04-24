Slink
=====

Link shortener service implemented in Python 3 and Django.

# Running

Assuming you have fish shell:

```
./install.fish
./run_dev.fish
```

or

```
docker-compose up
```

Django port is 8000, Docker exposes it to port 80.

# Routes

* `/` - main screen

* `/links/<link_id>` - link redirection

* `/admin/` - if you use `python3 slink/manage.py createsuperuser`
              admin panel is available

# Environment variables

Modify the following either in `run\_dev.fish` or `run\_prod.fish`.

* `DEBUG` - whether the application runs in debug mode

* `SECRET_KEY` - Django secret key

* `LINK_LENGTH` - generated link lenth

# Checking code style

```
./code_style.fish
```
