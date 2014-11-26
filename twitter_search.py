# twitter_search.py
# encoding: utf-8
# author: lili
# date: 2014-11-20
# introduction: input a query and return the clustered result from twitter api

import web, re, json, urllib

# set encoding utf-8
import sys, os
reload (sys)
sys.setdefaultencoding('utf-8')

# define urls
urls = (
      '/','index',
      '/submit','submit'
      )

app = web.application(urls, globals())
render = web.template.render('templates/')

# the index page
class index:
    def GET(self):
        return render.index()

# the submit page
class submit:
    def GET(self):
        # get the query
        i = web.input()
        keyword = i.get('query')
        return render.submit(keyword)

if __name__ == "__main__":
    app.run()
        
    
    


