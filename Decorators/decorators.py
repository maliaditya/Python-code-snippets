


def BigBazzar(func):

	def goingtomall():
		print("On the way to mall")
		return func()

	return goingtomall


@BigBazzar
def shopping():
	print("I love Shopping")


ready = BigBazzar(shopping)

shopping()