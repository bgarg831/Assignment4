try:
    with open('sample.txt','r+') as file:
        print("Reading file content:\n" + file.read())
except FileNotFoundError:
    print("Error: The file sample.txt was not found.")
