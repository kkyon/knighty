Knighty
=======

A python automation library with webkit. 

#Dependency
* Python 2.7
* Pyqt4
You can download pyqt4 it from 

http://www.riverbankcomputing.com/software/pyqt/download

#Example 1 pinterest.com  Auto Follow

This is a example for login pinterest.com and auto follow a user list. Code is revised to load full follower list. 


    username='username' # your pinterest account 
    password='password' # password
	 # any page have interesting user list
    followerbroad=http://www.pinterest.com/baker7549/wedding-dress/followers/'
	
#Example 2 Google search result scraping.

	new object 'Bag' is added for communication between javascript and python code. see the sample .
	
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
		
		In javascript code ,you need to save value by API .
		
		Bag.addField(key1,value1);
		Bag.addField(key2,value2);
		Bag.saveRow();		
		Bag.addField(key1,value1);
		Bag.addField(key2,value2);
		Bag.saveRow();
		
		In python code, you can manipulate the store by self.Bag.list or use bulit-in function 'saveCsv'
				
		
