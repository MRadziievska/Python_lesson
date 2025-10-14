#1
# def foo():
#     print('Hello!')
#     name = input('What is your name? ')
#     print(name, 'Nice to meet you!')
#
# foo()
# foo()
# foo()

#2
# def foo():
#     number = float(input('Number: '))
#     return number
# print(foo() + foo())

#3
# def foo():
#     my_list = list(input('Number: '))
#     return my_list
# print(foo() + foo())

def foo():
    input_str = input("Введите числа через пробел: ")
    numbers = [float(num) for num in input_str.split()]
    return numbers

nums1 = foo()
nums2 = foo()

all_numbers = nums1 + nums2

average = sum(all_numbers) / len(all_numbers)

print(f"Общий список: {all_numbers}")
print(f"Среднее значение: {average}")












