with open('/home/vachan/hexis/day4/file.txt',"r") as file:
    print(file.read())
    lines = file.readlines()
    # creating contxt..learn it...idk

for line in lines:
    print(line.strip("\n"))
#remove \n

file.seek(0) #just for pointing cursor to first location