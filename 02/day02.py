import numpy as np

def area(a):
    s = [a[0]*a[1],a[0]*a[2],a[1]*a[2]]
    return 2*(np.sum(s))+np.min(s)

def ribbon(a):
    return 2*(np.sum(a)-np.max(a))+np.prod(a)

data = np.loadtxt("input",delimiter="x",dtype=int)
print(np.sum([area(d) for d in data]))
print(np.sum([ribbon(d) for d in data]))