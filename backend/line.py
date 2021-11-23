class line :
    linecontent = None
    sindex = 0
    eindex = 0
    mark = 0
    metadatacount = 0
    def __str__(self) -> str:
        return self.linecontent
    
    def set(self,x,sind,eind):
        self.linecontent = x
        self.sindex = sind
        self.eindex = eind
        self.mark = 0 
        self.metadatacount = 0
    
    def display(self):
        print("linecontent",self.linecontent)
        print("line start index",self.sindex)
        print("line end  index",self.eindex)
        print("metadata count",self.metadatacount)
    
    def getstartindex(self):
        return self.sindex

    def getendindex(self):
        return self.eindex

    def setmark(self):
        self.mark = 1
    
    def getmark(self):
        return self.mark
    
    def getlinecontent(self):
        return self.linecontent