def parse():
    f1 = open("sample.txt", "r")
    words = []
    for line in f1:
        words.append(line.split(" "))
    f2 = open("test.txt", "w")
    f2.write(words.__str__())
    f2.close()

parse()
