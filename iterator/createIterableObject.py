class MyRange:

    def __init__(self,start,end):
        self.value = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current 






nums = MyRange(1,10)

# for loop works which means it is a iterable 
# for num in nums:
#     print(num)

#it is also a iterator because it has a __next__ method 

print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
