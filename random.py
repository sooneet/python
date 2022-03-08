import random
print('print random number from list is :',end='')
print(random.choice([10,20,30]))

print ("A random number from range is : ",end="")    
print(random.randrange(10,100,10))

print("The random number between 0 and 1 is : ", end="")  
print(random.random)
print(random.seed(4))