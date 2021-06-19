import random
import numpy as np
import matplotlib.pyplot as plt
switchAndWon=0
switchAndLost=0
remainAndLost=0
remainAndWon=0
infoArray=[] #stores all the results later
#these variables are outside the for loop because they are general and are always counting from the beginning
#they don't reset every trial
for i in range(10000):#10,000 trials
    randDoor = np.random.random_integers(1, 3, 1)  # random door 1-3
    prizeDoor = np.random.random_integers(1, 3, 1)  # prize door 1-3

    randNum = np.random.random_integers(1, 2, 1) #determines if the player switches or not
    if randNum == 1:#player switches
        Switch = True
        if randDoor == prizeDoor:
            switchAndLost = switchAndLost + 1 #logic: if originally the user had the door with the prize and now he switches, then he , then he will 100% not have the prize, so it is a loss
        if randDoor != prizeDoor:
            switchAndWon = switchAndWon + 1 #logic: if originally the user doesn't have the door with the prize, but now also knows the one that doesn't have the prize, then he will always pick the one that will have the prize

    if randNum == 2: #player doesn't switch and stays the same
        Switch = False
        if randDoor == prizeDoor:
            remainAndWon = remainAndWon + 1 #logic: if the player already has the door with the prize and he doesn't switch, then he wins while staying the same.
        if randDoor != prizeDoor:
            remainAndLost = remainAndLost + 1 #logic: if the player doesn't have the door with the prize and he doesn't switch, then he loses while staying the same

for z in range(switchAndLost):
 infoArray.append("switch and lost")
for d in range(switchAndWon):
 infoArray.append("switch and won")
for u in range(remainAndLost):
 infoArray.append("remain and lost")
for e in range(remainAndWon):
 infoArray.append("remain and won")


 #in lines 28-35,I am appending the frequency of the categories in word form to an array, so that it becomes easier for the histogram to make a graph

plt.hist(infoArray,align="mid",color="blue")
plt.title("Monty Hall")
plt.xlabel("Categories Result")
plt.ylabel("Frequency")
plt.show()

#probabilites are 16.66% for remain and lost & switch and won
#probabilities are 33.33% for remain and won & switch and lost
print(remainAndLost)
print(remainAndWon)
print(switchAndWon)
print(switchAndLost)