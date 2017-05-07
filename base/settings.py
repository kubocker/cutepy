import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

######################
# Cute.py   SETTINGS #
######################

CANVAS = {
    'x': 1000,
    'y': 1000,
    'width': 650,
    'height': 1000
}

########################
# Cute.py APPLICATIONS #
########################

INSTALLED_APPS = (

)

#######################
# Cute.py STATICS     #
#######################

STATIC_URL = '/static/'

TEMPLATES = []

DATABASES = {
    'default': {
        'ENGINE': '',
        'NAME': os.path.join(BASE_URL, 'db.sqlite3'),
    }
}
