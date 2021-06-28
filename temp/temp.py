f = open("temp.txt", "r")
w = open("tempout.txt", "w")

for line in f :
    line = line.split()
    if len(line) == 2 :
        w.write(f"{line[1]}\n")