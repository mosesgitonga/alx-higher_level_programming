#!/usr/bin/python3

def append_after(filename="", search_string="", new_string=""):
    with open(filename, mode="r+", encoding="utf-8") as myfile:
        lines = myfile.readlines()
        myfile.seek(0)
        for line in lines:
            myfile.write(line)
            if search_string in line:
                myfile.write(new_string)
    myfile.close()

    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read())

