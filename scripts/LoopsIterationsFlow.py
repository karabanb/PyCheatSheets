
import time

#############################################   LOOPS   ################################################################

for i in range(0, 10, 2):
    print(i)
    time.sleep(3)

####################################   ITERATING OVER OBJECTS    #######################################################

cubes = []

for i in range(10):
    cubes.append(i**3)

# list comprehensions

cubes = [i**3 for i in range(10)]  # list comprehension throws the same effect like for loop

