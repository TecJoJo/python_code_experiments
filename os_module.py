import os 

# print(os.getcwd())

os.chdir("\programming\python\python_code_experiments")

# for tuple in os.walk("\programming\python\python_code_experiments"):
#     dirpath,dirnames,filenames = tuple 
#     print("current path:", dirpath)
#     print("Directories:",dirnames)
#     print("Files:",filenames)

# print(os.walk("\programming\python\python_code_experiments"))
# print(os.getcwd())

# print(os.listdir())

# print(os.environ.get('Path'))#enviroment variable in windows 

# file_path = os.path.join("\programming\python\python_code_experiments","pathtest.txt")

# print(file_path)

print(os.path.basename("/temp/test.txt"))
print(os.path.dirname("/temp/test.txt"))
print(os.path.split("/temp/test.txt"))
print(os.path.exists("/temp/test.txt"))
print(os.path.isfile("/temp/test.txt"))
print(os.path.isdir("/temp/test.txt"))
print(os.path.splitext("/temp/test.txt"))