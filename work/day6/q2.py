import random
lst = ["ridha","rimsha","sajitha","niha","irfan"]
random.choice(lst)

try:
    index = int(input("enter a preferred index number: "))
    if 0<=index<len(lst):
        print("name of the given index are : ",lst[index])
    else:
        print("index out of range")

except ValueError:
    print("invalid input")

print("random choice are: ",random.choice(lst))