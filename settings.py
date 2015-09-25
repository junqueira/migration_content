import json
import os

migration = {
                'BROKER_URL_AMQP': 'YOUR_BROKER_URL_AMQP',
                'URL_MIGRATE': 'YOUR_URL_MIGRATE'
}


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
try:
    from settings_local import *
    local = open(os.path.join(BASE_DIR,'settings_local.py')).read()
    exec(local)
except IOError:
	pass