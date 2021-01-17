"""import os
print(os.getcwd())# to get the cutrrent path
path="C:/Users/LAEEQAKBAR/Desktop"
if "india" in path:
    print("folder exits")
else:
    os.mkdir("india")
"""
#packing and unpacking
#tuple
a=("ram","rahul","krish") #packing 
(rank1,rank2,rank3)=a    # unpacking
print(rank1)

#list
b=["devops","linux","aws"] #packing
[cou1,cou2,cou3]=b #unpacking
print(cou1)
b=["linux","panda"]
[cou1,cou2]=b
print(cou1)

import os
print(os.listdir("."))#to list directories
os.mkdir("kk")
import os
print(os.getcwd())
f=open("hello.txt","w")
f.write("helloworl\n")
f.write("hey world\n")
f=open("hello.txt","a")#to append
f.write("heybro")
f.close()
f=open("hello.txt","r")
data=f.read()
print(data)

#f.close() is used to close the file
#f.closed is used to check whether file is closed or not
with open("hey.txt","w") as f:
    f.write("hey\n")
    f.write("jk\n")
    f.write("devops")
print("fileis closed or not:",f.closed)

print(os.getcwd())
path="C:/Users/LAEEQAKBAR/Desktop"
print(os.path.isfile("hello.txt"))




