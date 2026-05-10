my_list = [1, 2, 2, 4, 6]
#print reverse
print(my_list[::-1])

student = {'user': 'Lubo',
           'pass': 'admin',
           'course': ['C# Fundamentals', 'C# ASP', 'Algorithms']}

for key in student:
    print(key)

for kvp in student.items():
    print(f'the key is: {kvp[0]}, and values are: {kvp[1]} ')


print(student['pass'])
print(student.get('Pass', 'Sorry mate no such key'))

if 'pass' in student.keys():
    print('Here')
else:
    print('Not here')

second_part_student = {
    'age': 25
}
student.update(second_part_student)
print(student)
