
def BigBazzar(func):

	def goingtomall():
		print("On the way to mall")
		return func()

	return goingtomall


@BigBazzar
def shopping():
	print("I love Shopping")

#the abov line is same as the below line
ready = BigBazzar(shopping)

shopping()