def hello(name="Ian"):
    print("The Hello Function has been run")

    def greet():
        return "greet func"

    def welcome():
        return "This is inside welcome"

    if name == "Ian":
        return greet
    else:
        return welcome

x = hello()
print(x())
y = hello("sam")
print(y())
