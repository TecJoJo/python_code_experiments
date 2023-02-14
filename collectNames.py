# import required module
import os
def lowerCase(word):
    return    word.lower()

# iterate over files in
# that directory
categoryList = []

# I used relative path here, use folder path as parameter
for filename in os.listdir("..\\python_code_experiments"):
    if filename.startswith("."):
        continue

    elif filename == "main.py" or filename == "CategoryTitles.txt" or  filename == "CategoryTitles.txt" or filename == "new_states.json" or filename == "readme.md" or filename == "src" or filename == "dummyFolder":
        continue 

    elif filename.endswith(".py"):
        categoryList.append(filename[:-3]) 
    else:
        categoryList.append(filename)

categoryList.sort(key=lowerCase)



result = "\n* ".join(categoryList)
result = "* " + result

with open("CategoryTitles.txt","w") as w:
    w.write(result)