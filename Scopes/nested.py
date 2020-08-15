def maker(N):
	def action(x):
		print(N+" will "+x)
	return action

print("lunch: ")
f = maker('mummy')

f('make Chapati')

d = maker("Didi")

d('make Bhaji')

print()

print("Dinner: ")

f('make Chapati')
f('make Bhaji')
f('make Rice')

print()


dine = maker('The we all')
dine('be having our dinner.')