class ssc:    #class 10th
    name="Rio"
    pno=1234567
    age=23 
    
    def __init__(self,sloc,sname,percent,year):
        self.sloc=sloc
        self.sname=sname
        self.percent=percent
        self.year=year
    def display(self):
        print(self.sloc,self.sname,self.percent,self.year,self.name,self.age,self.pno)

class dip(ssc):    #diploma
    def __init__(self,cgpa,cloc,dyear,cname,sloc,sname,percent,year):
        self.cgpa=cgpa
        self.cloc=cloc
        self.dyear=dyear
        self.cname=cname
        super().__init__(sloc,sname,percent,year)
    def display(self):
        super().display()
        print(self.cgpa,self.cloc,self.dyear,self.cname)

class deg(dip):     #degree
    def __init__(self,sgpa,dloc,byear,dname,cgpa,cloc,dyear,cname,percent,sloc,year,sname):
        self.sgpa=sgpa
        self.dloc=dloc
        self.byear=byear
        self.dname=dname
        super().__init__(cgpa,cloc,dyear,cname,percent,sloc,year,sname)
    def display(self):
        super().display()
        print(self.sgpa,self.dloc,self.byear,self.dname)

all=deg(9,"Pune",2023,"ICOER",8,"thane",2020,"GSV",82,"Ahemdabad",2017,"JVA")
all.display()
        
    
