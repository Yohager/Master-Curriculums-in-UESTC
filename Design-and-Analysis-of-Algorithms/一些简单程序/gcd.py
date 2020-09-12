import sys

def gcd1(m,n):
	while (n!=0):
		r = m%n
		m = n
		n = r
	return m

def gcd2(m,n):
	if n == 0:
		return m
	return gcd2(n,m%n)

if __name__ == "__main__":
	argvs = sys.argv
	m = int(argvs[1])
	n = int(argvs[2])
	print(gcd2(m,n))
	