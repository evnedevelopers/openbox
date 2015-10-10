# -*- coding: utf-8 -*-

import requests
from subprocess import call

api_url = 'http://api.forismatic.com/api/1.0/?method=getQuote&format=json&jsonp=parseQuote'

data = requests.get(api_url).json()
print(data['quoteText'])
call(["cinnamon-screensaver-command", "-l", "-m", data['quoteText']])