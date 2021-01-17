"""basic data types
int
float
complex
string
"""
#float
x=2.1e78  #exponential form where big value is storing in less momeory
print(x)
print(type(x))

#complex number(X+YJ)whereY is imaginary part and X is real part 
x=2+3j
print(x)
print(type(x))

#============================================================
x,y=0b11,0B101
z=0b101010
print(y)
print(x,y)
print(type(x))
#binary integer 0 - start with 0b or 0B  base value is 2


#octal 0-7 start with 0o or 0O base value i s8
z=0o134
i=0o245
print(i)
print(z)


#hexadecimal(0-9) a-f or A-F start with 0x or 0X
i=0xfac9
k=0xaf346
print(k)
print(i)

#Typecasting
#integer to float
x=3
y=float(x)
print(type(y))
print(y)
#integer to string
c=str(3)
print(c)
print(type(c))
#ninteger to boolean
d=bool(x)
print(d)
#integer to complex
e=complex(x)
print(e)


# string to integer
"""f="hi"
g=int(f)
print(g)

#string to float
h=float(f)
print(h)
#string to complex
i=complex(f)
print(i)
"""
#float to integer
a=2.3
b=int(a)
print(b)
#float to str
c=str(a)
print(c)
#float to boolean
d=bool(a)
print(d)
#float to complex
e=complex(a)
print(e)
# boolean to integer
f=True
g=int(f)
print(g)
h=float(f)
print(h)
i=complex(f)
print(i)
g=str(f)
print(g)

#complex to inter str bool float
x=2+3j
y=str(x)
print(y)
#z=int(x)
#print(z)
#cant convert complex to string
#z=float(x)
#print(z)
# cant convert complex to float
z=bool(x)
print(z)












































































