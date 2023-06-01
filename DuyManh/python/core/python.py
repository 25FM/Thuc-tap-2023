import modules
print(modules.A)
print(modules.md1.number)
print(modules.md2.number)
# Python3 program for explaining
# List, tuple, set and dictionary

list = ['5']
list2 = [2,3,5]
# Adding Element into list
list.append(5)
list.append(7)
list.append(10)
list.extend(list2)
list.remove(5)
print("Adding 5, 7 and 10 in list", list)

# Popping Elements from list
list.pop()  # lấy ra phần tử trên cùng
print("Popped one element from list", list)
print()


# Set
s = set()

# Adding element into set
s.add(5)
s.add(10)
print("Adding 5 and 10 in set", s)

# Removing element from set
s.remove(5)
print("Removing 5 from set", s)
print()

# Tuple
tuples = ("hello", ("python", "world"))
Tuple = ("a", "b", "c", "d", "e", "f")
Tuple = [(0, 1), (2, 3), (4, 5)]

# Tuples are immutable
print(Tuple[2][1])
print("Tuple", tuples[1])
print()

# Dictionary
d = {}

# Adding the key value pair
d[5] = "Five"
d[10] = "Ten"
d[7] = "Seven"
# print("Dictionary", d)
print("Dictionary: ", d)

# Removing key-value pair
del d[10]
print("Dictionary", d)

'''
Comment theo nhiều dòng
sử dụng """""" hoặc ''''''
'''

list1 = [1, 2, 3]
list1.append([4, 5, 6])
print(list1)

# ------------------------------------------------------
# static method
class Phone_number:
    def __init__(self, brand, number):
        self.brand = brand
        self.number = number

    def get_number(self):
        return self.number

    @staticmethod
    def get_emergency_number():
        return "113"


user = Phone_number("Samsung", "31232")
phone = Phone_number.get_number(user)
phone_police = Phone_number.get_emergency_number()
print(phone)
print(phone_police)

# ------------------------------------------------------
# class method
class Person:
    def __init__(self, age, name, email):
        self.age = age
        self.name = name
        self.email = email
