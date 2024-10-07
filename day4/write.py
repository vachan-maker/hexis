with open('day4/write.txt',"w") as file:
    file.write("Hello from Python!!")
#overwrites the entire file
with open('day4/write.txt',"a") as file:
    file.write("\nHello from Python!!---appended string")
#appends the file
