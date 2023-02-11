nums = [1,2,3]
i_nums = iter(nums)
#i_nums = nums.__iter__()#do the same thing as the iter(nums)
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
# the forth call will trigger StopIteration
print(next(i_nums))