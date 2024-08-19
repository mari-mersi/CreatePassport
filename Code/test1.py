def new_line(path,line):
    with open(path, 'a') as file:
        file.write(line+"\n")


file_path = "output.txt"
text=["1","2","3"]
new_line(file_path,text[0])
new_line(file_path,text[1])
new_line(file_path,text[2])
