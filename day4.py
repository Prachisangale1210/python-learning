#Random Module:

import random
random_integer = random.randint(0,1)
print(random_integer)
if(random_integer==0):
    print("Heads")
else:
    print("Tells")


#Lists
states_of_india=["Assam","Bihar","Chandigarh","Delhi"]
print(states_of_india[0])
print(states_of_india[3])
print(states_of_india[-1])

#Who pay the bill?
friends = ["Aachal","Nikita","Prachi","Mayur","Satyam"]
print(random.choice(friends))
random_index = random.randint(0,4)
print(friends[random_index])
print(len(friends))