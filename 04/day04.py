import hashlib

def num(string):
	i=0
	while True:
		bdata = (data+str(i)).encode()
		hex = hashlib.md5(bdata).hexdigest()
		if hex.startswith(string):
			return i
		i+=1

data = "ckczppom"

print(num("00000"))
print(num("000000"))