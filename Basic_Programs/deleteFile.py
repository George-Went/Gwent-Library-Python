import os # this imports the os module

if os.path.exists("demofile.txt"): #check if file exists
  os.remove("demofile.txt")
else:
  print("The file does not exist") 

import os
os.rmdir("myfolder") #deletes entire (empty) folder 