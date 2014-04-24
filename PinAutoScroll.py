
from knighty import *

class PinAutoScroll(knighty) :
    
  
    followerbroad='http://www.pinterest.com/baker7549/wedding-dress/followers/'
    
    def __init__(self):
       super(PinAutoScroll, self).__init__()
       self.request(self.followerbroad,'GET',callback=self.scroll)
       
    def scroll(self,response):
        print response.status
        self.execjs('''
                    var lastn=0;
                    function s(){
                    var n=$.find('div.item').length;
                    
                    alert(n+' ' +lastn);
                    
                    if ( lastn < n){
                    lastn=n;
                    $("html, body").animate({scrollTop:$(document).height()}, 'slow');
       
                    setTimeout(s,5000); 
                    
                    }
                    };
                    
                     $(function(){
                       setTimeout(s,5000);               
                 
                 }
                 );
                    ''' )
        
     
                    
                    
PinAutoScroll.run()