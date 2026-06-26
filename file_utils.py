def write_file(filename, text):
    file = open(filename, "w")
    file.write(text)
    file.close()
    print("Data written successfully")


def read_file(filename):
    file = open(filename, "r")
    print(file.read())
    file.close()


def append_file(filename, text):
    file = open(filename, "a")
    file.write(text)
    file.close()
    print("Data added")