#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import logging

AUTHOR = "kokokuo"

# Website Information  ===
SITENAME = "koko's Note"
SITEURL = ""
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

TIMEZONE = "Asia/Taipei"
DEFAULT_LANG = "en"

FAVICON = "/static/favicon.ico"

# SITELOGO => "https://avatars3.githubusercontent.com/u/5389253?s=460&v=4"
SITELOGO = "/static/koko-logo.png"

# Social Widget ==========
SOCIAL = (('github', 'https://github.com/kokokuo'),
          ('linkedin', 'https://www.linkedin.com/in/easonkuo'),)


"""
== Theme ==========
- Indicate installed theme by pelican-themes command, used Flex
"""
THEME = "themes/Flex"

"""
== Input Content Root ======
- 讀取的輸入目錄，也就是你的工作目錄 (即便改掉或不填也沒影響，主要看你的專案目錄 Folder 是否為 content 名稱來影響是否可以產生內容)
"""
PATH = "content"

"""
== Category ===============
- Use the `posts` folder as category.
- If USE_FOLDER_AS_CATEGORY set False, then the default category will be posts because we set DEFAULT_CATEGORY.
- DEFAULT_CATEGORY will work when USE_FOLDER_AS_CATEGORY set False.
"""
DEFAULT_CATEGORY = "posts"
USE_FOLDER_AS_CATEGORY = True

"""
== Tags ==========================
- TAG_URL, TAG_SAVE_AS, TAGS_SAVE_AS currently use default value.
"""
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}.html'
TAGS_SAVE_AS = 'tags.html'

"""
== Menu Item ====================
- Format => (Title, URL.html)
- If using MENUITEMS to defined menu list, the DISPLAY_PAGES_ON_MENU and DISPLAY_PAGES_ON_MENU both need set False.
- Need to set MAIN_MENU is True to make MENUITEMS work when using Flex theme.
"""
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

# 文章列表與標籤沿用 Template 提供的 archives.html 與 tags.html
# 但是下面會透過 THEME_TEMPLATES_OVERRIDES 修改這兩個 Template
MENUITEMS = (
    ('關於我', '/pages/about.html'),
    ('文章列表', '/archives.html'),
    ('標籤', '/tags.html'),
    ('軟體開發', '/pages/software-development.html'),
    ('理財投資', '/pages/financial-investment.html'),
)

"""
== PAGE URL & SAVE_AS  ===============
- PAGE_URL, PAGE_SAVE_AS currently use default value.
"""
PAGE_URL = 'pages/{slug}'
PAGE_SAVE_AS = 'pages/{slug}.html'

"""
== Article URL & SAVE_AS ==============
- ARTICLE means the markdown we wrote
- ARTICLE_URL, ARTICLE_SAVE_AS use post as a prefix url.
"""
ARTICLE_URL = 'posts/{slug}'
ARTICLE_SAVE_AS = 'posts/{slug}.html'

"""
== Pagination ============================
- Format => (minimum_page, page_url, page_save_as,)
"""
PAGINATION_PATTERNS = (
    (1, "{url}", "{save_as}"),
    # (1, "{base_name}", "{base_name}/index.html"),
    (2, "{base_name}/pagination/{number}/", "{base_name}/pagination/{number}/index.html"),
)


"""
== Static Path ================
- 設定哪些目錄或檔案，要被視為靜態文件，並且放置到輸出目錄下
"""
STATIC_PATHS = [
    "images",
    "static",
    "resources",
]

"""
== Extra Path Metadata ========================================
- 用來設定複製到輸出目錄時，使該 extra/custom.css 會被投放對應的位置，這邊設定在 static，其他的也是檔案亦是。
- README :使得 Github Repo 可以看得到檔案，為了避免被 Pelican 判斷成要轉換為文章的 markdown，須先設定為無格式，在此轉換。
- CNAME : Github 客製化網址使用。
- 另外因 README 與 CNAME 需要放在根目錄下，所以不指定在 static 之中
"""
EXTRA_PATH_METADATA = {
    "static/custom-style.css": {"path": "static/custom-style.css"},
    "static/koko-logo.png": {"path": "static/koko-logo.png"},
    "static/favicon.ico": {"path": "static/favicon.ico"},
    "resources/CNAME": {"path": "CNAME"},
    "resources/README": {"path": "README.md"},
}


"""
== Flex Theme Custom Setting ========
- MAIN_MENU is True will make MENUITEMS work in Flex theme.
"""
MAIN_MENU = True
# If True hide URL hash => 可以使點文章擊連結時，不會跳轉到文章標題的位置，連結的跳轉可以參考 Flex 下 templates/index.html 
DISABLE_URL_HASH = True
# CUSTOM_CSS 是輸出成 HTML 時的該客製化 CSS 檔案的位置
CUSTOM_CSS = "static/custom-style.css"

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

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

LOG_FILTER = [(logging.DEBUG)]
