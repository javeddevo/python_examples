#string formating
a=4
c=5
print("the vlue of a and c is:{},{}".format(a,c))

print("hey {name}.where is {name1}".format(name="jhon",name1="kasi"))


#string indexng
x="python"
print(x[0])
print(x[-1])
print(x[1:])

#slicing a[start:end:step]
x="india"
print(x[1:4]) #m,n-1
print(x[1:100:2])
print(x[-1])
print(x[1::2])

#position of the index

hello="helloworld"
print(hello.index("o"))
print(hello.index("h"))


a="python"
b="scripting"
new=a+b
print(new)
print(a+" "+b) #string concatination
print("======================================================")
import pprint
pprint.pprint(dir(str))

new="hello world"
print(new.upper())
print(new.lower())
print(new.capitalize())
print(new.title())
print(new.isnumeric())
print(new.startswith("f"))
print(new.endswith("d"))
print(new.partition("hello"))
print(new.ljust(1))
p="java 1.2.3"
print(p.split()[-1]) #$$
hi= "this is java"
print(hi.strip())
print(new.replace("hello world","hellodevops"))#$$$
print(p.lstrip("java"))















