import twitter
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

api=\
twitter.Api(consumer_key='QyQhX9AMryjItOVKt2NML8BOY',     \
        consumer_secret='m5n560gpccsvhVYytSE9M5XYEMSNLA2CYFSZ52Uu0L3s80cQWX',\
        access_token_key='2851407324-YKTqodpywkuaSTyhWIu47mYYI0d7GHg0kIICR3z',\
        access_token_secret='yuBrZfncjTubi7IuXAQOA2CAoKmWTMu6SOlmZFuzFCyOX')


def search(query):
   statuses = api.GetSearch( term = query, geocode=None, since_id=None, max_id = None, until = None,count = 20,
        lang=None, locale=None, result_type='recent', include_entities=None)
   return statuses

