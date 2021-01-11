data = open("input","r").readline()
dataCount = data.replace("(","+1").replace(")","-1")
print(eval(dataCount))
p = 0
for i,d in enumerate(data):
    p += (d=="(")-(d==")")
    if p < 0:
        print(i+1)
        break