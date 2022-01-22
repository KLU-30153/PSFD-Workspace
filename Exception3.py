try:
    klu1 = open("file.txt", "r")
    try:
        klu1.read("This is S1 Section")
    finally:
        klu1.close()
except IOError:
            print("File not Found")
else:
    print("The file opened Successfully")
    klu1.close()