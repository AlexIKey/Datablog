#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Олександр Курсік'
SITENAME = u"Stories with Data"
SITEURL = 'http://localhost:8000'
#SITELOGO = 'images/my_site_logo.png'
#HIDE_SITENAME = False
#DISPLAY_BREADCRUMBS = False

## Banner Image
#BANNER = '/path/to/banner.png'
#BANNER_SUBTITLE = 'This is my subtitle'
#BANNER_ALL_PAGES = True

TIMEZONE = u'Europe/Kiev'
LOCALE = u'uk_UA.utf8'
DEFAULT_LANG = u'uk'
DEFAULT_DATE_FORMAT = '%A %d %B %Y'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None


# CUSTOM_CSS = 'static/custom.css'
# STATIC_PATHS = ['figure', 'images','extra/robots.txt', 'extra/favicon.ico', 'extra/custom.css']
# EXTRA_PATH_METADATA = {
#     'extra/robots.txt': {'path': 'robots.txt'},
#     'extra/favicon.ico': {'path': 'favicon.ico'},
#     'extra/custom.css': {'path': 'static/custom.css'}
# }

LINKS = (('R-Bloggers',  'https://www.r-bloggers.com'),)

# Social widget
SOCIAL = (('linkedin',  'https://www.linkedin.com/in/oleksandr-kursik'),
          ('github',  'https://github.com/alexikey'),
         ('facebook',   'https://www.facebook.com/olexandr.kursik'),)
    

#DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')

DEFAULT_PAGINATION = 5

TAG_CLOUD_MAX_ITEMS = 10

DISPLAY_CATEGORIES_ON_MENU = False

DISPLAY_TAGS_ON_SIDEBAR = True



ROBOTS = 'index, follow'


# THEME
THEME = u"pelican-bootstrap3"
BOOTSTRAP_THEME = 'simplex'
BOOTSTRAP_FLUID = True
PATH = 'content'



MAIN_MENU = True
# MENUITEMS = (('Archives', '/archives.html'),
#  	     ('Categories', '/categories.html'),
#  	     ('Tags', '/tags.html'),)


# Plugin Setup
#NOTEBOOK_DIR = 'notebooks'
PLUGIN_PATHS = ['/home/alex/virtualenvs/pelican/pelican-plugins']
PLUGINS = ['i18n_subsites','rmd_reader'
           # 'liquid_tags.img', 'liquid_tags.video',
           # 'liquid_tags.youtube', 'liquid_tags.vimeo',
           # 'liquid_tags.include_code', 'liquid_tags.notebook'
           ]
# Enable Jinja2 i18n extension used to parse translations.
JINJA_EXTENSIONS = ['jinja2.ext.i18n']




RMD_READER_RENAME_PLOT = 'directory'
RMD_READER_KNITR_OPTS_CHUNK = {'fig.path': 'figure/'}




DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

LOAD_CONTENT_CACHE = False
#Localize settings
I18N_SUBSITES = {
     'uk': {
         'SITENAME': 'Олександр Курсік blog',
         'LOCALE': u'uk_UA.utf8'
         },
     # 'en': {
     #     'SITENAME': 'Oleksandr Kursik\'s blog',
     #     'LOCALE': 'en'
     # }
}

DATE_FORMATS = {
 	'en': ('en_US','%a, %d %b %Y'),
  	'uk': (u'uk_UA.utf8','%a, %d %b %Y'),
}

PYGMENTS_STYLE = 'zenburn'  