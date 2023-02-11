nums = [1,2,3]

for num in nums:
    print(num)

i_nums = nums.__iter__()
# i_nums = iter(nums)

print(dir(nums))
print(dir(i_nums))
print(i_nums)


