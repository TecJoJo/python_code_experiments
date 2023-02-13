# def gfi(max):
#     fibo_list = []
#     a,b = 0,1
#     while a <= max:
#         fibo_list.append(a)
#         temp_a = a
#         a = b
#         b = temp_a + b
#     return fibo_list
        
# def gfi(max):
#     fibo_list = []
#     a,b = 0,1
#     while a <= max:
#         fibo_list.append(a)
#         a,b = b,a+b
#     return fibo_list

#wrong way to generate fibonacci sequance, a is reassigned, a should have been reserved before the additon.
# def gfi(max):
#     fibo_list = []
#     a,b = 0,1
#     while a <= max:
#         fibo_list.append(a)
#         a = b
#         b = a+b
#     return fibo_list


    
#try to save the same problem with recursion 



def fib_list(max):
    
    def fib(n):
        if n == 0:
            return 0
        if n==1:
            return 1 
        else:
            return fib(n-1) + fib(n-2)
    
    # n = 0
    # while fib(n) <= max:
    #     n += 1
    
    # return list(map(fib,range(n)))

    

print(fib_list(100))

    

