number = int(input("please enter a number"))
even = 0
odd = 0
counter = 0
for i in range (1,number+1):
    if i%2 == 0:
        even += i
        counter +=1
    else:
        odd +=i
print("the avarage of the even numbers:" , even//counter)
print("the sum of the odd numbers:" , odd)
