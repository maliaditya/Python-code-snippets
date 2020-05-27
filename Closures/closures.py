# A closure gives you access to an outer function's scope from an inner function.

def pizzahut(item):

	def inner(cat):

		 	print("i want to buy a {1} {0}".format(item,cat))

	
	return inner


funpart = pizzahut("pizza")
funpart("Margherita")


