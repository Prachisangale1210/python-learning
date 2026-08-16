#Data Types
#---------------------------#
#1.Strings

#Subscripting
print("Hello"[0]) #H
print("Hello"[-1]) #o

#Concatenation
print("123"+"345")


#2.Integer
print(123+345)
print(123_456_789) #large integers

#3.Float
print(3.14159)

#4.Boolean - True or False

#type of the data
print(type("Hello"))
print(type(123))

#type conversion - int(),float(),str(),bool()
name = "123"
name = int(name) # do not modify the original variable we need to explicitly modified that
print(type(name))

#Basic Mathematical Operations
print(2-1)
print(3+2)
print(4*5)
print(6/3) #float result
print(6//3) #integer result
print(2**3) #power

#PEMDAS - parentheses, exponent , multiplication , division , addition , subtraction

#Number Manipulation
num = 23.89079
print(int(num)) #23
print(round(num)) #24
print(round(num,2)) #23.89

#F-string - convert all the data types into the string without the string function
score = 0;
height = 1.8;
print(f"Your score is {score} and your height is {height}") 




