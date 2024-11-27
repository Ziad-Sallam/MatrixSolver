
def max_error(x1,x):
	n=len(x1)
	max=0
	for i in range (0,n):
		if (abs(x1[i]-x[i])/x1[i]>max):
			max=abs(x1[i]-x[i])/x1[i]
	return max
		
		
def seidel(a, x, e=0, no_I=10000):
	n = len(a)				 
	x1=x.copy()
	ilteration=0
	while(True):
		ilteration += 1
		x=x1.copy()
		for j in range(0, n):
			d = a[j][n]
			for i in range(0, n):
				if(j != i):
					d-=a[j][i] * x1[i]
			x1[j] = d / a[j][j]	 
		
		if ((max_error(x1,x)<e) or ilteration>=no_I ):
			break
		else:
			continue
			 
	return x1 


# intial conditons
x = [0,0,0,0,0,0,0,0,0,0]	

# Augmented matrix for the system
a = [
    [10, 1, 2, 3, 1, 0, 0, 0, 0, 0, 10],
    [2, 20, 3, 4, 1, 0, 0, 0, 0, 0, 25],
    [1, 1, 30, 1, 2, 0, 0, 0, 0, 0, 35],
    [2, 0, 1, 40, 1, 0, 0, 0, 0, 0, 45],
    [0, 2, 1, 1, 50, 0, 0, 0, 0, 0, 55],
    [0, 0, 0, 0, 1, 60, 1, 0, 0, 0, 65],
    [0, 0, 0, 0, 0, 2, 70, 1, 0, 0, 75],
    [0, 0, 0, 0, 0, 0, 2, 80, 1, 0, 85],
    [0, 0, 0, 0, 0, 0, 0, 1, 90, 1, 95],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 100, 105]
]

# Solution array
# x_solution = [
#     0.294,
#     0.804,
#     1.026,
#     1.059,
#     1.026,
#     1.049,
#     1.027,
#     1.024,
#     1.033,
#     1.040
# ]
	 
Ans = seidel(a, x)
print(Ans)

Ans_rounded = [round(x, 3) for x in Ans]
print(Ans_rounded)
