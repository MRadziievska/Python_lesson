list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(list_a[0]) #1
# print(list_a[-1]) #10
# print(list_a[:5]) # : - по умолчанию от 0 до элемента после : (от 0 до 5)
# new_list = list_a[:5]
# print(list_a) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(new_list) #[1, 2, 3, 4, 5]
# print(list_a[2:]) # [3, 4, 5, 6, 7, 8, 9, 10] от первого эл. (20) до последнего (:)

message = "don't subscribe"
# print(message[6:]) # subscribe
# print(message[6:].upper()) #SUBSCRIBE
# print(list_a[-5:-2]) # [6, 7, 8]
# print(message[-5:-2]) # cri
# print([list_a[-2:-5]])  # []
# print(list_a[::2]) # [1, 3, 5, 7, 9] каждый 2 эл.
# print(list_a[::-1]) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(list_a[8:2:-1]) # [9, 8, 7, 6, 5, 4]
print(list_a[8:2:-2]) # [9, 7, 5]


