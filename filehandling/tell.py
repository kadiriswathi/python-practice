with open(r'C:\python practice\filehandling\name.txt', 'r') as file:
    print(file.tell())  # Output: 0 (start of file)
    content = file.read(10)  # Read 5 characters
    print(content)         # Assume file has "Hello, world!"
    print(file.tell())     # Output: 5 (moved 5 bytes)