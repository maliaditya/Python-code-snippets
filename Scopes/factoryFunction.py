def outer(X):
	
	def inner(y):
		return X +y
	return inner


o = outer(2)
print(o(3))