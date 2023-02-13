import os
import shutil
#print(dir(os)
path=os.getcwd()
print("the current working directory is",path)
#os.mkdir(";)")
result=os.listdir("C:/Users/Admin/OneDrive/Desktop")
print(result)
C=os.path.exists("C:/Users/Admin/OneDrive/Desktop/ABC")
print(C)
root,ext=os.path.splitext("C:/Users/Admin/OneDrive/Desktop/boat.jpg")
print("the root of the message is",root)
print("the ext of the message is",ext)


destination="C:/Users/Admin/OneDrive/Desktop/c111"
source="C:/Users/Admin/OneDrive/Desktop/The Tempest Project"
files=os.listdir(source)
for i in files:
    name,ext=os.path.splitext(i)
    print(name,ext)
    result=shutil.move(source,destination)