# def outer_func():
#     message = "hi"
#     def inner_func():
#         print(message)
#     return inner_func

# my_func = outer_func()
# my_func()
# my_func()
# my_func()

def outer_func(msg):
    message = msg
    def inner_func():
        print(message)
    return inner_func

hi_func = outer_func("hi")
hello_func = outer_func("hello")

hi_func()
hello_func()