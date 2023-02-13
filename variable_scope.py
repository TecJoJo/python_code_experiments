#LEGB
#Local --> Enclosing --> Global --> Built-in

def outer():
    x = "outer x"
    def inner():
        nonlocal x
        x = "inner x"
        print(x)
    inner()
    print(x)
outer()