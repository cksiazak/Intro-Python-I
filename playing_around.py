# # prints hello world
# print("Hello, world!")

# name = "Tim"

# print(name)

# print("hello " + name)
# print("hello " + "world")
# print("Hello", name)

# # string interpolation
# print(f"Hello {name}")

# # creates an array
# my_list = [1, 2, "test1"]
# # appends to back of array
# my_list.append("Test")
# print(my_list)

# # for loop in list above
# for i in my_list:
#     print(i)
#     print(i)

# # range
# for i in range(len(my_list)):
#     print('this is range', i, my_list[i])

# # enumerate
# for (idx, el) in enumerate(my_list):
#     print('this is enumerate', idx, el)

# numbers = [1,2, 3, 4, 5]

# squares = [num * num for num in numbers]
# print(squares)

# halves = [num / 2 for num in numbers]
# print(halves)

# evens = [num for num in numbers if num % 2 == 0]
# print(evens)

names = ["andrea", "gwen", "stephanie", "sagdi", "yankho", "tim"]
# get all names that start with S and capitalize
s_names = [name.capitalize() for name in names if name.startswith("s")]
print(s_names)

my_dict = {"a": 1, "b": 2}
my_dict["c"] = 3
print(my_dict)

for k in my_dict:
    print(k)


my_tuple = ("a", 1, 3)