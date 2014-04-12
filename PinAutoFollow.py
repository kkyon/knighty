
from knighty import *

class PinAutoFollow(knighty) :
    
    username='username'
    password='password'
    followerbroad='http://www.pinterest.com/baker7549/wedding-dress/followers/'
    
    def __init__(self):
       super(PinAutoFollow, self).__init__()
       self.request('https://www.pinterest.com/login/','GET',callable=self.login)
       
    def login(self,response):
        print response.status
        self.execjs('''
                    $("input[name=username_or_email]").val("%s");
                    $("input[name=password]").val("%s");
                    $("form").submit();
                    '''% (self.username,self.password),
                    callable=self.followerlist)
        
    def followerlist(self,response):
       #open follower list page
       self.request(self.followerbroad,'GET',callable=self.follow)
     
    def follow(self,response):
       self.execjs('''
                   $(function(){
                $("button:contains('Follow')[data-element-type='62']").each(
                            function(index){
                                var e=$(this);
                                setTimeout(function() {e.click();},(index+1)*5000);
                                } 
                        );
                        }
                    );
       
                    '''
                    )
                    
                    
                    
PinAutoFollow.run()