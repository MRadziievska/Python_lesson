#1
# grades = [5, 3, 4, 2, 5]
# my_list = grades[::]
# for g  in my_list:
#     if g <= 3:
#         grades.remove(g)
# print(grades)

#2
# l_1 = ["apple", "lemon", "gpt"]
# l_2 = ["git", "tea", "python"]
# l_1.extend(l_2)
# print(l_1)
# for word in l_1:
#     char_count = len(word)
#     print(f"Word:  '{word}', Count: {char_count}")

#3
l_3 = ["apple", "grape", "kiwi", "pear", "melon", "banana", "mango"]
l_3.sort(key=len, reverse=True)
print(l_3)









