# create an empty list
my_list = []
# add items to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)
# insert 15 at the second post
my_list.insert(1, 15)
print(my_list)
# extend the list
my_list.extend([50, 60, 70])
print(my_list)
# removing the last element
my_list.pop()
print(my_list)
# sorting the list in ascending order
my_list.sort()
print(my_list)
# finding the index of 30
index_of_30 = my_list.index(30)
print(index_of_30)