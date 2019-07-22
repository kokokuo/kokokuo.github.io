#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "kokokuo"
SITENAME = "koko's Note"
SITEURL = ""

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

"""
Tag 設置參數，其他未出現的參數保持預設可以參考。
http://docs.getpelican.com/en/4.1.0/settings.html#url-settings
"""
# 目前 TAG_URL, TAG_SAVE_AS, TAGS_SAVE_AS 皆保持預設
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}.html'
TAGS_SAVE_AS = 'tags.html'


"""
Pagination 設置參數，未出現的參數為預設狀態，可以參考
http://docs.getpelican.com/en/4.1.0/settings.html#pagination
"""
PAGINATION_PATTERNS = (
    (1, "{url}", "{save_as}"),
    # (1, "{base_name}", "{base_name}/index.html"),
    (2, "{base_name}/page/{number}/", "{base_name}/page/{number}/index.html"),
)

# ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
# ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

FAVICON = "/static/favicon.ico"

# SITELOGO = "https://avatars3.githubusercontent.com/u/5389253?s=460&v=4"
SITELOGO = "/static/koko-logo.png"

# 設定哪些目錄或檔案，要被視為靜態文件，並且放置到輸出目錄下
STATIC_PATHS = [
    "images",
    "extra"
]
# 用來設定複製到輸出目錄時，使該 extra/custom.css 會被投放對應的位置，這邊設定在 static，其他的也是檔案亦是。
# README :使得 Github Repo 可以看得到檔案，為了避免被 Pelican 判斷成要轉換為文章的 markdown，須先設定為無格式，在此轉換。
# CNAME : Github 客製化網址使用。
# 另外因 README 與 CNAME 需要放在根目錄下，所以不指定在 static 之中
EXTRA_PATH_METADATA = {
    "extra/custom.css": {"path": "static/custom.css"},
    "extra/koko-logo.png": {"path": "static/koko-logo.png"},
    "extra/favicon.ico": {"path": "static/favicon.ico"},
    "extra/CNAME": {"path": "CNAME"},
    "extra/README": {"path": "README.md"},
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

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
