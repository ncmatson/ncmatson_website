AUTHOR = 'N. Cameron Matson'
SITENAME = 'N. Cameron Matson'
SITEURL = 'https://ncmatson.com'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'https://getpelican.com/'),
#          ('Python.org', 'https://www.python.org/'),
#          ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
CONTACT = (
            ('linkedin', 'https://www.linkedin.com/in/n-cameron-matson/'),
            ('github', 'https://github.com/ncmatson'),
            # ('ncmatson AT gatech DOT edu', '#'),
          )

DEFAULT_PAGINATION = False
DISPLAY_CATEGORIES_ON_MENU = False

STATIC_PATHS = ['images', 'pdf', 'extra']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                       'extra/favicon.ico': {'path': 'favicon.ico'}
                       }
# FAVICON = 'favicon.ico'

THEME = "themes/bootstrap"
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
