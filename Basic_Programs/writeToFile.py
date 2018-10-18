f = open("demofile.txt", "a")
f.write("now the file has one more line")
#"a" will append the file
f = open("demofile.txt", "w")
f.write("the file still has one line")
#"w" will overwrite the file
f = open("demofile.txt", "x")
f.write("the file still has one line")
#"x" will create a file