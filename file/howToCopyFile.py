with open("G:\\programming\\python\\python_code_experiments\\dummyFolder\\test.txt", "r") as rf:
    with open("G:\\programming\\python\\python_code_experiments\\dummyFolder\\test_copy.txt", "w") as wf:
        for line in rf:
            wf.write(line)




