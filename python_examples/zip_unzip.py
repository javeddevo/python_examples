import os
from zipfile import*
print(os.getcwd()) # to get current working directory
os.chdir("C:/Users/LAEEQAKBAR/Desktop/scripting_aws")
print(os.getcwd())
with open("file200.txt","w") as f: #to create a file
    f.write("hello\n")
    f.write("world\n") #f.close() not necessary when u use with open
with open("file201.txt","w") as f:
    f.write("hi\n")
    f.write("wooorld\n")
f=ZipFile("data_files.zip","w",ZIP_DEFLATED)
f.write("file200.txt")
f.write("file201.txt")
f.close()
print("successfully zipping is done")
"""k=ZipFile("data_files.zip","r",ZIP_STORED)
name=k.namelist()# its is function to unzip
for each in name:
    c=open(name,"r")
    print(c.read())
    print()
"""
