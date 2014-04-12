import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
import urllib
import json
import re
import time
import sqlite3
 
from urlparse import parse_qs

class response :
    pass
class knighty(QWidget):
 
  
    def __init__(self):
        super(knighty, self).__init__()
  
     
        self.view = QWebView(self)
        layout = QVBoxLayout(self)
        layout.addWidget(self.view)
 
        #view.setHtml(html)
        self.callback=None
        self.frame = self.view.page().mainFrame()
        self.view.loadFinished.connect(self._loadFinished)
        self.view.loadProgress.connect(self.print_percent)
        

         
    def request(self,url,method,data=None,callable=None,meta=None):
        self.callback=callable
        if method=='POST' :
            self.frame.evaluateJavaScript(data)
        elif method=='GET' :
            self.view.load(QUrl(url))
        else:
            raise BaseException()
            
    def execjs(self,js,callable=None,timeout=None):
        self.callback=callable
        print js
        self.frame.evaluateJavaScript(js)
        
    def print_percent(self, percent):
 
        print str(percent)+"%"
 
    def _loadFinished(self, result):  
        #print finished
        
        self.frame.evaluateJavaScript('<script src="http://code.jquery.com/jquery-1.11.0.min.js"></script>')
        self.frame.evaluateJavaScript('<script src="http://code.jquery.com/jquery-migrate-1.2.1.min.js"></script>')
        if self.callback is not None:
            res=response()
            res.url=self.view.url().toString()
            res.body=unicode(self.frame.toHtml())
            res.status=result
            self.callback(res)
            
    @classmethod    
    def run(cls):
        print type(cls)
        app = QApplication(sys.argv)
        window = cls()
        window.show()
        app.exec_()     
          
       
 