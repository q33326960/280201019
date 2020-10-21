fhand = open("/home/cem/PycharmProjects/280201019/README")
char = fhand.read()
print(len(char))
count = 0
for line in fhand:
    count = count + 1
print(count)
fhand = open("/home/cem/PycharmProjects/280201019/README")
for line in fhand:
    line = line.rstrip()
    if line.startswith("19"):
        print(line)
