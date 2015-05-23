#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'ahmao'
SITENAME = u'\u4e0d\u6094\uff0c\u5c31\u662f\u4e0d\u6094'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MD_EXTENSIONS = (['toc'])

# Blogroll
LINKS = None 

DISQUS_SITENAME = "ahmao"

# Social widget

SOCIAL = (('FB Group(ValleyRain)', 'http://www.facebook.com/groups/ValleyRain'),
          ('微信联系人(Tao)', 'http://weixin.qq.com/r/SH-27I3EjgDxrRmN9ypa'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Use bootstrap3 theme
THEME = 'themes/pelican-bootstrap3'
#FAVICON = 'images/favicon.ico'
BOOTSTRAP_THEME = 'cosmo'
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
