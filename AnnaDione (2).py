#!/usr/bin/env python
# coding: utf-8

# somme des i allant de 0 a n-1 de i+3 avec i impaire
# produit des i+3 pour i pair

# In[4]:


n=int(input("Donner un entier n:"))
s=0
p=1
for i in range(1,n):
    if i%2!=0:
        s=s+(i+3)
    else:
        p=p*(i+3)
        
print("La somme est:",s)
print("Le produit est:",p)


# Write a program that reads the number of the day of the week (from 0 to 6). If it is a
# working day, then the program will write the name of the corresponding day. Otherwise,
# it will write the word "Weekend".

# In[10]:


n=int(input("donner un entier entre 0 et 6:"))
if n==0:
    print("lundi")
if n==1:
    print("mardi")
if n==2:
    print("mercredi")
if n==3:
    print("jeudi")
if n==4:
    print("vendredi")
if n==5 or n==6:
    print("Weekend")


# Make a program that, given a month number (from 0 to 11), indicates how many days it
# has (28, 30 or 31), ignoring the leap years

# In[2]:


n=int(input("donner un entier entre 0 et 11:"))
if n==0:
    print(31)
if n==1:
    print(28)
if n==2:
    print(31)
if n==3:
    print(30)
if n==4:
    print(31)
if n==5:
    print(30)
if n==6:
    print(31)
if n==2:
    print(30)
if n==7:
    print(31)
if n==8:
    print(30)
if n==5 or n==9:
    print(31)
if n==5 or n==10:
    print(30)
if n==5 or n==11:
    print(31)


# 4. Write two versions of python code that displays your name 3 times. One version with a
# "for loop" and another version with a "while loop".

# In[6]:


myname="Anna DIONE"
for i in range(0,3):
    print(myname)


# In[7]:


myname="Anna DIONE"
i=0
while i<3:
    print(myname)
    i=i+1


# Given two numbers a0 and a1, the Fibonacci sequence they generate is constructed from
# the recursion formula an+1 = an + an-1. Calculate the first 15 terms of a Fibonacci
# sequence, asking the user the initial values

# In[11]:


a0=1
a1=1
f=0
print(a0,'\n',a1)
for i in range(0,13):
    f=a0+a1
    print(f)
    a0=a1
    a1=f


# 6. Compute the first 30 terms of the sequence defined by 2xn+2-xn+1 -6xn = 0 sequence,
# given any two initial values x0 and x1

# In[ ]:


x0=0
x1=1
s=0
print(x0,'\n',x1)
for i in range(0,98):
    s=s+((x1+6*x0)/2)
    print(s)
    x0=x1
    x1=s


# In[ ]:





# In[ ]:





# a) Write python code to determine whether or not a year is a leap year. Be sure you
# know what a leap year is.
# 

# In[15]:


n=int(input("Donner l'annee: "))
if n%400!=0:
    print(n, " is a leap year.")
else:
     print(n, " is not a leap year.")
    


# b) Write the code using only logical operators, i.e. no conditional branching.

# In[27]:


n=int(input("Donner l'annee: "))
x=" is a leap year."
y=" is not a leap year."
result=(x,y)[n%400==0]
print(result)
    


# In[ ]:





# Write python code that computes the sum of the square of the first n natural numbers.
# One version with a "for loop" and another version with a "while loop".
# 

# In[18]:


from math import sqrt
n=int(input("Donner n: "))
s=0
for i in range(1,n):
    s=s+sqrt(i)
print(s)


# In[19]:


from math import sqrt
n=int(input("Donner n: "))
s=0
i=1
while i<n:
    s=s+sqrt(i)
    i=i+1
print(s)


# b) Write python code that prints, for a natural number M, the smallest natural number
# n such that 1^2+2^2+.........+n^2 >= M: One version with a "for loop" and another version
# with a "while loop".
# 

# In[80]:


M=int(input("Donner M: "))

if M==0 or M==1 or M==2:
    print(M)
s=0
for i in range(1,M):
    s=s+i**2
    if s>=M:
        print(i)
        break

        
        


# In[83]:


M=int(input("Donner M: "))
if M==0 or M==1 or M==2:
    print(M)
s=0
i=1
while i<M:
    s=s+i**2
    i=i+1
    if s>=M:
        print(i-1)
        break
    
        
       


# a) Write python code that prints all the divisors of a given natural number.

# In[87]:


n=int(input("Donner n: "))
print("Les diviseurs de ",n," sont:")
for i in range(1,(n//2)+1):
    if n%i==0:
        print(i)


# b) Read an integer number input by the user and calculate its prime factors. This will
# just be some of its divisors.

# In[5]:


import math
n= int(input("Donner n:"))
while n%2==0:
       print(2)
       n=n//2
for i in range(3,(n//2)+1,2):
       while n%i==0:
           print(i)
           n=n/i
if n>2:
       print(n)


# Read an integer number between n 0 and 9 and print its multiplication table up to N
# where N is another another natural number read by the program.

# In[8]:


n= int(input("Donner n l'entier pour lequel vous voulez sa table de multiplication:"))
N=int(input("Donner N l;entier pour lequel vous voulez vous arretez pour la multiplication:"))
print("La table de multiplication de ",n," jusqu'a",N, "est:")
for i in range(0,N+1):
    print(n,"x",i,"=",n*i)


# Write a program that prints all the numbers between 0 and 40 that are multiples of 3, 7 or 11

# In[10]:


for i in range(0,41):
    if i%11==0 or i%7==0 or i%3==0:
        print(i)


# Write python code that prints the floor of a float x. Recall that the floor of a float x is the
# largest integer value less than or equal to x, i.e. if E[x] is the floor of x, then it satisfies,
# E[x] = 1 + E[x-1]
# PS: On Friday, you will be asked to write a recursive version

# In[5]:


import math
def floor(x):
    return math.ceil(x)-1
floor(3.8)


# 13. Given a point in the plane by its Cartesian coordinates, determine in which quadrant it is
# (1st, 2nd, 3rd, 4th), if it lies on an axis, or if it is the origin. Do this for several points in
# the same execution of the program until the user quits.

# In[ ]:





# Ask for an integer number between 0 and 9, denoted x. Once the user has entered a correct
# number (that is one in the range [0..10)) the program asks for a second integer number
# between 0 and 255, denoted max. The program continues asking for the number until it
# is correct (that it is in the range [0..256)). When this is done, show all multiples of x that
# are between 0 and max. Then, ask the user whether he/she wants to continue; if in the
# affirmative, ask for another couple of numbers, otherwise finish.

# In[1]:


import sys
x= int(input("Donner x: "))
if x in range(0,10):
    maxx= int(input("Donner maxx:"))
    while maxx not in range(0,256):
        maxx= int(input("Donner maxx:"))
    for i in range(0,maxx):
        if i%x==0:
            print(i)
Q=int(input("Taper sur n'importe quelle touche  pour continuer et 0 pour quitter"))
if Q==0:
    sys.exit()
    
else:
    while Q !=0:
        x= int(input("Donner x: "))
        if x in range(0,10):
            maxx= int(input("Donner maxx:"))
        while maxx not in range(0,maxx):
            maxx= int(input("Donner maxx:"))
        for i in range(0,255):
            if i%x==0:
                print(i)
        Q=int(input("entrer sur n'importe quel entier non nuul  pour continuer et 0 pour quitter"))


    


# In[ ]:




