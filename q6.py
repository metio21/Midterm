#shows how lists are mutable
my_list = [1, 2, 3]
print("Original list:", my_list)

my_list[1] = 99
print("Modified list:", my_list)

my_list.append(4)
print("List after appending:", my_list)

#shows how string are immutable
my_string = "hello"
print("Original string:", my_string)

try:
    my_string[0] = "H"
except TypeError as error:
    print("Error when modifying string:", error)

