print("Welcome to Python Pizza Deliveries!!")
size = input("What is the size of the pizza L , M or S: ")
cheese = input("Do you want cheese on your pizza? Y or N: ")
extra_pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
price = 0

if(size=='S'):
    price = 15
    if(extra_pepperoni=='Y'):
        price+=2
elif(size=='M'):
    price = 20
    if(extra_pepperoni=='Y'):
        price+=3
else:
    price = 25
    if(extra_pepperoni=='Y'):
        price+=3
if(cheese=='Y'):
    price+=1

print(f"The price of the pizza is {price}")