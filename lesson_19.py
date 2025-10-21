# def add(number_one, number_two):
#     result = number_one + number_two
#     print(result)  # 8
#
# our_result = add(3, 5)
# print(our_result)  # None так как не возвращает

# def add(number_one, number_two):
#     result = number_one + number_two
#     return result
#
# our_result = add(3, 5)
# print(our_result) # 8,


def add(number_one, number_two):
    result = number_one + number_two
    return result

def exp(number):
    return number ** 2

our_result = exp(add(3, 5))
# our_exp = exp(our_result)   # = our_result = exp(add(3, 5))
print(our_result)
# print(our_exp)              # в этом случае это лишнее




