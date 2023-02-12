nums = [1,2,3,4,5,6,7,8,9,10]

# my_list = []
# for letter in "abcd":
#     for num in range(4):
#         my_list.append((letter,num))
# print(my_list)

my_list = [(letter,num) for letter in "abcd" for num in range(4)]

print(my_list)

