"""
oops:
1.class
2.object
3.method
4.polymorphisim
5.inheritance
6.data abstraction

class:plan or template is called class.with plan object is created
object:execution of class is called object

function sinside the class are caleed methods
"""
class Hello():
    def hi(self,name,course,timing):
        self.pname=name
        self.pcourse=course
        self.ptiming=timing
    def info(self): # any menthod inside the class is universal means you can access the method in other function
        print(self.pname)
        print(self.pcourse)
        print(self.ptiming)
p1=Hello()
p2=Hello()
p1.hi("javed","devops",2) # here your are calling the values
p2.hi("ram","linux",3)
print(p1.pcourse)
p1.info()
p2.info()



class Jk():
    def httpd(self):
        self.port=404
        self.conf="server/xml"
    def display_info(self):
        print(self.port)
        print(self.conf)
httpd_info=Jk()
httpd_info.httpd()
httpd_info.display_info()
#============================================================================
# def __init__

class Jk():
    #def httpd(self):
      def __init__(self):#by this you dont need to call 
          self.port=404
          self.conf="server/xml"
      def display_info(self):
        print(self.port)
        print(self.conf)
httpd_info=Jk()
#httpd_info.httpd() you dont need to call 
httpd_info.display_info()
#============================================================================

class Bo():
    def __init__(self,name,course,timing):
        self.pname=name
        self.pcourse=course
        self.ptiming=timing
    def display(self):
        print(self.pname,self.pcourse,self.ptiming)
info=Bo("javeed","dev",33) #you can call arguments directly while assigning class to object
info.display()

#data hiding
class Jk():
    #def httpd(self):
      def __init__(self):#by this you dont need to call 
          self.port=404
          self.__conf="server/xml"#(__if u give this while assignng value to varibale it cant be callled)data hiding or abstarction
      def display_info(self):
        print(self.port)
        print(self.conf)
httpd_info=Jk()
print(httpd_info.port)
#print(httpd_info.conf)     
#==========================================================================
#inheritence genes from the parent
#polymorphism is same method name under different classes
class Parent():
   def __init__(self,name,age):
       self.pname=name
       self.page=age
   def display(self):
        print(self.pname)
        print(self.page)


class Hey():
    def __init__(self,name,age,rollno):
         Parent.__init__(self,age,name)
         self.prollno=rollno
    def display(self):
        Parent.display(self)
        print(self.prollno)
class Teach():
    def __init__(self,name,age,subject):
          Parent.__init__(self,age,name)
          self.psubject=subject
    def display(self):
         Parent.display(self)
         print(self.psubject)
        
std1=Hey("javed",33,33)
std1.display()

tec1=Teach("kav",22,"eng")
tec1.display()

# method overloading means same method used for  multiple times in different ways
#def hello(age)
#def hello(age,name)
#def hello(age,name no)

#data hiding(__is the private key)
class Data():
    def __init__(self):
        self.__salary=2000
    def display(self):
        print(self.__salary)
d=Data()
d.display()
d.salary=3000
d.display()




        



















































