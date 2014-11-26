# twitter_search.py
# encoding: utf-8
# author: lili
# date: 2014-11-20
# introduction: input a query and return the clustered result from twitter api

import web, re, json, urllib
import time
import sys,os

from connect_twitter_api  import search 
from  similarity_score import compare
from star_clustering import star_clustering_result

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
        if(keyword):
            # connect twitter api and retrun the original result
            original_result = search(keyword)
            """
            f = file ('original_result','w')
            for i in range(0, len(original_result)):
                f.write(original_result[i].text)
            f.close()
            """
             
            # calculate the similarity score of two documents
            score = dict()
            for i in range (0, len(original_result)):
                for  j in range(i+1, len(original_result)):
                    score[(i,j)] = compare(original_result[i].text, original_result[j].text)
            print  time.clock()
            cluster = star_clustering_result(len(original_result), score)
            print cluster
            print time.clock()
            return render.submit(keyword,original_result,cluster)
        else:
            return  render.submit()
        

if __name__ == "__main__":
    app.run()
        
    
    


