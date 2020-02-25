import random
people=[]

for i in range(0,8):
    person=input("enter the names ")
    people.append(person)

index=random.randint(0,7)
random_person=people[index]
print("picking a random person",random_person)