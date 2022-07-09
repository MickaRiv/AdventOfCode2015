import numpy as np

def isNice(string):
	if any(chars in string for chars in ["ab","cd","pq","xy"]):
		return False
	elif any(string[i]==string[i+1] for i in range(len(string)-1)):
		if np.sum([char in vowels for char in string]) > 2:
			return True
	return False
	
def isVeryNice(string):
	if any(string[i:i+2] in string[:i]+"-"+string[i+2:] for i in range(len(string)-1)):
		if any(string[i]==string[i+2] for i in range(len(string)-2)):
			return True
	return False
		
data = np.loadtxt("input05",dtype=str)
vowels = "aeiou"
print(np.sum([isNice(d) for d in data]))
print(np.sum([isVeryNice(d) for d in data]))