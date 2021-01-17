# conditinal statements 
x=2
if x==2:
    print("correct")
else:
    print("false")


"""num=input("enter the value:")
if num==2:
    print("correct")
else:
    print("false")
"""
#iteratives  for and while
for each in range(0,11):# range(m,n-1)
    print(each)

x=[1,2,3,4,5]
i=0
for each in x:
    print("tha value of index-{} is {}".format(i,each))
    i=i+1
# count the lengtt of the variable
y=[1,2,3,4,5]

print(len(y))
count=0
for each in y:
    count=count+1
print(count)
print(max(y))

# to count the repeated string
s="pyhtonlanguahepython"
i=0
for each in s:
    if each=="p":
      i=i+1
print("total count of p is:",i)
# to find the ma xvalue
x=[1,2,3,4,6,7,9]
max_value=x[0]
for each in x:
    if each>max_value:
        max_value=each
print(max_value)

#while if statement is true it will perform and false come out of the loop
x=1
while x<=10:
    print(x)
    x=x+1

#loop control statements:
#1continue
#2break
#pass

for each in range(1,20):
    if each==6:
        print("key found")
        break
print(each)

for each in [1,2,3,4,5]:
    if each==5:
       break
    print(each)
print("========================================")
#continue wil skip the iteration if the statement is true
for each in range(0,18):
    if each%2==0:
        continue
    print(each)
# pass will doesnt ipact the scrip means it will, not through an error
def hello():
    pass

        
#functions
def hello(a,b):# a,b are the parameters
   sum=a+b
   print(sum)
hello(3,3)





























