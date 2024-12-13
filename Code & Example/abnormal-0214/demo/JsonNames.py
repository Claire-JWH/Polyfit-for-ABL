import os

name = os.listdir("../json/")

m = []

for i in name:
    m.append(i[0:-5])
print(m)

