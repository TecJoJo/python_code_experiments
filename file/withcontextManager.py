#context manager
with open("G:\\programming\\python\\python_code_experiments\\dummyFolder\\test.txt", "r") as f:
    # f_contents = f.read()
    # f_contents = f.readlines()
    # print(f_contents)

    # for line in f:
    #     print(line, end="")


    size_to_read = 10
    
    # f_contents = f.read(size_to_read)
    # print(f_contents, end="")

    # f.seek(0)

    f_contents = f.read(size_to_read)
    print(f_contents,)
    print(f.tell())
    while len(f_contents) > 0:
        print(f_contents, end="*")
        f_contents = f.read(size_to_read)