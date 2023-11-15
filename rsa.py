import math
def gcd(a, h):
	temp = 0
	while(1):
		temp = a % h
		if (temp == 0):
			return h
		a = h
		h = temp
p,q,e = 3,7,2
n = p*q
phi = (p-1)*(q-1)

while (e < phi):
    if(gcd(e, phi) == 1):
		break
	else:
		e = e+1

k,msg = 2,12.0
d = (1 + (k*phi))/e
print("Message data = ", msg)
c = pow(msg, e)
c = math.fmod(c, n)
print("Encrypted data = ", c)
m = pow(c, d)
m = math.fmod(m, n)
print("Original Message Sent = ", m)
