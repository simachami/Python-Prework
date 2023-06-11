my_list = []
print(my_list)
my_list = list()
print(type(my_list))

#index 0,1,2,3,4
numbers = [2,6,10,12.5,0]
print(numbers)
print(type(numbers))

print(numbers[1])
print(type(numbers[1]))
#print([2,6,10,12.5,0][1])
#print(numbers[1]*2.5)

print(numbers[3])
print(type(numbers[3]))


foods = ["pizza", "tacos", "burgers", "fries"]
print(foods[1])
print(type(foods[1]))
print(foods[1].upper())

x = 12
y = 15.5
z = "Z"

random_list = [x, y, z]
print(random_list[0])
print(type(random_list[0]))

print(random_list[1])
print(type(random_list[1]))

print(random_list[2])
print(type(random_list[2]))

my_fav_num = random_list[0]
print(my_fav_num)

foods = ["pizza", "tacos", "burgers", "fries"]
foods.append("cheeseburger")
#DO NOT DO THIS => foods = foods.append("cheeseburger")
print(foods)
foods.insert(0, "Pho")
print(foods)

foods.remove("Pho")
print(foods)


foods = ["pizza", "tacos", "burgers", "fries"]
foods.append("pizza")
print(foods)
foods.remove("pizza")
print(foods)
#remove only removes the first instance


foods = ["pizza", "tacos", "burgers", "fries"]
print(foods)
#removes whatever instance you tell it to remove
del foods[1]
print(foods)


foods = ["pizza", "tacos", "burgers", "fries"]
#pop returns the element that you removed
print(foods.pop())
print(foods)


#method of the list class called .sort
#built in function called sorted()
#.sort is only on list. Only works on list. 
#sorted() works items that iterable 

#sort is in place
foods = ["pizza", "tacos", "burgers", "fries"]
print(foods.sort())
print(foods)
print(foods.sort(reverse=True))
print(foods)


#sorted is out of place
foods = ["pizza", "tacos", "burgers", "fries"]
print(sorted(foods))
print(foods)
foods = sorted(foods, reverse=True)
print(foods)
print("This command ends here")


foods = ["pizza", "tacos", "burgers", "fries"]
foods.reverse()
print(foods)

