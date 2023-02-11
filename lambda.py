def power(n):
    return lambda x : x**n


raisePowerOf3 = power(3)
raisePowerOf2 = power(2)

print(raisePowerOf2(3))
print(raisePowerOf3(2))


print(power(4)(10))