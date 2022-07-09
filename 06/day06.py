import numpy as np

def update(lights,cmd,brightness=False):
	cmdData = cmd.split()
	starts = np.array(cmdData[-3].split(","),dtype=int)
	ends =  np.array(cmdData[-1].split(","),dtype=int)
	sizes = ends - starts + 1
	if cmdData[1] == "on":
		if brightness:
			new = lights[starts[0]:ends[0]+1,starts[1]:ends[1]+1] + 1
		else:
			new = np.ones(sizes)
	elif cmdData[1] == "off":
		if brightness:
			new = np.clip(lights[starts[0]:ends[0]+1,starts[1]:ends[1]+1] - 1,0,np.inf)
		else:
			new = np.zeros(sizes)
	else:
		if brightness:
			new = lights[starts[0]:ends[0]+1,starts[1]:ends[1]+1] + 2
		else:
			new = 1 - lights[starts[0]:ends[0]+1,starts[1]:ends[1]+1]
	lights[starts[0]:ends[0]+1,starts[1]:ends[1]+1] = new

data = np.loadtxt("input06",dtype=str,delimiter=";")
lights = np.zeros((1000,1000))
for d in data:
	update(lights,d)
print(np.sum(lights))

lights = np.zeros((1000,1000))
for d in data:
	update(lights,d,True)
print(np.sum(lights))