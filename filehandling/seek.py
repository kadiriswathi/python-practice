with open(r'C:\python practice\filehandling\name.txt', 'r') as file:
    file.seek(2) # Move to byte 7
    content = file.read()
    print(content) 