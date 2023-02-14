# import required module
import os
# assign directory
directory = 'files'

# iterate over files in
# that directory
for filename in os.listdir("..\\python_code_experiments"):
	f = os.path.join("..\\python_code_experiments", filename)
	# checking if it is a file
	# if os.path.isfile(f):
	print(f)
