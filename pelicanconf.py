#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'katsuya0719'
SITENAME = 'Help page'
SITEURL = ''

THEME = 'C:/Users/obakatsu/Documents/Python_scripts/pelican-themes/pelican-themes/bootstrap2'

PATH = 'content'

TIMEZONE = 'Asia/Hong_Kong'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('EP post processing tool', 'http://getpelican.com/'),
         ('Group promotion database', 'http://python.org/'),
         ('Gitlab', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images']
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
