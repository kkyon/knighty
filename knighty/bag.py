from PyQt4.QtCore import *
import unicodecsv
import codecs

class Bag(QObject):
    def __init__(self):
        super(Bag,self).__init__()
        self.map={}
        self.list=[]
        
    @pyqtSlot(str,str)    
    def addField(self,key,value):
  
        key=unicode(key)
        value=unicode(value)
        self.map[key]=value
        
    @pyqtSlot()        
    def saveRow(self):
        self.list.append(self.map);
        self.map={}
    def saveCsv(self,filename):
        fields=set()
        for row in self.list:
            #print row.keys()
            fields.update(row.keys())
        
        with open(filename, mode="w") as f:
            w = unicodecsv.writer(f, encoding='utf-8')
            w.writerow(fields)
            for row in self.list:
                values=[]
                for key in fields :                    
                    if key in row.keys() :
                        values.append(row[key])
                    else:
                        values.append("")
                    
                w.writerow(values)
 
            
        
    pass
 
 