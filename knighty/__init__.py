# -*- encoding: utf-8 -*-
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
import os
from bag import Bag
from PyQt4.QtNetwork  import *

class response :
    pass
class nam(QNetworkAccessManager):
    pass

 

def get_jquery(jslatency=True):
  
    f = open(os.path.join(os.path.dirname(__file__), 'jquery-1.11.0.min.js'))
    jquery = f.read()
    f.close()
    if jslatency :
        return '<script>'+jquery+'</script>'
    else:
        return jquery
class KWebpage(    QWebPage):
    def userAgentForUrl (self,url):
        return "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:8.0) Gecko/20100101 Firefox/8.0"    
class knighty(QApplication):
 
  
    def __init__(self,jslatency=True):
        super(knighty, self).__init__(sys.argv)
        self.jquery = get_jquery(jslatency)
        self.Bag=Bag()       
        self.view = QWebView()
        self.page= KWebpage()
        self.view.setPage(self.page)
        #layout = QVBoxLayout(self)
        #layout.addWidget(self.view)

        self.view.show()
        self.frame=self.page.currentFrame()
        self.connect(self.view, SIGNAL("loadFinished(bool)"),
            self._loadFinished)
            
        self.view.page().mainFrame().javaScriptWindowObjectCleared.connect(
                self._addBag)
        #self.connect(self.view.page.mainFrame(), SIGNAL("javaScriptWindowObjectCleared"),
        #    self._addBag)
            
        
        #self.set_load_function(None)
        
        ##view.setHtml(html)
        #self.callback=None
        #self.frame = self.view.page().mainFrame()
        self.network_manager = QNetworkAccessManager()
        self.network_manager.createRequest = self._create_request
        self.page.setNetworkAccessManager( self.network_manager)
        #
        
        self._addBag()
        
        #self.view.loadFinished.connect(self._loadFinished)
        #self.view.loadProgress.connect(self.print_percent)
        self.view.settings().setAttribute(
             QWebSettings.DeveloperExtrasEnabled, True)
        #self.inspector = QWebInspector(self)
        #self.inspector.setPage(self.view.page())
        #self.inspector.show()
        #self.splitter = QSplitter(self)
        #self.splitter.addWidget(self.view)
        #self.splitter.addWidget(self.inspector)
        #layout = QVBoxLayout(self)
        #layout.addWidget(self.splitter)
        #QShortcut(QKeySequence('F7'), self,
        #    self.handleShowInspector)
    def _addBag(self):
        self.page.mainFrame().addToJavaScriptWindowObject("Bag", self.Bag)
    def _create_request(self, operation, request, data):
     
        #if request is not None:
        #    print request.url()
     
        reply = QNetworkAccessManager.createRequest(self.network_manager,
                                                    operation,
                                                    request,
                                                    data)
        return reply
    def handleShowInspector(self):
        self.inspector.setShown(self.inspector.isHidden())     
    def request(self,url,method,data=None,callback=None,meta=None):
       
        self.callback=callback
        if method=='POST' :
            self.frame.evaluateJavaScript(data)
        elif method=='GET' :
            self.frame.load(QUrl(url))
        else:
            raise BaseException()
            
    def execjs(self,js,callback=None,timeout=None):
   
        #nm=self.frame.page().networkAccessManager()
        self.callback=callback
        #print js
     
        self.frame.evaluateJavaScript(js)
        
    def print_percent(self, percent):
 
        print str(percent)+"%"
 
    def _loadFinished(self, result):  
        #print finished
        
        #self.frame.evaluateJavaScript('<script src="http://code.jquery.com/jquery-1.11.0.min.js"></script>')
        self.frame.evaluateJavaScript(self.jquery)

        if self.callback is not None:
            res=response()
            res.url=self.view.url().toString()
            res.body=unicode(self.frame.toHtml())
            res.status=result
            self.callback(res)
            
    @classmethod    
    def run(cls,proxy=None):
        #print type(cls)
        if proxy is not None :
            host,port=proxy.split(':')
            QNetworkProxy.setApplicationProxy(QNetworkProxy(QNetworkProxy.HttpProxy, host, int(port)))
        app = cls() 
        app.exec_()     
          
       
 