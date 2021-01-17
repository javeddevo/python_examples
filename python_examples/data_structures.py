#data structures
""""
list
tuple
set
dictionary"""

a=1,2,3
print(a)
print(type(a))
#default data structure is tuple

b=[1,2,3],[2,3,4] #it is a tuple
print(b)
print(type(b))



#list is mutable means can be modified

#immutable is you cant modify

c=[1,2,3,3,4]
d=[1,2,3,3,4]
e=c+d#to concatinate two list
print(e)
print(type(e))
new=[1,2,3,4]
del new[0] #to delete
print(new)
new.append(60)
print(new)
new.pop() # it will delete last value
print(new)
new.remove(2) # it will delete exact value
print(new)
new.append(5)
print(new)
print(new.count(3))
print(new)
new.insert(0,10)#index,value
print(new)
new1=["hello"]
new.extend(new1)
print(new)
new.reverse()
print(new)

#tuple is immutable you cant modify
helo=(1,2,3)
print(helo)
print(type(helo))
print(helo[:]) # it will list all the elemts
t=6*helo
print(t)

l=1,2,4
l=l*40# it will repeate 40 times
print(l)


#set mutable it will not accept dublicate values
import pprint
pprint.pprint(dir(set))
a={1,2,3}
b={4,5,6}
print(a.union(b))
a.add(4)
print(a)
a.clear()
print(a)
b.pop()
print(b)
b.remove(6)
print(b)

#frozenset  immutable
a={1,2,3,4,5}
b=frozenset(a) #to convert set to frozen set
print(type(b))


# dictonaries key:value
# always keys should be unique
a={"name":"javeed",
    "no":9020202,
    "address":"kphp"}
print(type(a))
print(a.get("name"))
print(a.setdefault("status","active"))# to add key and value
print(a)
for each in a.values(): # for getting values
    print(each,"-------->",type(each))
print("================================")
for each in a:
    if "name" in a.keys():
        print("key found")
    print (each)
print(a.pop("status")) # to delete the key
print(a)
print(a.popitem())  # it will delete the last value
print(a)
print(a.clear()) # it will clear all the values
print(a)



account={101:"jacved",103:"ram"}
print(account)
for k,v in account.items():
    print("account no is:",k,"name is:",v)
         

   





























