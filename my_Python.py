a = input("a")
b = input("b")
sum = int(a)+int(b)
print(sum)
tuple = (a, b, sum)
print(tuple)
tup = (10, 34, 123)
print(tup)
# print(type(tup))
tuple = (1, 1, 3, 4, 5)
print(tuple.index(3))
print(tuple.count(1))
movies = []
mov1 = input("Enter first movie: ")
mov2 = input("Enter second movie: ")
mov3 = input("Enter third movie: ")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
movies.append(input("Enter 4th movie: "))
print(movies)

list1 = [1, 2, 3]
copy_list1 = list1.copy()
copy_list1.reverse()
if (copy_list1 == list1):
    print("Palindrome")
else:
    print("Not a palindrome")
print(copy_list1)
grade = ["Grade A", "Grade B", "Grade A", "Grade D", "Grade A", "Grade C"]
grade.sort()
print(grade)


# def new_func():
#     dict = {
#     "name": "Manish",
#     "age": 30,
#     "is_student": True,
#     "cgpa":7.8,
#     "topics" : ("Python", "Java", "C++"),
#     "learning" : ["Python", "Java", "C++"],
#     "city": "Benagaluru"
# }
#     print(dict)

# new_func()


