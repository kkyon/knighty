
from knighty import *

class PinAutoFollow(knighty) :
    
    username='username'
    password='password'
    followerbroad='http://www.pinterest.com/baker7549/wedding-dress/followers/'
    
    def __init__(self):
       super(PinAutoFollow, self).__init__()
       self.request('https://www.pinterest.com/login/','GET',callback=self.login)
       
    def login(self,response):
        print response.status
        self.execjs('''
                    $("input[name=username_or_email]").val("%s");
                    $("input[name=password]").val("%s");
                    $("form").submit();
                    '''% (self.username,self.password),
                    callback=self.followerlist)
        
    def followerlist(self,response):
       #open follower list page
       self.request(self.followerbroad,'GET',callback=self.follow)
     
    def follow(self,response):
       self.execjs('''
       var lastn=0;
                    function s(){
                    var n=$.find('div.item').length;                    
          
                    
                    if ( lastn < n){
                        lastn=n;
                        $("html, body").animate({scrollTop:$(document).height()}, 'slow');       
                        setTimeout(s,5000); 
                    
                    }else{
                           $("button:contains('Follow')[data-element-type='62']").each(
                                function(index){
                                    var e=$(this);
                                    setTimeout(function() {
                                                        e.click();
                                                        $('html, body').animate({
                                                        scrollTop: e.offset().top-200
                                                        }, 'slow');
                                                        
                                                      
                                                        
                                                            },(index+1)*5000);
                                    } 
                        );
                    
                    }
                    };
                    
                     $(function(){
                       setTimeout(s,5000);               
                 
                 }
                 );
                 
                    
       
                    '''
                    )
                    
                    
                    
PinAutoFollow.run()