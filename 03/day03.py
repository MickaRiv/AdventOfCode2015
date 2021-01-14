import numpy as np

def update(loc,direc):
    return loc + np.array([(direc==">")-(direc=="<"),(direc=="^")-(direc=="v")],dtype=int)

data = open("input","r").readline()
location = np.zeros(2,dtype=int)
history = [location]
for direction in data:
    location = update(location,direction)
    history.append(location)
print(len(np.unique([",".join([str(h_i) for h_i in h]) for h in history])))

locationS = np.zeros(2,dtype=int)
locationR = np.zeros(2,dtype=int)
history = [locationS]
for i in range(len(data)//2):
    locationS = update(locationS,data[2*i])
    history.append(locationS)
    locationR = update(locationR,data[2*i+1])
    history.append(locationR)
print(len(np.unique([",".join([str(h_i) for h_i in h]) for h in history])))