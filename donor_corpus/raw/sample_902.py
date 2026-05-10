# 
# vect3dotfun.py
# Dot product of two 3-d vectors using function in Python 3.7
#
# Sparisoma Viridi | https://github.com/dudung
# 
# 20210110
# 2001 Start creating this example.
# 2002 Test it and ok.
# 

# Define dot function with two arguments
def dot(a, b):
	p = a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
	return p

# Define two vector using array
r1 = [1, 2, 3]
r2 = [2, 2, 9]

# Calculate dot product of two vectors
p = dot(r1, r2)

# Display result
print("r1 = ", r1, sep="");
print("r2 = ", r2, sep="");
print("p = r1 \xb7 r2 = ", p, sep="");
