#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os

HERE = os.path.abspath(os.path.dirname(__file__))
PATH = os.path.join(HERE, 'content')

AUTHOR = u'team@mydev.my'
SITENAME = u'Laman Kolaboratif MyDev'
SITEURL = 'http://www.mydev.my'
RELATIVE_URLS = False
TIMEZONE = 'Asia/Kuala_Lumpur'

DEFAULT_LANG = u'en'

# Blogroll - This is required
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
           ('Python.org', 'http://python.org'),
           ('Jinja2', 'http://jinja.pocoo.org'),
           ('You can modify those links in your config file', '#'),)

# Social widget - This is required
#SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

MD_EXTENSIONS = ['toc', 'codehilite', 'extra', 'admonition']

STYLESHEETS = ('pygment.css', 'custom.css')

GOOGLE_ANALYTICS = 'UA-41580964-1'

FILES_TO_COPY = (
    ('extra/CNAME', 'CNAME'),
    ('images/mydev.jpg', 'images/mydev.jpg'),
)
DISQUS_SITENAME = 'mydevcommunity'

OPEN_GRAPH = True
OPEN_GRAPH_IMAGE = 'mydev.jpg'
