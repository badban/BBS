# 中华蒲氏文化协会

This is a imitation 中华蒲氏文化协会
 forum using Python, Django, Bootstrap and MySQL.

## Requirements

- Python 3.5
- Django 1.11

## Usage

#### Clone
 ```
 git clone git@github.com:fsvu/V8EX.git
 ```

#### Making Model Changes
 ```
 Change Models in models.py
 python manage.py makemigrations
 python manage.py migrate
 ```

#### Create An Admin User
 ```
 python manage.py createsuperuser
 ```

#### Start The Development Server
 ```
 python manage.py runserver
 ```

## Project Structure
```
├── BBS
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-34.pyc
│   │   ├── settings.cpython-34.pyc
│   │   ├── urls.cpython-34.pyc
│   │   └── wsgi.cpython-34.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── README.md
├── app
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-34.pyc
│   │   ├── admin.cpython-34.pyc
│   │   ├── models.cpython-34.pyc
│   │   ├── urls.cpython-34.pyc
│   │   └── views.cpython-34.pyc
│   ├── admin.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── media
│   └── upload_imgs
│       ├── index.jpg
│       └── user-0.jpg
├── static
│   ├── css
│   │   ├── base.css
│   │   ├── bootstrap.min.css
│   │   └── navbar-fixed-top.css
│   ├── fonts/
│   └── js
│       ├── bootstrap.min.js
│       ├── jquery.min.js
│       └── search.js
└── templates
    ├── base.html
    ├── base_center.html
    ├── category.html
    ├── detail.html
    ├── index.html
    ├── login.html
    ├── node.html
    ├── post.html
    ├── reg.html
    ├── search.html
    └── userInfo.html
```

## LICENSE
```
The MIT License (MIT)

Copyright (c) 2016 Jiegao Zhu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
