#!/usr/bin/env python
# coding: utf-8

# Write a python script that asks the user for the values of x and y and uses these inputs to
# compute the numerical value of the expression
# :

# In[2]:


import math
x=int(input("Donner x:"))
y=int(input("Donner y:"))
print(math.sqrt(x**2+y)/(1/x+math.sin(y)))


# Write a function that given two integers b and n (n is positive), calculates bn without using
# python’s power operator. Name this function ownpowerfn.py.

# In[11]:


def ownpower(b,n):
    p=1
    for i in range(0,n):
        p=p*b
    return p
ownpower(2,3)


#  PS: What if we do not specify that n has to be positive?

# In[26]:


def ownpower(b,n):
    p=1
    m=1
    if n>0:
        for i in range(0,n):
            p=p*b
    elif n==0:
        p=1
    else:
        for i in range(0,abs(n)):
            p=p*(1/b)
    return p
        
ownpower(2,-2)


# Write functions that do the following:
# a.)Takes two arguments, and computes their arithmetic and geometric means. Name
# these functions arithmetic_mean and geometric_mean respectively.
# 
# 

# In[28]:


def arithmetic_mean(n,m):
    return (n+m)/2
arithmetic_mean(10,10) 
    


# In[33]:


def  geometric_means(n,m):
    return ((n*m)**(1/2))
geometric_means(3,5)


# b) Converts degree Celsius to Fahrenheit and vice versa. Name these two functions
# celcius_to_fahrenheit and fahrenheit_to_celcius respectively.

# In[39]:


def celcius_to_fahrenheit(t):
    return (t* 9/5) + 32 
celcius_to_fahrenheit(5)


# In[41]:


def fahrenheit_to_celcius(t):
    return 5/9*(t-32)
fahrenheit_to_celcius(41)


# c) Converts angle in degrees to radians and vice versa. Name these two functions
# degrees_to_radians and radians_to_degrees respectively.

# In[44]:


def degrees_to_radians(an):
    import math
    return an*math.pi/180
degrees_to_radians(8)


# In[46]:


def radians_to_degrees(anr):
    import math
    return (anr*180)/math.pi
radians_to_degrees(0.13962634015954636)


# 
# d) Computes the circumference and the area of a circle given the radius

# In[47]:


import math
r=int(input("Donner le rayon:"))
print("La circonference du cercle est:",2*math.pi*r)
print("L'aire du cercle est:",math.pi*r*r)


# 4. Write functions that do the following:
# a) Given two numbers, compute their average and geometrical mean and prints them.
# Now write a program that performs this process 10 times, taking as input the means
# computed in the previous step. Name this function avggeom.

# In[60]:


def  avggeom(n,m):
    p=(n+m)/2
    t= ((n*m)**(1/2))
    print(p,t)
    i=1
    while i<10:
        n=(t+p)/2
        m=((n*m)**1/2)
        print(n,m)
        i=i+1
avggeom(5,8)


# b) Write a function that computes the distance between two points in the plane. Use
# it in another program that computes the perimeter and the area of a triangle, given
# three points in the plane. Name this function distancefn

# In[63]:


def distancefn(p1,p2):
    import math
    p1=(x1,y1)
    p2=(x2,y2)
    return math.sqrt((x2-x1)**2+(y2-y1)**2)


# In[ ]:


p1=(3,4)
p2=(6.4)
p3=(2,1)


# Write a program that offers three options to the user:
# 1.Evaluation of actorial
# 2.Evaluation of a second degree equation
# 3. Exit
# The user selects one of the options and then the program requests the data needed and
# calls the corresponding function to produce a result. The program then repeats the process
# until the user says he wants to exit. Name this function fact2nddeg.

# In[ ]:


def factorial(n):
    f=1
    if n==0 or n==1:
        return 1
    else:
        for i in range(1,n+1):
            f=f*i
    return f
def secondd(a,b,c):
    delta=b**2-(4*a*c)
    if delta==0:
        print("Solution double")
    elif delta>0:
        print('deux solutions')
    else:
        print("Pas de solution")
def fact2nddeg():
    import sys
    option=int(input("Choisissez une option:"))
    if option==0:
        sys.exit()
    elif option==1:
        (t,p,o)=int(input("Donner t,p,o:"))
        secondd(t,p,o)
    else:
        m=int(input("Donner m:"))
        factorial(m)
    option=int(input("Choisissez une option:"))
    while option!=0:
        fact2nddeg()
fact2nddeg()


# 6. For a fixed real number x and a natural number n, we can define recursively xn using the
# relations:
# x0 = 1 and xn+1 = x:xn:
# Write a function power(x,n) that implements the above recursion.
# 

# In[4]:


def recursion(n,x):
    x0=1
    x1=x
    p=1
    for i in range(1,n+1):
        p=p*x1
        x0=x1
        x1=p
    return p
recursion(2,4)


# 7. Write code that implements the Fibonacci sequence. Test your program at 100

# In[6]:


f0=1
f1=1
f=0
n=int(input("Donner un entier:"))
print(f0,'\n',f1)
for i in range(1,n):
    f=f0+f1
    print(f)
    f0=f1
    f1=f


# In[ ]:




