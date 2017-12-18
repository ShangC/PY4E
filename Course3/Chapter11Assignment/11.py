import re

# This is the only work-around to make sure VS Code can read the file in terminal directly.
# Remember to remove the directory when uploading to assignment because it will cause FileNotFoundError
# c:/Users/AdminWLGlobal/Desktop/py4e/Course3/Chapter11Assignment/
# otherwise simply type the python command in below terminal will bypass the path problem
fhandle = open('regex_sum_44132.txt')

for line in fhandle:
    line = line.rstrip()
    numberInLine = re.findall('[0-9]+', line)
    print(numberInLine)
