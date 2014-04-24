# -*- encoding: utf-8 -*-
from knighty import *
 
class GoogleSearch(knighty) :

    def __init__(self):
       super(GoogleSearch, self).__init__(jslatency=False)
       self.request('https://www.google.com?hl=en','GET',callback=self.search)
       self.keyword='computer'
       
    def search(self,response):
    
        self.execjs('''
   
            $("input[name=q]").val("%s");
            $("input[name=q]").parents("form").submit();
                '''%self.keyword,
                callback=self.parse_list
                 )
     
                
    def parse_list(self,response):
        self.execjs('''
   
            $("li.g").each(function(i){
                var title=$(this).find("h3").text();
                Bag.addField('title',title);
                var link=$(this).find("div div.kv cite").text();
                Bag.addField('link',link);
                Bag.saveRow();
                }
            );
             Bag.addField('test Field','ccc');
                Bag.saveRow();
                '''  
                 )
        self.Bag.saveCsv('google.csv')  
    
    
GoogleSearch.run(proxy='127.0.0.1:8087')