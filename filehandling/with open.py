with open('name.txt') as fr, open('WRITE.txt', 'w') as fw:
    fw.write(fr.read())
