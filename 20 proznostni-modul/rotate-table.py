from sys import stdin

l = []
for line in stdin:
    l.append(float(line))

for i in l[::-1]:
    print("-{}".format(i))