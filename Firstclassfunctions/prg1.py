# def cube(x):
# 	return x*x*x

# def my_func(func,list):
# 	result = []
# 	for i in list:
# 		result.append(func(i))

# 	return result

# cubes = my_func(cube, [1,2,3,4,5])
# print(cubes) 



def logger(msg):

	def log_message(text):
		print("Log:{0} {1}".format(msg,text))

	return log_message

log_hi = logger('hi')
log_hi("adi")

# def html_tag(tag):

# 	def wrap_text(msg):
# 		print("<{0}>{1}<{0}>".format(tag,msg))

# 		return wrap_text

# f = html_tag('hi')
# f('header')