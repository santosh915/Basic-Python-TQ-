#!/usr/bin/env python
# coding: utf-8

# In[19]:


#1 write program to reverse number an integer in python

l = int(input())

l = str(l)
print(l[::-1])

l = input()

print(l[::-1])


# In[ ]:


#or
#reverse a number without using string function

def reverse_number(number):
    reversed_number = 0
    while number > 0:
        last_digit = number % 10
        reversed_number = (reversed_number * 10) + last_digit
        number = number // 10
    return reversed_number

number = int(input())
print(reverse_number(number))


# In[ ]:


#2 check armstrong number

num = int(input())
sum = 0
temp = num 
n = str(num)

while temp>0:
    digit = temp % 10
    sum += digit ** len(n)
    temp//=10
    
if num == sum:
    print("the number is armstrong number")
    
else:
    print("the number is not armstrong number")
    
    


# In[ ]:


# #3 to check prime or not prime 

n = int(input())

flag = False

if n == 1:
    print("the given number is not prime")
    
elif n>1:
    for i in range(2,n):
        if n%i==0:
            flag=True
            break
            
    if flag:
        print("the given number is not prime")
        
    else:
        print("the given number is prime")
                


# In[ ]:



#counting prime numbers in a range

def count_primes_in_range(start: int, end: int) :
    count = 0
    for num in range(start,end+1):
        if num >1:
            for i in range(2,num):
                if (num % i) ==0:
                    break
            else:
                count +=1
    return count

print(count_primes_in_range(1,10)) 


# In[ ]:





# In[1]:


#4 fibonacci using iterative method

n = int(input())
result = 0
first, second =0,1
print("fiboncci series are:")

for i in range(0,n):
    if i<=1:
        result=i
        
    else:
        result = first + second
        first = second
        second = result
    print(result)


# In[21]:


#5 fibonacci using recursive method

def fob_seq(n):
    if n <= 1 :
        return n
    
    else:
        return fob_seq(n-1) + fob_seq(n-2)
    
n = int(input())
if n <=1:
    print("fiaboncci is 1")
    
else:
    for i in range(n):
        print(fob_seq(i))


# In[ ]:


#6,7 pallindrome in number

n = int(input())

n = str(n)


rev = (n[::-1])

if n == rev:
    print("the given number is pallindrome")
    
else:
    print("it is not pallindrome number")


# In[ ]:


#8 greatest number in given:

n1 = int(input())

n2 = int(input())

n3 = int(input())

if n1>=n2 and n1>=n3:
    result = n1
    
elif n2>=n3 and n2>=n1:
    result = n2
    
else:
    result = n3
    
print(result)


# In[ ]:


#11 swapping two variables without using third variable 

x = int(input())

y = int(input())

x = x - y

y = x + y

x = y - x

print("after swapping x,y ",x,y)


# In[ ]:


#12 swapping numbers using third variables

x = int(input())

y = int(input())

temp = x 

x = y

y = temp

print("after swapping x,y ",x,y)


# In[12]:


#13 prime factors of given number


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n%i:
            i += 1
            
        else:
            n //= i
            factors.append(i)
            
    if n > 1:
        factors.append(n)
    return factors


n = int(input())

print(prime_factors(n))


# In[26]:


#15 to check given number is perfect 

n = int(input())
sum = 0
for i in range(1,(n//2)+1):
    remainder = n%i
    if remainder == 0:
        sum = sum + i
        
if sum == n :
    print("given number is perfect number")
    
else:
    print("given no. is not a perfect number")
    
    
    


# In[ ]:


#16 Average of list
s = [215,254]



avg = (sum(s))/(len(s))
print(avg)


# In[2]:


#17 factorial with iterative method

n = int(input())

factorial = 1

if n < 0:
    print("the factorial does not exist negative value")
    
elif n == 0:
    print("factorial of 0 is 1")

else:
    
    for i in range(1,n+1):
        factorial = factorial * i
    print(factorial)
    


# In[ ]:





# In[ ]:


# 18 factoral with recursive method

def factorial(n):
    if n == 1:
        return n 
    else:
        return n * factorial(n-1)
    
n = int(input())

if n < 0:
    print("the factorial does not exist negative value")
    
elif n ==0:
    print("factorial of 0 is 1")
    
else:
    print(factorial(n))


# In[ ]:


# 19 given no is even or odd:

n = int(input())

if n%2==0:
    print("the given number is even")
    
else:
    print("the given no is odd")


# In[ ]:


#20 21 prime number in given range

lower = int(input())
upper = int(input())
count = 0

for i in range(lower,upper+1):
    if i > 1:
        for n in range (2,i):
            if i%n==0:
                break
        else:
            print(i)
            


# In[ ]:


#22 smalllest number among three

n1 = int(input())
n2 = int(input())
n3 = int(input())

if  n1<=n2 and n1<=n3:
    result = n1 
    
elif n2<=n3 and n2<=n1:
    result = n2 
    
else:
    result = n3
    
print(result)


# In[28]:


#23,24 calculate power 

base = int(input())

exponent = int(input())

result = pow(base,exponent)
print(result)


# In[ ]:


# 25 square of given number 

n = int(input())

sq = n ** 2

#sq = n*n

print(sq)


# In[ ]:


#26 find the given no.of cube

n = int(input())

cube = n*n*n
#cube = n ** 3

print(cube)


# In[ ]:


#27 calculate square root


n = float(input())


sqrt = n ** 0.5

print(sqrt)


# In[ ]:


#29 lcm of two numbers

n1 = int(input())

n2 = int(input())

lcm = max(n1,n2)

while True:
    if (lcm % n1 ==0) and (lcm % n2==0):
        print(lcm)
        break
        
    else:
         lcm = lcm + 1
        


# In[ ]:


#30 gcd or hcf 

n1 = int(input())
n2 = int(input())

hcf = min(n1,n2)

while True:
    
    if n1%hcf ==0 and n2%hcf==0:
        print(hcf)
        break
    else:
        hcf = hcf-1


# In[ ]:


#34 check the given year is leap yr or non leap yr

yr = int(input())

if yr%400==0:
    print('leap yr')
    
elif yr%100==0:
    print('not a leap yr')


elif yr%4==0:
    print("the given yr is leap yr")

else:
    print("non leap yr")
    
    


# In[ ]:


#35 conversion of cel into fahrenheit

cel = float(input())

fahrenheit = (1.8*cel)+32

print(fahrenheit)


# In[ ]:


#36 fahrenheit to celcius

fahr = float(input())

cel = (fahr-32)/1.8
print("to take %0.2f"%cel)


# In[ ]:


#37 simple interest 

total_rs = int(input())
rate = int(input())
time = float(input("in year:"))

interest = (total_rs * rate * time)/100
print(interest)


# In[ ]:


##string


# In[ ]:


#1 remove character from string and replace


str1 = input()
ch = input()
print(str1.replace(ch,"_"))   #''


#input - santosh
#ch - 
#output - s_ntosh 


# In[ ]:



# 2 count characters in a string

str1 = input("plz entr a string ")

ch = input("enter a character")

result=str1.count(ch)
print(result)


# In[ ]:


#3 amogram string 

str1 = input("enter a string: ")

str2 = input("enter a another string: ")

str1 = str1.lower()

str2 = str2.lower()

if len(str1) == len(str2):
    l = sorted(str1)
    m = sorted(str2)
    
    if l == m:
        print("this strings are amogram")
        
    else:
        print("this strings are not amagrom")
        
else:
    print("this strings are not amagram")


# In[ ]:


#4  check pallindrome 

str1 = input("enter a string: ")

str1 = str1.lower()

str2 = str1[::-1]

if str1 == str2:
    print("given string is pallindome")
    
else:
    print("the given string is not pallindrome")
    


# In[ ]:


#5check given character in vowel or consonant 

i = input("enter a character: ")
i = i.lower()

if (i=="a" or i=="e" or i=="o" or i=="i" or i=="u"):
      print("given cha in vowel present ",i)
        
else:
      print("only consonants is present",i)


# In[ ]:


#6 given character is digit or not


str1 = input()

if str1>="0" and str1 <= "9":
    print("given character is digit ")
    
else:
    print("given character is not digit")
    


# In[13]:


str1 = input()

if str1.isdigit():
    print('the string contains only digits')
    
else:
    print('the string contains non digits charaters')
    
    


# In[14]:


#8,9 replace a string in space

string = input("enter a string: ")
space = ''
ch = input("enter acharacter: ")

for i in string:
    if i == ' ':  #give a space is compulsory 
        i=ch
    result = str1.join(i)
        
print(result)


# In[ ]:





# In[ ]:


str1 = input()
space = ' '
ch = input()

print(str1.replace(space,ch))


# In[ ]:


str1 = input()

ch = ' '



str1.replace(ch,input())


# In[ ]:


#10  lower case character to convert upper case

str1= input("enter a string: ")

str1 = str1.upper()
print(str1)


# In[ ]:


#11 lower case vowel to convert upper case

string = input("enter a :")

vowels = "aeiou"

for char in string:
    if char in vowels:
        upper_char = char.upper()
        string = string.replace(char,upper_char)
        
print(string)


# In[ ]:


#12 removing vowels in string

string = input("enter a string: ")

result = ""

for i in string:
    if i in ("a","e","i","o","u","A","E","I","O","U"):
        i = ""
        
    result += i
    
    
print(result)


# In[10]:


#to removing vowels

str1 = input() 

ch = 'aeiouAEIOU'
result = ''

for i in str1:
    if i in ch:
        i = ''
    result += i
        
print(result)


# In[ ]:


str1 = input() 

result = ''

for i in str1:
    if i in 'aeiouAEIOU':
        i = ''
    result += i
        
print(result)


# In[ ]:


#13 count vowels and consonent 

string = input("enter a string : ")

vowels = 0

consonent = 0

for i in string:
    if i in ('a','e','i','u','o','A','E','I','O','U'):
        vowels += 1
        
    elif i.isalpha():
        
        consonent += 1       
  
print("vowels are: ",vowels ,"and consents are",consonent)


# ###### 

# In[14]:



#14 highest frequency character

string = input('please enter a string: ')

freq_dict = {}

for char in string:
    if char in freq_dict:
        freq_dict[char] += 1
        
    else:
        freq_dict[char] = 1
        
max_freq = max(freq_dict.values())

for char in freq_dict:
    if freq_dict[char] == max_freq:
        print(char,end='')


# In[ ]:


#15 replace first vowel in string with '_'

def replace_vowel(string):
    vowels = 'AEIOUaeiou'
    
    for i in range(len(string)):
        if string[i] in vowels:
            string = string[:i] + '_' + string[i+1:]
            break
            
    return string 

string = input('plz enter a string: ')
print('original string : ',string)
print('modified string : ',replace_vowel(string))


# In[19]:





# In[ ]:


#16  count alphabets,digits and special characters in the string:

string = input('enter a string : ')

alphabets = 0

digits = 0

specialchars = 0


for i in string:
    
    if i.isalpha():
        alphabets += 1
        
    elif i.isdigit():
        digits += 1
        
    else:
        specialchars += 1
        
#it calculate the space in special character

print('alphabets = ',alphabets,'digits = ',digits,'specialchars = ', specialchars)


# In[ ]:


# 17 seperate characters in astring

string = input()

for char in string:
    print(char)


# In[ ]:


#18 remove all blank spaces in a given string

string = input('enter a string : ')
result = ''

for i in string:
    if i != ' ':
        result += i
        
print(result)


# In[ ]:





# In[ ]:


str1 = input()
#space = ' '

print(str1 .replace(' ',''))


# In[ ]:


#19 concatenate two string using join function

str1 = input('enter a string : ')

str2 = input('enter a string : ')

print('concatenate of two strings :',''.join([str1, str2]))


# In[ ]:


#20 joing two strings without join function

str1 = input('enter a string: ')

str2 = input('enter a string :')

str1.replace(' ','')
concatenate = str1  + str2
print(concatenate)


# In[ ]:


#21 remove repeated character in a string///unique character in string

def remove_duplicates(string):
    unique_chars = set()
    output = ""
    for char in string:
        if char not in unique_chars:
            unique_chars.add(char)
            output += char
            
    return output

string = input('enter a string : ')

print(remove_duplicates(string))


# In[ ]:


def remove_duplicates(string):
    
    unique = set()
    
    output = ''
    
    space = ' '
    for char in string:
        if char in space:
            output += char
            
        
        elif char not in unique :
            unique.add(char)
            output += char
            
    return output

string = input()

print(remove_duplicates(string))


# In[ ]:


#22 sum of integers in the strings

str1 = input('enter a string: ')

sum = 0

for i in str1:
    
    if i.isdigit():
        
        sum = sum + int(i)
        
print("sum of numbers:",sum)


# In[ ]:


#23 find all non repeating charactersin a string

string = input('please enter a string: ')

freq_dict = {}

for char in string:
    if char in freq_dict :
        freq_dict[char] += 1
        
    else:
        freq_dict[char] = 1
        
non_repeating_chars = ""
for char in string:
    if freq_dict[char] == 1:
        non_repeating_chars += char
        
print("non repeating chars:",non_repeating_chars)


# In[ ]:


#24 copy one string to another string

str1 = input("enter a string")

str2 = str(str1)

#str2 = str1

print('the new string is:',str2)


# In[ ]:





# In[ ]:


string = input('Enter a string : ')

if string >= '0' and string <= '9':
    print(string,'False')

else:
    print(string,'True')


# In[ ]:


a = int(input())
b = int(input())
    
    
    print(int(a/b))
    
    print(float(a/b))


# In[ ]:


n = int(input())

for i in range(0,n):
    n = i * i
    print(n)


# In[ ]:


def is_leap(year):
    leap = False

    if year % 400 == 0: 
        return True 
    if year % 100 == 0: 
        return False 
    if year % 4 == 0: 
        return True 
    return False



year = int(input())
print(is_leap(year))


# In[ ]:


#if select input 5 : output [1,2,3,4,5]

n = int(input())
    
for i in range(1,n+1):
    
    print(i,end='')
        


# In[ ]:


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    a = []
    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):
                if i+j+k!=n:
                   a.append([i,j,k])
print(a)
        


# In[ ]:


if __name__ == '__main__':
    student = []
    for _ in range(int(input())):
        name = input('enter name')
        score = float(input('enter score'))
        student.append([name, score])
    # print(student)

    # Make an Empty List which stores the Marks
    marks = []
    for k in student:
        # Value = k[1]
        marks.append(k[1])

    # From the marks we will get the second minimun Value and store it
    second_min =  sorted(set(marks))[1]

    # We will store the Name, Which has same marks as Second minimun
    name = []
    for i in student:
        if i[1] == second_min:
            name.append(i[0])

    # print(name)
    # Print the name in Alphabetical order
    for name in sorted(name):
        print(name)


# In[ ]:


import numpy as np
print(np.polyval(list(map(float, input().split())), float(input())))

# 2.1 2 6
#0


# In[7]:


def mutate_string(string, position, character):

    return string[:position] + character + string[position + 1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
    
# santosh/
# 3 k 


# In[ ]:


def count_substring(string, sub_string):
    start = 0
    end = len(string)
    count = 0
    
    while(True):
        if string.find(sub_string, start, end) != -1:
            start = string.index(sub_string, start, end) + 1
            count += 1
        else:
            break
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
    
#ABCABCABC
#ABC
#OUTPUT 3


# In[ ]:


def string_validation(s):
    


    print (any(s.isalnum()for s in s))
    print (any(s.isalpha()for s in s))
    print (any(s.isdigit()for s in s))
    print (any(s.islower()for s in s))
    print (any(s.isupper()for s in s))

    return
if __name__ == '__main__':
    s = input() 
    string_validation(s)


# In[ ]:


import textwrap


def wrap(string, max_width):
    a = textwrap.wrap(string, max_width)
    i = '\n'.join(a)
    return(i)
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    
#input saaaaaaaaaaaaa
#   3
#otput saa
#aaa
#aaa
#aaa
#aaa


# In[ ]:


from collections import Counter

EMPTY_COUNTER = Counter()

def MinWindowSubstring(strArr):
    
    N, K = strArr
    frequencyK = Counter(K)
    options = []
    for i in range(len(N)):
        curr = Counter()
    for j in range(i, len(N)):
        curr[N[j]] += 1
    if frequencyK - curr == EMPTY_COUNTER:
        options.append(N[i:j + 1])
        break
    return min(options, key=len)
      

# keep this function call here 
print(MinWindowSubstring(input()))


# In[ ]:


#strings important questions


# In[17]:


'''
Sample Input

this is a string   

Sample Output

this-is-a-string'''

def split_and_join(line):
    a=line.split(" ")
    f="-".join(a)
    return f
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# In[13]:



# given string
s = "geeksforgeeks"
k = 2
 
# dictionary for mapping
mp = {}
 
# mapping over the string
for char in s:
    if char in mp:
        mp[char] += 1
    else:
        mp[char] = 1
 
for char in s:
    if mp[char] == 1:
        k -= 1
        if k == 0:
            print("The K’th Non-repeating Character is:")
            print(char)
            # break after you get the correct output
            break


# In[ ]:


#Python code for the same approach
def replaceSpaces(input):
    rep = "%20"
    for i in range(len(input)):
        if(input[i] == ' '):
            input = input.replace(input[i],rep)
    print(input)
 
# driver code
input = "Mr John Smith"
replaceSpaces(input)
 
# This code is contributed by shinjanpatra


# In[ ]:


# Python3 program to convert given sentence
# to camel case.

# Function to remove spaces and convert
# into camel case
def convert(string):
    while True:
        i = 0
        while i < len(string):
            if string[i] == ' ':
                string = string[:i] + string[i+1:].capitalize()
                # Terminate inner loop after removing a space and making character next to it as capital
                break
            i += 1
        # Terminate outer loop when we reach to the end of string
        if i == len(string):
            break
    return string


# Driver program
if __name__ == '__main__':
    string = "I get intern at geeksforgeeks"
    print(convert(string))


# In[ ]:





# In[ ]:


#1 reverse string 
s = "Hello world"
' '.
join(w[::-1] for w in s.split())


    
    
    


# In[9]:



def print_words(s):
    # word variable to store word
    word = ""
 
    # making a string stream
    iss = s.split()
 
    # Read and print each word.
    for i in iss:
        word = i[::-1]
        print(word, end=" ")
 
 
# Driver code
if __name__ == '__main__':
    s = "Geeks for Geeks is good to learn"
    print_words(s)


# In[ ]:



# A Python3 program to find a maximum
# product of a triplet in an array of integers
 
# Function to find a maximum product of a
# triplet in array of integers of size n
def maxProduct(arr, n):
 
    # if size is less than 3, no triplet exists
    if n < 3:
        return -1
 
    # Sort the array in ascending order
    arr.sort()
 
    # Return the maximum of product of last
    # three elements and product of first
    # two elements and last element
    return max(arr[0] * arr[1] * arr[n - 1],
               arr[n - 1] * arr[n - 2] * arr[n - 3])


 
# Driver Code
if __name__ == "__main__":
 
    arr = [10, 1, 5, 15, 20]
    n = len(arr)
 
    _max = maxProduct(arr, n)
 
    if _max == -1:
        print("No Triplet Exists")
    else:
        print("Maximum product is", _max)


# In[ ]:





# In[ ]:





# In[ ]:


#round up figure

import math

def round_up_to_nearest_50_or_100(number):
    if number % 50 == 0:
        return number
    elif number % 100 == 0:
        return number
    else:
        return math.ceil(number / 50) * 50

number = 56





print(round_up_to_nearest_50_or_100(number)) # Output: 1250


# In[ ]:


#second largest number

list1 = [10, 20, 4, 45, 99,489,12]
max_num = list1[0]
second_max = list1[0]
for i in range(1,len(list1)):
    if list1[i] > max_num:
        second_max = max_num
        max_num = list1[i]
    elif list1[i] > second_max and list1[i] != max_num:
        second_max = list1[i]
print(second_max)

second_min = list1[0]
for i in range(1,len(list1)):
    if list1[i] < max_num:
        second_min = max_num
        max_num = list1[i]
    elif list1[i] < second_min and list1[i] != max_num:
        second_min = list1[i]

print(second_min)
    


# In[ ]:


# two number are equla or not equal
numbers = input("Enter two comma-separated numbers: ")
num1, num2 = numbers.split(",")
if num1 == num2:
    print("The numbers are equal")
else:
    print("The numbers are not equal")


# In[ ]:


list1 = [10, 20, 4, 45, 99]
list1.sort()
print(list1[-2])
print(list1[1])


# In[ ]:


#second minimum
list1 = [10, 20, 4, 45, 99]
max_num = list1[0]
second_max = list1[0]
for i in range(1,len(list1)):
    if list1[i] < max_num:
        second_max = max_num
        max_num = list1[i]
    elif list1[i] < second_max and list1[i] != max_num:
        second_max = list1[i]
print(second_max)


# In[ ]:


#write a program to implement a function that takes a list of integers 
#as input and return the sum untill total should be a single digit number

def sum_list(list1):
    s = sum(list1)
    if s < 10:
        return s
    else:
        return sum_list([int(i) for i in str(s)])

list1 = [11,22,33,44,55]
print(sum_list(list1))


# In[ ]:


#remove the extra spaces

string1 = "  Hello       World!  "
string1 = " ".join(string1.split())
print(string1)


# In[ ]:





# In[ ]:


#11 lower case vowel to convert upper case

string = input("enter a :")

vowels = "aeiou"

for char in string:
    if char in vowels:
        upper_char = char.upper()
        string = string.replace(char,upper_char)
        
print(string)


# In[ ]:


string = input("enter a :")

vowels = "aeiouAEIOU"

result = ''

for i in string:
    if i in vowels:
        
        
         print(i)


# In[ ]:


#3 to check prime or not prime 

n = int(input())

flag = False

if n == 1:
    print("the given number is not prime")
    
elif n>1:
    for i in range(2,n):
        if n%i==0:
            flag=True
            break
            
    if flag:
        print("the given number is not prime")
        
    else:
        print("the given number is prime")


# In[ ]:


#sort a list
list1 =[99,25,21,23,54,120]

list1.sort()
print(list1)


# In[ ]:


#remove common elements from array

import numpy as np

a = [1,2,3,4,5,7]
b = [3,4,5,6]

a = np.array([1,2,3,4,5,7])

b = np.array([3,4,5,6])

result = np.setdiff1d(a,b)

print(result)


# In[ ]:


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

res_list1 = list(set(list1) - set(list2))
res_list2 = list(set(list2) - set(list1))

print(res_list1)
print(res_list2)


# In[ ]:


my_list = [1, 2, 3, 4, 3, 2]
res = list(set(my_list))
print(res)


# In[ ]:


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3 = list1 + list2

list3 = list(set(list1))
print(list3)


# In[ ]:


#unique character in string

def unique_characters(string):
    unique_chars = set()
    for char in string:
        unique_chars.add(char)
    print(list(unique_chars))
    
string = input()
unique_characters(string)


# In[ ]:


#21 remove repeated character in a string
#unique
def remove_duplicates(string):
    unique_chars = set()
    output = ""
    for char in string:
        if char not in unique_chars:
            unique_chars.add(char)
            output += char
            
    return output

string = input('enter a string : ')

print(remove_duplicates(string))


# In[ ]:


#count duplicate character in string

def count_duplicates(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in char_count:
        if char_count[char] > 1:
            print(char, char_count[char])
            
string = "aabccbdcbe"
count_duplicates(string)


# In[ ]:


#remove extra spaces in string
def remove_extra_spaces(string):
    return " ".join(string.split())

string = "  This is   a    string  with extra   spaces.  "
print(remove_extra_spaces(string))


# In[ ]:



# python code to reverse words in a given string

# input string
string = "i like this program very much"

# spliting words in the given string
# using slicing reverse the words
s = string.split()[::-1]

# joining the reversed string and
# printing the output
print(" ".join(s))


# In[ ]:



def longestcommonprefix(a):
    size = len(a)
    
    if (size==0):
        return ''
    
    elif (size == 1):
        return a[0]
    
    a.sort()
    
    end = min(len(a[0]),len(a[size-1]))
    i = 0
    while (i < end and a[0][i]== a[size -1][i]):
        i += 1
    pre = a[0][0: i]
    return pre
if __name__ == "__main__":
    
    input = ["geeksforgeeks", "geeks", "geek", "geezer"]
    
    print(longestcommonprefix(input))

