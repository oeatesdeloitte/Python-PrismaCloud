filename = input("Enter a filename: ")
with open("/var/data/" + filename, "r") as file:
    content = file.read() #
