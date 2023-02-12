nums = [1,2,3,4,5,6,7,8,9,10]


my_list = [n*n for n in nums]
print(my_list)

#side note about map and labda
# my_list_2 = map(lambda item: item*item, nums)


even_list = [n for n in nums if n%2 ==0]
print(even_list)