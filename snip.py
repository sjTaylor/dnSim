def twoD(m, n, val):
	a = []
	for x in range(0,m):
		b = []
		for y in range(0,n):
			b.append(val)
		a.append(b)
	return a