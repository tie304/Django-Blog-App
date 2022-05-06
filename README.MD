# Django Blog App

A Revolutionary new blogging system.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) or [poetry](https://python-poetry.org/) to install Django Blog App.

```bash
pip install -r requirements.txt
```

OR
```bash
poetry install
```

## Usage

```bash
 cd myapp
```
Run migrations
```bash
python manage.py migrate
```
Start server
```bash
python manage.py runserver
```
## Methods
> (GET, POST )Create  or list blog posts: localhost:8000/post

> (GET, PUT, DELETE) Manage specifc Post  localhost:8000/post/<id>

>(POST, GET) Create or Get User localhost:8000/user/<id>

> (POST) Add Like to Post localhost:8000/post/like/<post_id>/<user_id>

## License
[MIT](https://choosealicense.com/licenses/mit/)