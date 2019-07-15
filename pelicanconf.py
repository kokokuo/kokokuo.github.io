#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "kokokuo"
SITENAME = "koko's Note"
SITEURL = "https://note.koko.guru"

# Pelican 讀取的輸入目錄，也就是你的寫作目錄
PATH = "content"

TIMEZONE = "Asia/Taipei"

DEFAULT_LANG = "en"

# Flex Theme Settings : Indicate installed theme by pelican-themes command
THEME = "Flex"
SITETITLE = "koko's Note"
SITESUBTITLE = """
Code / Web / Architecture
<br/>
<br/>
你需要非常多的努力
<br/>
才能看起來毫不費力
"""

COPYRIGHT_NAME = "kokokuo"
COPYRIGHT_YEAR = 2019

FAVICON = "/static/favicon.ico"

# SITELOGO = "https://avatars3.githubusercontent.com/u/5389253?s=460&v=4"
SITELOGO = "/static/koko-logo.png"

# 設定哪些目錄或檔案，要被視為靜態文件，並且放置到輸出目錄下
STATIC_PATHS = [
    "images",
    "extra"
]
# 用來設定複製到輸出目錄時，該 extra/custom.css 會被投放對應的位置，這邊設定在 static
EXTRA_PATH_METADATA = {
    "extra/custom.css": {"path": "static/custom.css"},
    "extra/koko-logo.png": {"path": "static/koko-logo.png"},
    "extra/favicon.ico": {"path": "static/favicon.ico"},
    "extra/CNAME": {"path": "CNAME"},
}
# CUSTOM_CSS 是輸出成 HTML 時的該客製化 CSS 檔案的位置
CUSTOM_CSS = "static/custom.css"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (("Pelican", "http://getpelican.com/"),
#          ("Python.org", "http://python.org/"),
#          ("Jinja2", "http://jinja.pocoo.org/"),
#          ("You can modify those links in your config file", "#"),)

# Social widget
SOCIAL = (('github', 'https://github.com/kokokuo'),
          ('linkedin', 'https://www.linkedin.com/in/easonkuo'),)

DEFAULT_PAGINATION = 15

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
