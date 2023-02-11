


def my_range(start, end):
    current = start
    while current < end:
        yield current 
        current +=1






#doesn't need to be end ever,but note using this with a for loop will
#result in an infinite loop which will crash you machine  


# def my_range(start):
#     current = start
#     while True:
#         yield current 
#         current +=1


nums = my_range(1,10)

print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))

for num in nums:
    print(num)



