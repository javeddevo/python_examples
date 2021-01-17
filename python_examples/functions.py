# functions is a set of statements

#parameters formed during the functioj creation
#arguments are created during function call

def hello(a,b,): # where a,b is formal parameters
    print("sum is:",a+b)
hello(10,20) # 10,20 areactual parameters


def hi(*all):#*allis the postive argumnets
    sum=0
    for each in all:
        sum=sum+each
    print("total sum:",sum)
hi(10,2,3,4)


#keyword arguments
def bye(**kw):
    for i,each in kw.items():
        print(i,"---->",each)
bye(key="value")

def new(name):
    print("new game",name)
new("cricket")


def sqrt(val):
    print("squareroot of the value",val,"is:",val*val)
sqrt(10)


def ad(a,b):
    return a+b #where return help to stores the result or value  in variable
result=ad(10,20)
print(result)
result1=ad(100,2002)
print(result1)


def no(a,b):
    sums=a+b
    mul=a*b
    sub=a-b
    return sums,mul,sub
re=no(23,3)
for each in re:
    print(each)

#lamba functio
# it is written in sible line
# for simplifying the code
m=lambda a,b : a+b
print("sum of and b is:",m(10,20))
y=lambda a:a*a
print("square is:",y(10))

def sq(val):
    print("square is:",val*val)
sq(100)

# doc string which help the other employes to understand the code when you leave the company
def intro():
    """this function is created in 2018 to know thevalues of the customers and this iis lis out all the slary o fthe customers"""

print(intro.__doc__) # to print the description of the function


"""def apple(a,b):
    return a+b
#if __name__=="__main__":
a=input("enter the value:")
b=input("enter the value:")
print("result is:",apple(a,b))
"""

def display():
    print("the value of a is:",a)
    print("tha value of b is:",b)
a=1
b=3
display()


def kk(a=0,b=2): #can metion default values as parameters
    print(a+b)
kk(3)
kk(7)


#defining values user message and result as parameters
def maths(p,q,user_message,result):
    print("the fisrt value is:",p)
    print("second value sis:",q)
    print("the",user_message," is:",result)
maths(2,3,"addition",2+3)
a=3
b=5
maths(a,b,"sub",a-b)






























    

































    









    























