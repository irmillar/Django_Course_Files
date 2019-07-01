try:
    f = open("simple.txt", "r+")
    f.write("Test write to simple text!")
except IOError:
    print("Error: COULD NOT FIND FILE OR READ DATA!")
else:
    print("SUCCESS!")
    print(f.read)
    f.close()
