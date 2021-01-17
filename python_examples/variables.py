#variables
#global
#local


#global variable
#which is acccessed in the whole programmme
#global variable is declared outside of the function

x=33
def hello():
    print(x)
def hello1():
    print(x)
def hello2():
    print(x)
hello()
hello1()
hello2()



#local variables:which is declared inside the function
x=44
def hi():
    x=22
    print(x)
def hi1():
    print(x)
hi()
hi1()

#note first preference goes to local variable if it is not decalred it will take from global variable

def ola():
    global p  #making local variable as global variable
    p=22
    print(p)
def ola1():
    print(p)
def ola2():
    print(p)
ola()
ola1()
ola2()

#calling global into local
f=88
def sky():
    t=99
    print(t)
    print(globals()['f'])
sky()


x="python"
print("\n".join(x))
y=2
z=7
print(x,y)
print(x,",",y)
















    
    



















